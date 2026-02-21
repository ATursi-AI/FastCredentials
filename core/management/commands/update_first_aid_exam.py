from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades First Aid Exam to Match 2026 World-Class Depth'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Standard First Aid')
            course.questions.all().delete()

            qs = [
                ('In 2026 trauma protocols, what is the absolute #1 priority for a victim with a spurting limb wound?', 
                 ['Airway management', 'Checking for a pulse', 'Life-threatening bleeding control (Tourniquet)', 'Treating for shock'], 3),
                
                ('What is the clinical definition of "Implied Consent"?', 
                 ['The victim verbally says yes', 'The law assumes an unconscious or incapacitated person would want life-saving care', 'A bystander gives permission for the victim', 'The police authorize the treatment'], 2),
                
                ('Where should a windlass-style tourniquet be placed on a bleeding limb?', 
                 ['Directly over the wound', 'On the joint nearest to the wound', '2-3 inches above the wound (between wound and heart)', 'Below the wound to stop drainage'], 3),
                
                ('Why is maintaining body temperature (Passive Rewarming) critical for a victim in shock?', 
                 ['It makes them more comfortable', 'It prevents the "lethal triad" of trauma where metabolic failure causes heat loss', 'It stops the bleeding faster', 'It helps them sleep'], 2),
                
                ('What is the first step in treating a 2nd-degree thermal burn?', 
                 ['Apply antibiotic ointment', 'Pop the blisters to release pressure', 'Cool with running water for 10-20 minutes', 'Apply ice directly to the skin'], 3),
                
                ('In the 2026 "PEACE & LOVE" protocol, what does the "A" in PEACE stand for?', 
                 ['Always use ice', 'Avoid anti-inflammatory drugs (H.A.R.M.)', 'Apply heat immediately', 'Avoid moving the limb'], 2),
                
                ('Which of these is a "Red Flag" indicator of a severe traumatic brain injury (SCAT6)?', 
                 ['A mild headache', 'One pupil appearing larger than the other', 'Feeling slightly tired', 'Thirst'], 2),
                
                ('When using the F.A.S.T. mnemonic for stroke, what are you looking for in the "S" step?', 
                 ['Is the skin cool?', 'Is their speech slurred or strange?', 'Is their stomach painful?', 'Is their shoulder dislocated?'], 2),
                
                ('If a diabetic victim is confused but conscious, what is the safest course of action?', 
                 ['Give them an insulin injection', 'Provide 15-20g of fast-acting sugar', 'Give them a large meal', 'Ask them to lie down and sleep'], 2),
                
                ('What is the "Cool First, Transport Second" rule for Heat Stroke?', 
                 ['Wait for the ambulance before cooling', 'Aggressively cool the victim (ice bath/wet sheets) before they are moved to the hospital', 'Give them a cold drink while walking', 'Only cool them if they are sweating'], 2),
                
                ('Why should you NOT rub the limbs of a victim with severe hypothermia?', 
                 ['It might break the skin', 'It can cause "afterdrop," forcing cold blood back to the heart too quickly', 'It is too painful', 'It doesn\'t help with warming'], 2),
                
                ('What is the "Two-System" rule for recognizing Anaphylaxis?', 
                 ['Two people must confirm the reaction', 'Symptoms must be present in two or more body systems (e.g., skin and lungs)', 'The victim must have two Epi-Pens', 'The reaction must last two hours'], 2),
                
                ('Where is the correct injection site for an Epinephrine Auto-Injector (Epi-Pen)?', 
                 ['The upper arm (deltoid)', 'The stomach', 'The mid-outer thigh', 'The buttocks'], 3),
                
                ('What should you do if you are bitten by a venomous snake in North America?', 
                 ['Use a suction kit to remove venom', 'Apply a tight tourniquet', 'Stay calm, still, and keep the limb at/below heart level', 'Apply ice to the bite'], 3),
                
                ('What is the first step when removing a tick from the skin?', 
                 ['Use a match to burn it off', 'Apply petroleum jelly to suffocate it', 'Use fine-tipped tweezers to pull it straight up', 'Twist it until it lets go'], 3)
            ]

            for text, options, correct in qs:
                Question.objects.create(
                    course=course,
                    text=text,
                    option_1=options[0],
                    option_2=options[1],
                    option_3=options[2],
                    option_4=options[3],
                    correct_option=correct
                )

            self.stdout.write(self.style.SUCCESS('SUCCESS: First Aid Exam upgraded to World-Class Standards.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
