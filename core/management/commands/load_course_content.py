from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Restores videos using the exact format from our successful bunny test'

    def handle(self, *args, **kwargs):
        # Restore Bloodborne Pathogens
        bbp = Course.objects.get(title="Bloodborne Pathogens")
        Lesson.objects.filter(course=bbp).delete()
        
        # We are using the simplest URL structure so the models.py regex works perfectly
        Lesson.objects.create(
            course=bbp,
            title="Introduction to OSHA 29 CFR 1910.1030",
            content="<p>Treat all blood and OPIM as if known to be infectious.</p>",
            video_url="https://youtu.be/S2z835P28j8",
            order=1
        )

        # Restore Fire & Electrical
        fire = Course.objects.get(title__contains="Fire & Electrical")
        Lesson.objects.filter(course=fire).delete()
        
        Lesson.objects.create(
            course=fire,
            title="The Surgical Fire Triad",
            content="<p>Oxidizer, Ignition Source, and Fuel.</p>",
            video_url="https://youtu.be/17uwTLEHTPM",
            order=1
        )
        self.stdout.write(self.style.SUCCESS('Content restored with verified short-link format.'))