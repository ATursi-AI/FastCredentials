from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Re-indexes all 24 courses into the correct Medical, Compliance, or Safety tabs'

    def handle(self, *args, **options):
        # --- TAB 1: MEDICAL & HEALTHCARE ('medical') ---
        medical_courses = [
            'HIPAA Patient Confidentiality',
            'Healthcare BLS (Basic Life Support)',
            'Operating Room Protocols',
            'Aseptic Technique',
            'Radiation Safety',
            'AdvaMed Code of Ethics',
            'The Sunshine Act',
            'Bloodborne Pathogens',
            'Bloodborne Pathogens (Body Art & Tattoo)'
        ]

        # --- TAB 2: WORKPLACE COMPLIANCE ('workplace') ---
        compliance_courses = [
            'Sexual Harassment Prevention',
            'Diversity, Equity & Inclusion (DEI)',
            'Cybersecurity & Ransomware',
            'Conflict Resolution & De-escalation',
            'Active Shooter Preparedness'
        ]

        # --- TAB 3: SAFETY & TRADE ('safety') ---
        safety_courses = [
            'Fire Safety',
            'Electrical Safety',
            'Forklift Safety (Theory)',
            'Food Handler Safety',
            'Alcohol Server Training',
            'Hazard Communication (GHS)',
            'Lockout/Tagout (LOTO)',
            'Slips, Trips, and Falls',
            'Standard First Aid',
            'Standard CPR / AED'
        ]

        self.stdout.write(self.style.WARNING('Starting Re-Indexing...'))

        # Bulk Updates using the correct model keys
        
        for title in medical_courses:
            updated = Course.objects.filter(title=title).update(category='medical')
            if updated: self.stdout.write(f'  [Medical] {title}')

        for title in compliance_courses:
            updated = Course.objects.filter(title=title).update(category='workplace')
            if updated: self.stdout.write(f'  [Compliance] {title}')

        for title in safety_courses:
            updated = Course.objects.filter(title=title).update(category='safety')
            if updated: self.stdout.write(f'  [Safety] {title}')

        self.stdout.write(self.style.SUCCESS('\nSUCCESS: All 24 courses have been re-indexed to their correct tabs.'))
