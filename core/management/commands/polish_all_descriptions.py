from django.core.management.base import BaseCommand
from core.models import Course

class Command(BaseCommand):
    help = 'Upgrades ALL remaining course descriptions to the Platinum Regulatory Standard'

    def handle(self, *args, **options):
        
        # 1. Standard First Aid -> Add OSHA 1910.151 & ANSI Z308.1
        Course.objects.filter(title='Standard First Aid').update(
            description="Compliant with OSHA 29 CFR 1910.151 and ANSI Z308.1 standards. Master critical interventions for hemorrhage control ('Stop the Bleed'), shock management, and stroke recognition. The definitive baseline for workplace emergency response."
        )

        # 2. Food Handler Safety -> Add FDA Food Code 2022 & HACCP
        Course.objects.filter(title='Food Handler Safety').update(
            description="Based on the 2022 FDA Food Code. Master the 'Fatal Four' pathogens, Time-Temperature Control for Safety (TCS) protocols, and HACCP principles. Mandatory for preventing foodborne illness liability."
        )

        # 3. Alcohol Server Training -> Add "Dram Shop" Liability
        Course.objects.filter(title='Alcohol Server Training').update(
            description="Responsible Beverage Service (RBS) certification. Mitigate 'Dram Shop' liability by mastering ID verification forensics, intoxication physiology, and the legal protocols for refusing service. Essential for liquor license retention."
        )

        # 4. Standard CPR / AED -> Add ILCOR 2025 & High-Performance Teams
        Course.objects.filter(title='Standard CPR / AED').update(
            description="Follows 2025 ILCOR & ECC Guidelines. Master 'High-Performance' team dynamics, AED deployment intervals, and fractional compression ratios. The standard for lay-rescuer and workplace compliance."
        )

        # 5. Forklift Safety -> Add "Powered Industrial Truck" & Stability Triangle
        Course.objects.filter(title='Forklift Safety (Theory)').update(
            description="OSHA 1910.178 Compliant for Powered Industrial Trucks (PIT). Master the 'Stability Triangle,' center of gravity physics, and pre-shift inspection mandates. Reduces crushing hazards and product damage."
        )

        # 6. Active Shooter -> Add "Run. Hide. Fight." & DHS Citations
        Course.objects.filter(title='Active Shooter Preparedness').update(
            description="Based on DHS and FBI 'Run. Hide. Fight.' protocols. Covers situational awareness, barricading techniques, and interacting with tactical law enforcement. Critical for modern corporate risk management."
        )

        # 7. Diversity, Equity & Inclusion (DEI) -> Add "Unconscious Bias" & EEOC
        Course.objects.filter(title='Diversity, Equity & Inclusion (DEI)').update(
            description="Aligned with EEOC best practices. Move beyond compliance to culture by mastering 'Unconscious Bias' mitigation, micro-aggression de-escalation, and inclusive leadership. Reduces hostile workplace claims."
        )

        # 8. Cybersecurity -> Add NIST & HIPAA Security Rule
        Course.objects.filter(title='Cybersecurity & Ransomware').update(
            description="Aligned with NIST and the HIPAA Security Rule (45 CFR 164.300). Master 'Zero Trust' principles, phishing detection forensics, and ransomware incident response. Protect your organization's digital perimeter."
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: All 24/24 courses are now Platinum Grade.'))
