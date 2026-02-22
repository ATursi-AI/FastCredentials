from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # FLOW
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('quiz/<int:course_id>/', views.take_quiz, name='take_quiz'),
    
    # PRIVATE: User viewing their own cert (Requires Login)
    path('certificate/<str:cert_id>/', views.certificate_view, name='certificate_view'),

    # PUBLIC: QR Code Destination (No Login Required)
    path('verify/<str:cert_id>/', views.verify_certificate, name='verify_certificate'),
    
    # STRIPE
    # STRIPE
path('upsell/<int:course_id>/', views.upsell, name='upsell'),
path('checkout/<int:course_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    
    # AUTH
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
    path('terms/', views.terms, name='terms'),
    
    # AI MONITORING
    path('powered-by-ai/', views.ai_monitoring, name='ai_monitoring'),
    path('ai-transparency/', views.ai_transparency, name='ai_transparency'),
]
