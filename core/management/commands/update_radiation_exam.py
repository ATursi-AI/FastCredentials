from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Radiation Exam to 15 World-Class 2026 Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Radiation Safety')
            course.questions.all().delete()

            qs = [
                ('What does the "Inverse Square Law" mean for your safety?', 
                 ['Radiation increases with distance', 'Doubling your distance from the source reduces your exposure to 1/4th', 'Distance doesn\'t matter as long as you wear lead', 'You should stand as close as possible'], 2),
                
                ('What is the difference between Deterministic and Stochastic effects?', 
                 ['Deterministic are random; Stochastic have a threshold', 'Deterministic (like burns) have a threshold; Stochastic (like cancer) have no safe threshold', 'They are the same thing', 'Stochastic effects only happen to patients'], 2),
                
                ('What is the cornerstone principle of radiation safety in 2026?', 
                 ['ASAP', 'ALARA (As Low As Reasonably Achievable)', 'OSHA', 'NIST'], 2),
                
                ('Where is the highest intensity of "Scatter Radiation" found near a C-Arm?', 
                 ['On the side of the Image Intensifier (receiver)', 'On the side of the X-ray Tube (source)', 'Directly behind the surgeon', 'Under the floor'], 2),
                
                ('How often must lead aprons and thyroid shields undergo a fluoroscopic inspection?', 
                 ['Every 5 years', 'Once a year (annually)', 'Only when they look dirty', 'Every month'], 2),
                
                ('Where should a personal dosimeter be worn for the most accurate reading?', 
                 ['At the waist, under the apron', 'At the collar, outside of the lead apron', 'In your pocket', 'On your wrist'], 2),
                
                ('Why should you NEVER fold a lead apron?', 
                 ['It makes it look messy', 'It causes the internal lead lining to crease and crack, creating "hot spots"', 'It makes it too heavy', 'OSHA only allows rolling'], 2),
                
                ('In 2026, where should a "Declared Pregnant Worker" wear their second (fetal) dosimeter?', 
                 ['At the collar', 'At the waist, UNDERNEATH the lead apron', 'On her shoe', 'She should not wear one'], 2),
                
                ('What is the 2026 clinical shift regarding "Patient Gonadal Shielding"?', 
                 ['It is now mandatory for every exam', 'It is now selective because it can cause the machine to automatically increase the dose', 'We use gold instead of lead', 'Shields must be 5 inches thick'], 2),
                
                ('What is "Collimation" in radiation safety?', 
                 ['Taking the same X-ray twice', 'Narrowing the X-ray beam to only hit the area of interest', 'Cleaning the machine', 'A type of lead apron'], 2),
                
                ('Which part of the body is most at risk for radiation-induced cataracts?', 
                 ['The skin', 'The lens of the eye', 'The thyroid', 'The fingernails'], 2),
                
                ('What does the Magenta-on-Yellow "Trefoil" symbol signify?', 
                 ['Biohazard waste', 'Radiation Area / Ionizing Radiation', 'Electrical hazard', 'Wet floor'], 2),
                
                ('How should you handle a "Stuck Shutter" emergency where the X-ray won\'t turn off?', 
                 ['Try to kick the pedal harder', 'Push the Emergency Stop (E-Stop) or unplug the machine immediately', 'Wait for the patient to move', 'Call the manager while the beam is on'], 2),
                
                ('What is the "Three Pillars of Protection" in radiation safety?', 
                 ['Lead, Steel, and Concrete', 'Time, Distance, and Shielding', 'Gloves, Goggles, and Aprons', 'Training, Testing, and Tracking'], 2),
                
                ('A patient with implanted radioactive "seeds" for cancer treatment:', 
                 ['Is not a radiation risk', 'Requires a "Chain of Custody" and provides a potential exposure risk to staff', 'Should be handled with bare hands', 'Is only radioactive in the dark'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Radiation Safety Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
