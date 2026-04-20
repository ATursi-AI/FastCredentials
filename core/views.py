import feedparser
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import stripe
import os
import random
from .models import Course, Lesson, Question, Certificate, Payment, BlogPost
from .utils import generate_certificate_pdf
from .forms import CertificateSignupForm

stripe.api_key = settings.STRIPE_SECRET_KEY

# Stripe Product Price IDs
PRICE_SINGLE = 'price_1TAhi49D3Q7H7mowikZeC1NP'    # $19.99 Single Certificate
PRICE_ANNUAL = 'price_1TAhjt9D3Q7H7mowaMhbwXsv'    # $49.99 Annual All-Access Pass
PRICE_UPGRADE = 'price_1TAhl59D3Q7H7mowVt3hUrw3'   # $30.00 Upgrade to Annual

def fetch_regulatory_data():
    feeds = {
        'OSHA': 'https://www.federalregister.gov/api/v1/articles.rss?conditions%5Bagencies%5D%5B%5D=occupational-safety-and-health-administration',
        'CDC': 'https://www.federalregister.gov/api/v1/articles.rss?conditions%5Bagencies%5D%5B%5D=centers-for-disease-control-and-prevention'
    }
    results = []
    for source, url in feeds.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:3]:
                results.append({
                    'source': source,
                    'title': entry.title,
                    'link': entry.link,
                    'date': entry.published[:16]
                })
        except Exception:
            continue
    return results

def home(request):
    courses = Course.objects.all().order_by('-priority', 'title')
    for course in courses:
        t = course.title.upper()
        if any(x in t for x in ['FORKLIFT', 'ALCOHOL', 'FOOD']):
            course.badge_text, course.badge_color = '3-YEAR CERT', '#F59E0B'
        elif any(x in t for x in ['CPR', 'AED', 'FIRST AID', 'BLS']):
            course.badge_text, course.badge_color = '2-YEAR CERT', '#10B981'
        else:
            course.badge_text, course.badge_color = 'ANNUAL REQ', '#0C4A6E'

        if any(x in t for x in ['FORKLIFT', 'FOOD', 'ALCOHOL', 'FIRE', 'ELECTRICAL', 'LOCKOUT', 'TAGOUT', 'HAZARD', 'GHS', 'SLIPS', 'TRIPS', 'STANDARD CPR', 'STANDARD FIRST AID', 'BODY ART', 'TATTOO']):
            course.category = 'safety'
        elif any(x in t for x in ['BLS', 'HIPAA', 'ADVAMED', 'SUNSHINE', 'ASEPTIC', 'OPERATING', 'RADIATION', 'BLOOD']):
            course.category = 'medical'
        else:
            course.category = 'workplace'
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
        course.has_paid = request.user.is_superuser or request.user.groups.filter(name='FreeAccess').exists() or has_annual_pass or (course.id in paid_course_ids)
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
        if 'cert_name' in request.POST:
            if request.user.is_authenticated:
                # Save name to account permanently only if not already set
                # This prevents a user from changing their name after the first certificate
                if not request.user.first_name:
                    parts = request.POST.get('cert_name', '').strip().split(' ', 1)
                    request.user.first_name = parts[0]
                    request.user.last_name = parts[1] if len(parts) > 1 else ''
                    request.user.save()
                cert, _ = Certificate.objects.get_or_create(user=request.user, course=course)
                return redirect('certificate_view', cert_id=cert.cert_id)
            else:
                # Guest user — store name in session for preview
                request.session['guest_cert_name'] = request.POST.get('cert_name')
                return redirect('certificate_view', cert_id=f"PREVIEW-{course.id}")

        submitted_ids = [int(k.split('_')[1]) for k in request.POST.keys() if k.startswith('question_')]
        score = sum(1 for q in all_questions if q.id in submitted_ids and int(request.POST.get(f'question_{q.id}')) == q.correct_option)
        percentage = (score / len(submitted_ids)) * 100 if submitted_ids else 0

        if percentage >= 100:
            if request.user.is_authenticated:
                if request.user.first_name:
                    # Already has a name — create cert and go straight to certificate view
                    cert, _ = Certificate.objects.get_or_create(user=request.user, course=course)
                    return redirect('certificate_view', cert_id=cert.cert_id)
                else:
                    # No name yet — show name entry form before creating certificate
                    return render(request, 'quiz_result.html', {'course': course, 'passed': True, 'score': 100})
            # Guest user — store pass in session and show name entry form
            request.session[f'passed_course_{course.id}'] = True
            request.session['latest_passed_course'] = course.title
            return render(request, 'quiz_result.html', {'course': course, 'passed': True, 'score': 100})

        return render(request, 'quiz_result.html', {'course': course, 'passed': False, 'score': int(percentage)})

    random.shuffle(all_questions)
    questions_data = [{'question': q, 'options': sorted([(q.option_1,1),(q.option_2,2),(q.option_3,3),(q.option_4,4)], key=lambda x: random.random())} for q in all_questions[:10]]
    return render(request, 'take_quiz.html', {'course': course, 'questions_data': questions_data})

def certificate_view(request, cert_id):
    expire_date = timezone.now() + timedelta(days=365)
    if cert_id.startswith('PREVIEW-'):
        course_id = cert_id.split('-')[1]
        course = get_object_or_404(Course, pk=course_id)
        class MockUser:
            def __init__(self, first, last):
                self.first_name, self.last_name = first, last
                self.username, self.email = 'guest', 'guest@example.com'
                self.pk = self.id = None
                self.is_authenticated = self.is_staff = self.is_superuser = False
        class MockCertificate:
            def __init__(self, course, cert_id, user):
                self.course, self.cert_id, self.user = course, cert_id, user
                self.issued_at, self.pdf_file = timezone.now(), None
                self.pk = self.id = None
        full_name = request.session.get('guest_cert_name', 'Valued Candidate').split(' ', 1)
        first_name = full_name[0]
        last_name = full_name[1] if len(full_name) > 1 else ''
        cert = MockCertificate(course, cert_id, MockUser(first_name, last_name))
        return render(request, 'certificate_view.html', {'cert': cert, 'has_paid': False, 'expire_date': expire_date})

    cert = get_object_or_404(Certificate, cert_id=cert_id, user=request.user)
    one_year_ago = timezone.now() - timedelta(days=365)

    has_paid = request.user.is_superuser or \
               request.user.groups.filter(name='FreeAccess').exists() or \
               Payment.objects.filter(user=request.user, date__gte=one_year_ago, amount__gte=49.00).exists() or \
               Payment.objects.filter(user=request.user, course=cert.course, date__gte=one_year_ago).exists()
    
    if has_paid and not cert.pdf_file:
        cert.pdf_file = generate_certificate_pdf(cert)
        cert.save()
        return redirect('certificate_view', cert_id=cert_id)
    return render(request, 'certificate_view.html', {'cert': cert, 'has_paid': has_paid, 'expire_date': cert.issued_at + timedelta(days=365)})

def upsell(request, course_id):
    if not request.user.is_authenticated:
        return redirect(f"/signup/?next=/upsell/{course_id}/")
    course = get_object_or_404(Course, id=course_id)
    has_single_payment = Payment.objects.filter(user=request.user, amount=19.99).exists()
    upgrade_price = 30 if has_single_payment else None
    return render(request, 'upsell.html', {
        'course': course,
        'has_single_payment': has_single_payment,
        'upgrade_price': upgrade_price,
    })

@login_required
def create_checkout_session(request, course_id):
    plan_type = request.GET.get('plan', 'single')

    has_single_payment = Payment.objects.filter(user=request.user, amount=19.99).exists()

    if plan_type == 'upgrade' or (plan_type == 'annual' and has_single_payment):
        price_id = PRICE_UPGRADE
        price_amount = 3000
    elif plan_type == 'annual':
        price_id = PRICE_ANNUAL
        price_amount = 4900
    else:
        price_id = PRICE_SINGLE
        price_amount = 1999

    target_course_id = course_id if plan_type == 'single' else (Course.objects.first().id if Course.objects.exists() else 1)

    try:
        session = stripe.checkout.Session.create(
            customer_email=request.user.email,
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment',
            allow_promotion_codes=True,
            success_url=request.build_absolute_uri(reverse('payment_success')) + \
                        f'?session_id={{CHECKOUT_SESSION_ID}}&course_id={target_course_id}&amount={price_amount}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return render(request, 'dashboard.html', {'error': f"Stripe Error: {str(e)}"})

@login_required
def payment_success(request):
    session_id = request.GET.get('session_id')
    course_id = request.GET.get('course_id')
    amount_param = request.GET.get('amount')

    if not session_id or not course_id:
        return redirect('dashboard')

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except stripe.error.StripeError:
        return redirect('dashboard')

    # Handle both paid and free (coupon = 100% off) orders
    if session.payment_status in ('paid', 'no_payment_required'):
        course = get_object_or_404(Course, id=course_id)
        if not Payment.objects.filter(stripe_charge_id=session_id).exists():
            Payment.objects.create(
                user=request.user,
                course=course,
                stripe_charge_id=session_id,
                amount=float(amount_param) / 100.0 if amount_param else 19.99
            )

    return redirect('dashboard')

def payment_cancel(request): return redirect('dashboard')

def signup(request):
    url_plan = request.GET.get('plan')

    if request.user.is_authenticated:
        if url_plan:
            cid = 1
            last_cert = Certificate.objects.filter(user=request.user).last()
            if last_cert: cid = last_cert.course.id
            elif Course.objects.exists(): cid = Course.objects.first().id
            return redirect(reverse('create_checkout_session', kwargs={'course_id': cid}) + f'?plan={url_plan}')
        return redirect('dashboard')

    if url_plan:
        request.session['pending_plan'] = url_plan

    promo_message = f"CONGRATULATIONS! You Passed {request.session.get('latest_passed_course')}. Create account to view certificate." if request.session.get('latest_passed_course') else None

    if request.method == 'POST':
        form = CertificateSignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Name rescue — if guest entered name during quiz, save it to their account
            guest_name = request.session.get('guest_cert_name')
            if guest_name and not user.first_name:
                parts = guest_name.split(' ', 1)
                user.first_name = parts[0]
                user.last_name = parts[1] if len(parts) > 1 else ''
                user.save()

            login(request, user)

            redirect_course_id = None
            for c in Course.objects.all():
                if request.session.get(f'passed_course_{c.id}'):
                    Certificate.objects.get_or_create(user=user, course=c)
                    redirect_course_id = c.id
                    del request.session[f'passed_course_{c.id}']

            pending_plan = request.session.pop('pending_plan', None)

            if pending_plan:
                cid = redirect_course_id or (Course.objects.first().id if Course.objects.exists() else 1)
                return redirect(reverse('create_checkout_session', kwargs={'course_id': cid}) + f'?plan={pending_plan}')

            if redirect_course_id:
                cert = Certificate.objects.filter(user=user, course_id=redirect_course_id).first()
                if cert:
                    return redirect('certificate_view', cert_id=cert.cert_id)
                return redirect('upsell', course_id=redirect_course_id)

            return redirect('dashboard')

    return render(request, 'signup.html', {'form': CertificateSignupForm(), 'promo_message': promo_message})

def about(request): return render(request, 'about.html')
def support(request): return render(request, 'support.html')
def terms(request): return render(request, 'terms.html')
def ai_monitoring(request): return render(request, "ai.html", {"live_updates": fetch_regulatory_data()})

def verify_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, cert_id=cert_id)
    return render(request, 'verify_certificate.html', {'cert': cert})

def ai_transparency(request):
    return render(request, 'ai_transparency.html')

def blog_index(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog_index.html', {'posts': posts})

def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'blog_post.html', {'post': post})

def faq(request):
    """FAQ page with FAQPage schema for AI search optimization"""
    return render(request, 'faq.html')

def pricing(request):
    """Pricing page with Product schema for AI search optimization"""
    return render(request, 'pricing.html')