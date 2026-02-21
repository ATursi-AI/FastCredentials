from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Fixes typos and restores the Free Exam hook for consumer courses'

    def handle(self, *args, **options):
        
        # 1. Fix LOTO Typo (Capitalize "Distinguish")
        Course.objects.filter(title='Lockout/Tagout (LOTO)').update(
            description="OSHA 29 CFR 1910.147 Compliant. Master 'Zero Energy' verification, Group Lockout protocols, and the 'Fatal Five' causes of injury. Distinguish between 'Authorized' and 'Affected' personnel responsibilities."
        )

        # 2. Restore "Free" Hook to Standard CPR / AED
        Course.objects.filter(title='Standard CPR / AED').update(
            description="Follows 2025 ILCOR & ECC Guidelines. Master 'High-Performance' team dynamics, AED deployment intervals, and fractional compression ratios. The standard for lay-rescuers. Study guides and exam are 100% free."
        )

        # 3. Restore "Free" Hook to Standard First Aid
        Course.objects.filter(title='Standard First Aid').update(
            description="Compliant with OSHA 29 CFR 1910.151 and ANSI Z308.1. Master critical interventions for hemorrhage control ('Stop the Bleed'), shock management, and stroke recognition. Study guides and exam are 100% free."
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: Typos fixed. "Free Exam" hooks restored to CPR and First Aid.'))
