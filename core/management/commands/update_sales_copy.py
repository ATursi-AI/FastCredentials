from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Updates course descriptions to be Best-in-Class Sales Copy'

    def handle(self, *args, **options):
        
        # 1. Conflict Resolution (Platinum Upgrade)
        Course.objects.filter(title='Conflict Resolution & De-escalation').update(
            description="Master clinical-grade de-escalation using the 'HEAT' method and 'Verbal Judo.' Covers the physiology of the 'Amygdala Hijack,' non-verbal 'Reactionary Gaps,' and recognizing Pre-Attack Indicators. Essential for healthcare and retail safety."
        )

        # 2. Hazard Communication GHS (Platinum Upgrade)
        Course.objects.filter(title='Hazard Communication (GHS)').update(
            description="Official OSHA 29 CFR 1910.1200 & GHS Rev 7 training. Master the 'Right to Understand,' 16-Section SDS interpretation, chemical incompatibility matrices, and spill containment ('Diking') protocols."
        )

        # 3. Lockout/Tagout LOTO (Platinum Upgrade)
        Course.objects.filter(title='Lockout/Tagout (LOTO)').update(
            description="OSHA 29 CFR 1910.147 Compliant. Master 'Zero Energy' verification, Group Lockout protocols, and the 'Fatal Five' causes of injury. distinguish between 'Authorized' and 'Affected' personnel responsibilities."
        )

        # 4. Slips, Trips, and Falls (Platinum Upgrade)
        Course.objects.filter(title='Slips, Trips, and Falls').update(
            description="Physics-based training on Tribology (friction science), ANSI A1264.1 stair geometry, and Fall Arrest Systems (PFAS). Reduces the #1 cause of general liability claims and lost workdays."
        )

        # 5. Electrical Safety (Polishing the existing short description)
        Course.objects.filter(title='Electrical Safety').update(
            description="Comprehensive training on NFPA 70E / OSHA Subpart S. Covers Arc Flash boundaries, Ground Fault Circuit Interrupters (GFCI), and safe work practices for high-voltage environments."
        )

        # 6. Bloodborne Pathogens (Tattoo) (Polishing the existing short description)
        Course.objects.filter(title='Bloodborne Pathogens (Body Art & Tattoo)').update(
            description="OSHA 29 CFR 1910.1030 compliant for the Body Art industry. Covers sterilization, cross-contamination, and specific exposure control plans for tattoo artists and piercers."
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: Best-in-Class Sales Copy injected for all Platinum courses.'))
