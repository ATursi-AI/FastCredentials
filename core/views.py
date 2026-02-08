from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import stripe
import os
import random
from .models import Course, Question, Certificate, Payment
from .utils import generate_certificate_pdf

# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

@login_required
def dashboard(request):
    courses = Course.objects.all()
    one_year_ago = timezone.now() - timedelta(days=365)
    user_certs = Certificate.objects.filter(user=request.user, issued_at__gte=one_year_ago)
    completed_count = user_certs.count()
    cert_map = {c.course.id: c.cert_id for c in user_certs}
    paid_courses = Payment.objects.filter(user=request.user, date__gte=one_year_ago).values_list('course_id', flat=True)

    for course in courses:
        course.user_cert_id = cert_map.get(course.id)
        course.is_completed = (course.id in cert_map)
        course.has_paid = (course.id in paid_courses) or request.user.is_superuser

    return render(request, 'dashboard.html', {
        'courses': courses, 
        'completed_count': completed_count
    })

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if not request.user.is_authenticated:
        return render(request, 'course_locked.html', {'course': course})
    
    one_year_ago = timezone.now() - timedelta(days=365)
    has_paid = Payment.objects.filter(
        user=request.user, 
        course=course,
        date__gte=one_year_ago 
    ).exists()

    if not has_paid and not request.user.is_superuser:
        return render(request, 'course_locked.html', {'course': course})
        
    return render(request, 'course_detail.html', {'course': course})

@login_required
def take_quiz(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    one_year_ago = timezone.now() - timedelta(days=365)
    has_paid = Payment.objects.filter(user=request.user, course=course, date__gte=one_year_ago).exists()

    if not has_paid and not request.user.is_superuser:
        return redirect('course_detail', course_id=course.id)

    all_questions = list(course.questions.all())

    if request.method == 'POST':
        score = 0
        submitted_question_ids = [int(key.split('_')[1]) for key in request.POST.keys() if key.startswith('question_')]
        total_attempted = len(submitted_question_ids)
        missed_lessons = []

        for q in all_questions:
            if q.id in submitted_question_ids:
                user_answer = request.POST.get(f'question_{q.id}')
                if user_answer and int(user_answer) == q.correct_option:
                    score += 1
                else:
                    if hasattr(q, 'related_lesson') and q.related_lesson:
                        missed_lessons.append(q.related_lesson)

        missed_lessons = list(set(missed_lessons))
        percentage = (score / total_attempted) * 100 if total_attempted > 0 else 0

        if percentage >= 100:
            cert, created = Certificate.objects.get_or_create(user=request.user, course=course)
            if not created and cert.issued_at < one_year_ago:
                cert.delete()
                cert = Certificate.objects.create(user=request.user, course=course)
            
            # Redirect to naming screen - PDF generation happens there
            return redirect('certificate_view', cert_id=cert.cert_id)
        else:
            return render(request, 'quiz_result.html', {
                'course': course, 
                'passed': False, 
                'score': int(percentage),
                'missed_lessons': missed_lessons
            })

    random.shuffle(all_questions)
    selected_questions = all_questions[:10]
    return render(request, 'take_quiz.html', {'course': course, 'questions': selected_questions})

@login_required
def certificate_view(request, cert_id):
    cert = get_object_or_404(Certificate, cert_id=cert_id)

    # Handle Name Confirmation and PDF Generation
    if request.method == 'POST' and 'confirm_name' in request.POST:
        # Only allow naming/locking if PDF hasn't been generated yet
        if not cert.pdf_file:
            request.user.first_name = request.POST.get('first_name')
            request.user.last_name = request.POST.get('last_name')
            request.user.save()
            
            # Generate and Save PDF (This Locks the Name)
            pdf_path = generate_certificate_pdf(cert)
            cert.pdf_file = pdf_path
            cert.save()

            # Send Email only once at the moment of locking
            try:
                subject = f"Official Certificate: {cert.course.title}"
                body = (f"Congratulations {request.user.first_name} {request.user.last_name},\n\n"
                        f"You have successfully passed the exam for '{cert.course.title}'.\n\n"
                        f"Your official locked credential is attached to this email.\n\n"
                        f"Best regards,\nThe FastCredentials Team")
                email = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [request.user.email])
                email.attach_file(cert.pdf_file.path)
                email.send()
            except Exception as e:
                print(f"EMAIL ERROR: {e}")

        return redirect('certificate_view', cert_id=cert_id)

    return render(request, 'certificate_view.html', {'cert': cert})

def verify_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, cert_id=cert_id)
    return render(request, 'verify_certificate.html', {'cert': cert})

@login_required
def create_checkout_session(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': f"All-Access: {course.title}"},
                    'unit_amount': int(course.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')) + f'?session_id={{CHECKOUT_SESSION_ID}}&course_id={course.id}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return render(request, 'course_locked.html', {'course': course, 'error': str(e)})

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')
    course_id = request.GET.get('course_id')
    if session_id and course_id:
        primary_course = get_object_or_404(Course, id=course_id)
        all_courses = Course.objects.all()
        for course in all_courses:
            Payment.objects.create(
                user=request.user, 
                course=course, 
                stripe_charge_id=session_id, 
                amount=primary_course.price if course == primary_course else 0
            )
        return redirect('course_detail', course_id=primary_course.id)
    return redirect('dashboard')

def payment_cancel(request):
    return redirect('dashboard')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def about(request): return render(request, 'about.html')
def support(request): return render(request, 'support.html')
def terms(request): return render(request, 'terms.html')
