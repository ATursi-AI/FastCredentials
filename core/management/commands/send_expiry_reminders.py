from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from core.models import Certificate


def get_expiry_date(cert):
    """Mirror the exact tier logic from utils.py"""
    title = cert.course.title.upper()

    if any(x in title for x in ['FORKLIFT', 'ALCOHOL', 'FOOD']):
        return cert.issued_at + timedelta(days=1095)
    elif any(x in title for x in ['FIRST AID', 'CPR', 'AED', 'BLS', 'HEALTHCARE']):
        return cert.issued_at + timedelta(days=730)
    else:
        return cert.issued_at + timedelta(days=365)


class Command(BaseCommand):
    help = 'Send expiry reminder emails to users whose certificates expire in 30 days'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        reminder_window_start = now + timedelta(days=29)
        reminder_window_end = now + timedelta(days=31)

        certs = Certificate.objects.select_related('user', 'course').all()

        sent = 0
        for cert in certs:
            expiry = get_expiry_date(cert)
            if reminder_window_start <= expiry <= reminder_window_end:
                user = cert.user
                course = cert.course

                subject = f"Your {course.title} Certificate Expires in 30 Days"
                message = f"""Hi {user.first_name or user.username},

Your {course.title} certificate issued on {cert.issued_at.strftime('%B %d, %Y')} is due to expire on {expiry.strftime('%B %d, %Y')}.

To stay compliant, renew your certification now:
https://fastcredentials.com/course/{course.id}/

Your previous progress is saved — it only takes a few minutes to requalify.

The FastCredentials Team
https://fastcredentials.com
"""
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Reminder sent to {user.email} for '{course.title}' (expires {expiry.strftime('%Y-%m-%d')})"
                ))
                sent += 1

        self.stdout.write(self.style.SUCCESS(f"\nDone. {sent} reminder(s) sent."))