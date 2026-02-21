from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Updates course priorities to show High Value items first'

    def handle(self, *args, **options):
        # TIER 1: The "Big 3" Mandates (Priority 100)
        # These are the highest volume/revenue courses.
        tier_1 = [
            'Sexual Harassment Prevention',
            'HIPAA Patient Confidentiality',
            'Bloodborne Pathogens'
        ]

        # TIER 2: The New "Platinum" Industrial Suite (Priority 90)
        # We just built these; they are the highest quality content on the site.
        tier_2 = [
            'Hazard Communication (GHS)',
            'Lockout/Tagout (LOTO)',
            'Slips, Trips, and Falls',
            'Conflict Resolution & De-escalation',
            'Forklift Safety (Theory)'
        ]

        # TIER 3: Corporate Liability & Culture (Priority 80)
        # Essential for HR and Risk Management.
        tier_3 = [
            'Active Shooter Preparedness',
            'Diversity, Equity & Inclusion (DEI)',
            'Cybersecurity & Ransomware',
            'Fire Safety'
        ]

        # TIER 4: Clinical & Specialized (Priority 50)
        # Niche but critical.
        tier_4 = [
            'Healthcare BLS (Basic Life Support)',
            'Operating Room Protocols',
            'Aseptic Technique',
            'Radiation Safety',
            'The Sunshine Act',
            'AdvaMed Code of Ethics'
        ]

        # Reset all to 0 first (Standard Tier)
        Course.objects.all().update(priority=0)

        # Apply New Priorities
        for title in tier_1:
            Course.objects.filter(title=title).update(priority=100)
            
        for title in tier_2:
            Course.objects.filter(title=title).update(priority=90)

        for title in tier_3:
            Course.objects.filter(title=title).update(priority=80)

        for title in tier_4:
            Course.objects.filter(title=title).update(priority=50)

        self.stdout.write(self.style.SUCCESS('SUCCESS: Dashboard re-ranked. High Value courses are now at the top.'))
