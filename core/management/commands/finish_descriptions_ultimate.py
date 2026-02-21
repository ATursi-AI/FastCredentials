from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Finalizes AdvaMed, BLS, and OR Protocols to Platinum Regulatory Standard'

    def handle(self, *args, **options):
        
        # 1. AdvaMed Code of Ethics -> The "Anti-Kickback" Upgrade
        Course.objects.filter(title='AdvaMed Code of Ethics').update(
            description="Master the AdvaMed Code on Interactions with Health Care Professionals. Covers 'Anti-Kickback Statute' implications, 'Safe Harbor' provisions for consulting, and strict prohibitions on entertainment. Essential for MedTech sales."
        )

        # 2. Healthcare BLS -> The "AHA Guidelines" Upgrade
        Course.objects.filter(title='Healthcare BLS (Basic Life Support)').update(
            description="Aligned with 2025 AHA Guidelines for CPR and ECC. Master 'High-Performance' team dynamics, advanced airway management, and 2-rescuer protocols. Mandatory for clinical providers and hospital credentialing."
        )

        # 3. Operating Room Protocols -> The "AORN" Upgrade
        Course.objects.filter(title='Operating Room Protocols').update(
            description="Aligned with AORN Standards for Perioperative Practice. Master the 'Red Line' strict sterile zones, surgical hand antisepsis, and traffic patterns. Required for vendor access to the O.R."
        )

        # 4. The Sunshine Act -> The "Open Payments" Upgrade
        Course.objects.filter(title='The Sunshine Act').update(
            description="Federal compliance for the Physician Payments Sunshine Act (42 C.F.R. § 403.900). Master 'Open Payments' reporting thresholds, 'Transfer of Value' categories, and dispute resolution. Protects against CMS penalties."
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: AdvaMed, BLS, OR, and Sunshine Act are now Platinum Grade.'))
