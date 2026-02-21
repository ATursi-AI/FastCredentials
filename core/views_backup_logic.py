from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
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
from .forms import CertificateSignupForm

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    courses = Course.objects.all().order_by('-priority', 'title')
    return render(request, 'home.html', {'courses': courses})

@login_required
def dashboard(request):
    courses = Course.objects.all().order_by('-priority', 'title')
    one_year_ago = timezone.now() - timedelta(days=365)
    user_certs = Certificate.objects.filter(user=request.user)
    cert_map = {c.course.id: c.cert_id for c in user_certs}
    has_annual_pass = Payment.objects.filter(user=request.user, date__gte=one_year_ago, amount__gte=49.00).exists()
    paid_course_ids = Payment.objects.filter(user=request.user, date__gte=one_year_ago).values_list('course_id', flat=True)
    
    for course in courses:
        course.user_cert_id = cert_map.get(course.id)
        course.is_completed = (course.id in cert_map)
        course.has_paid = request.user.is_superuser or has_annual_pass or (course.id in paid_course_ids)
        title = course.title.upper()
        if any(x in title for x in ['FORKLIFT', 'ALCOHOL', 'FOOD']):
            course.badge_text, course.badge_color = '3-YEAR CERT', '#ffc107'
        elif any(x in title for x in ['FIRST AID', 'CPR', 'AED', 'BLS', 'HEALTHCARE']):
            course.badge_text, course.badge_color = '2-YEAR CERT', '#198754'
        else:
            course.badge_text, course.badge_color = 'ANNUAL REQ', '#0d6efd'

    return render(request, 'dashboard.html', {'courses': courses, 'completed_count': user_certs.count()})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

def take_quiz(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    all_questions = list(course.questions.all())
    
    if request.method == 'POST':
        # Handle Name Submission from Quiz Result Page
        if 'cert_name' in request.POST:
            request.session['guest_cert_name'] = request.POST.get('cert_name')
            # Redirect to the certificate view using the course ID as a temporary marker
            return redirect('certificate_view', cert_id=f"PREVIEW-{course.id}")

        # Handle Quiz Submission
        submitted_ids = [int(k.split('_')[1]) for k in request.POST.keys() if k.startswith('question_')]
        score = sum(1 for q in all_questions if q.id in submitted_ids and int(request.POST.get(f'question_{q.id}')) == q.correct_option)
        percentage = (score / len(submitted_ids)) * 100 if submitted_ids else 0
        
        if percentage >= 100:
            if request.user.is_authenticated:
                cert, _ = Certificate.objects.get_or_create(user=request.user, course=course)
                return redirect('certificate_view', cert_id=cert.cert_id)
            
            # Guest Passed: Save progress to session but stay here to show Name Box
            request.session[f'passed_course_{course.id}'] = True
            request.session['latest_passed_course'] = course.title
            return render(request, 'quiz_result.html', {'course': course, 'passed': True, 'score': 100})
            
        return render(request, 'quiz_result.html', {'course': course, 'passed': False, 'score': int(percentage)})

    random.shuffle(all_questions)
    questions_data = [{'question': q, 'options': sorted([(q.option_1,1),(q.option_2,2),(q.option_3,3),(q.option_4,4)], key=lambda x: random.random())} for q in all_questions[:10]]
    return render(request, 'take_quiz.html', {'course': course, 'questions_data': questions_data})

def certificate_view(request, cert_id):
    # Calculate expiration (1 year from now)
    expire_date = timezone.now() + timedelta(days=365)

    # GUEST PREVIEW LOGIC
    if cert_id.startswith('PREVIEW-'):
        course_id = cert_id.split('-')[1]
        course = get_object_or_404(Course, pk=course_id)
        
        # 1. Create a "Hologram" User
        class MockUser:
            def __init__(self, first, last):
                self.first_name = first
                self.last_name = last
                self.username = 'guest'
                self.email = 'guest@example.com'
                self.pk = None
                self.id = None
                self.is_authenticated = False
                self.is_staff = False
                self.is_superuser = False

        # 2. Create a "Hologram" Certificate (Bypasses models.py entirely)
        class MockCertificate:
            def __init__(self, course, cert_id, user):
                self.course = course
                self.cert_id = cert_id
                self.issued_at = timezone.now()
                self.user = user
                self.pdf_file = None # No PDF yet
                self.pk = None
                self.id = None

        # Get name from session
        full_name = request.session.get('guest_cert_name', 'Valued Candidate').split(' ', 1)
        first_name = full_name[0]
        last_name = full_name[1] if len(full_name) > 1 else ''
        
        # Instantiate the Hologram
        cert = MockCertificate(course, cert_id, MockUser(first_name, last_name))
        
        return render(request, 'certificate_view.html', {
            'cert': cert, 
            'has_paid': False,
            'expire_date': expire_date
        })

    # EXISTING USER LOGIC (Standard Flow)
    cert = get_object_or_404(Certificate, cert_id=cert_id, user=request.user)
    one_year_ago = timezone.now() - timedelta(days=365)
    
    # Check payments
    has_paid = request.user.is_superuser or \
               Payment.objects.filter(user=request.user, date__gte=one_year_ago, amount__gte=49.00).exists() or \
               Payment.objects.filter(user=request.user, course=cert.course, date__gte=one_year_ago).exists()
    
    # Handle Name Confirmation for Paid Users
    if request.method == 'POST' and 'confirm_name' in request.POST and has_paid:
        if not cert.pdf_file:
            if request.POST.get('first_name'):
                request.user.first_name = request.POST.get('first_name')
                request.user.last_name = request.POST.get('last_name')
                request.user.save()
            cert.pdf_file = generate_certificate_pdf(cert)
            cert.save()
        return redirect('certificate_view', cert_id=cert_id)
        
    return render(request, 'certificate_view.html', {
        'cert': cert, 
        'has_paid': has_paid,
        'expire_date': cert.issued_at + timedelta(days=365)
    })

@login_required
def create_checkout_session(request, course_id):
    plan_type = request.GET.get('plan', 'single')
    if plan_type == 'annual':
        course = Course.objects.filter(id=course_id).first() or Course.objects.first()
        if not course: return render(request, 'dashboard.html', {'error': 'No courses available.'})
        price_amount, product_name = 4999, "FastCredentials Annual Pass"
    else:
        course = get_object_or_404(Course, id=course_id)
        price_amount, product_name = 1999, f"Certification: {course.title}"
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price_data': {'currency': 'usd', 'product_data': {'name': product_name}, 'unit_amount': price_amount}, 'quantity': 1}],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('payment_success')) + f'?session_id={{CHECKOUT_SESSION_ID}}&course_id={course.id}&amount={price_amount}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        courses = Course.objects.all().order_by('-priority', 'title')
        return render(request, 'dashboard.html', {'courses': courses, 'error': f"Stripe Error: {str(e)}"})

@login_required
def payment_success(request):
    session_id, course_id, amount_param = request.GET.get('session_id'), request.GET.get('course_id'), request.GET.get('amount')
    if session_id:
        Payment.objects.create(user=request.user, course=get_object_or_404(Course, id=course_id), stripe_charge_id=session_id, amount=float(amount_param)/100.0 if amount_param else 19.99)
    return redirect('dashboard')

def payment_cancel(request): return redirect('dashboard')

def signup(request):
    if request.user.is_authenticated: return redirect('dashboard')
    if request.method == 'GET' and request.GET.get('plan'): request.session['pending_plan'] = request.GET.get('plan')
    
    promo_message = f"CONGRATULATIONS! You Passed {request.session.get('latest_passed_course')}. Create account to view certificate." if request.session.get('latest_passed_course') else None
    
    if request.method == 'POST':
        form = CertificateSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # SURGICAL CHANGE START: Track if we found a passed course
            redirect_course_id = None
            for c in Course.objects.all():
                if request.session.get(f'passed_course_{c.id}'):
                    # Create the cert record silently
                    Certificate.objects.get_or_create(user=user, course=c)
                    redirect_course_id = c.id # Capture the Course ID
                    del request.session[f'passed_course_{c.id}']
            
            # Handle Annual Plan Redirect
            if request.session.pop('pending_plan', None) == 'annual':
                cid = Course.objects.first().id if Course.objects.exists() else 1
                return redirect(reverse('create_checkout_session', kwargs={'course_id': cid}) + '?plan=annual')
            
            # FRICTIONLESS BYPASS: Go STRAIGHT to Stripe (Skip Certificate View)
            if redirect_course_id:
                return redirect('create_checkout_session', course_id=redirect_course_id)
                
            return redirect('dashboard')
            # SURGICAL CHANGE END
            
    return render(request, 'signup.html', {'form': CertificateSignupForm(), 'promo_message': promo_message})

def about(request): return render(request, 'about.html')
def support(request): return render(request, 'support.html')
def terms(request): return render(request, 'terms.html')
def ai_monitoring(request): return render(request, "ai.html")

def verify_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, cert_id=cert_id)
    # Verification always shows the "Paid/Valid" version because it's public proof
    return render(request, 'certificate_view.html', {'cert': cert, 'has_paid': True})
