from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Aseptic Technique Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Aseptic Technique')
            course.questions.all().delete()

            qs = [
                ('What is the 2026 goal of Aseptic Technique?', 
                 ['To make the equipment look shiny', 'To achieve Asepsis—the state of being free from disease-causing contaminants', 'To save money on gloves', 'To speed up the procedure'], 2),
                
                ('What is the "ANTT®" framework in 2026?', 
                 ['A type of antibiotic', 'Aseptic Non-Touch Technique—focusing on protecting "Key Parts" and "Key Sites"', 'A manual for surgical instruments', 'A handwashing song'], 2),
                
                ('Why are Biofilms dangerous in 2026 healthcare?', 
                 ['They are colorful', 'They make bacteria up to 1,000x more resistant to antibiotics and disinfectants', 'They make the floor slippery', 'They only exist in older hospitals'], 2),
                
                ('What is the 2026 standard for skin-prep "Residual Kill Power"?', 
                 ['Soap and Water', '2% Chlorhexidine Gluconate (CHG) in 70% Alcohol', 'Warm Saline', 'Lemon juice'], 2),
                
                ('How wide is the "Non-Sterile" border on a sterile wrapper?', 
                 ['Half an inch', '1 inch', '2 inches', '3 inches'], 2),
                
                ('In Aseptic Technique, what is a "Key Part"?', 
                 ['The handle of the bed', 'Any component that, if contaminated, will directly infect the patient (e.g., needle tip)', 'The patient\'s chart', 'The trash can'], 2),
                
                ('What is the mandatory "Scrub the Hub" time for IV access in 2026?', 
                 ['2 seconds', '5 seconds', '15 seconds', '1 minute'], 3),
                
                ('Why is the vigorous "Back-and-Forth" scrub used for CHG antisepsis?', 
                 ['To move the bacteria around', 'To create mechanical friction that reaches the lower layers of the skin', 'To warm up the skin', 'It is faster than a circular motion'], 2),
                
                ('Where is the "Safe Zone" for gloved hands during an aseptic procedure?', 
                 ['Resting on the patient\'s bed', 'Between the waist and shoulders, within your field of vision', 'Behind your back', 'Hanging by your sides'], 2),
                
                ('What is "Strike-Through" contamination?', 
                 ['When a needle pokes through a glove', 'When moisture wicks bacteria through a sterile drape from a non-sterile surface', 'A type of surgical incision', 'When a patient coughs'], 2),
                
                ('How should you clean a wound according to 2026 aseptic standards?', 
                 ['From the dirtiest area to the cleanest', 'From the center (cleanest) outward to the surrounding skin', 'Only clean the edges', 'In a zigzag pattern'], 2),
                
                ('What is the risk of "Air-Shedding" during a procedure?', 
                 ['The air being too cold', 'The release of skin cells and dust from human movement that can contaminate the field', 'Oxygen tanks leaking', 'The room being too humid'], 2),
                
                ('In a 2-person urinary catheterization, what happens when a hand touches the patient?', 
                 ['The hand becomes extra sterile', 'The hand is now contaminated and must never return to the sterile field', 'The hand must be washed with alcohol immediately', 'Nothing happens'], 2),
                
                ('What should you do if you see a senior clinician break aseptic technique?', 
                 ['Nothing, they are the boss', 'Wait until after the procedure to tell them', 'Speak up immediately (Stop the Line) to correct the error', 'Report it to the news'], 3),
                
                ('What is the final step of every aseptic procedure?', 
                 ['Signing the chart', 'Removing the patient\'s ID band', 'Final hand hygiene', 'Taking a break'], 3)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Aseptic Technique Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
