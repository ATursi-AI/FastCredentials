from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Food Handler Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Food Handler Safety')
            course.questions.all().delete()

            qs = [
                ('Which pathogen is the leading cause of foodborne illness and spread by the fecal-oral route?', 
                 ['Salmonella', 'Norovirus', 'Listeria', 'E. coli'], 2),
                
                ('In 2026, what is the mandatory "Double Handwashing" protocol?', 
                 ['Wash once with soap, once with sanitizer', 'Wash in the restroom, then again at the kitchen handwashing station', 'Wash for 40 seconds', 'Wash with cold, then hot water'], 2),
                
                ('What is the difference between "Cross-Contamination" and "Cross-Contact"?', 
                 ['There is no difference', 'Contamination involves pathogens; Contact involves allergens', 'Contamination is for meat; Contact is for veggies', 'Contact is for managers only'], 2),
                
                ('What is the 2026 Temperature Danger Zone (TDZ) for TCS foods?', 
                 ['32°F to 100°F', '41°F to 135°F', '70°F to 120°F', '0°F to 40°F'], 2),
                
                ('What is the minimum internal temperature for Poultry and Reheated foods?', 
                 ['145°F', '155°F', '165°F', '135°F'], 3),
                
                ('How long must Shellstock Tags be kept on file after the last item is sold?', 
                 ['30 days', '90 days', '1 year', '7 days'], 2),
                
                ('Which thawing method is PROHIBITED for TCS foods?', 
                 ['In the refrigerator', 'Under running water at 70°F or lower', 'On the counter at room temperature', 'In the microwave if cooked immediately'], 3),
                
                ('What is the "Two-Stage Cooling" method total time limit?', 
                 ['2 hours', '4 hours', '6 hours', '12 hours'], 3),
                
                ('In vertical storage (top-to-bottom), where should raw poultry be placed?', 
                 ['On the top shelf', 'Middle shelf', 'The very bottom shelf', 'Next to the fruit'], 3),
                
                ('Which body fluid is NOT considered an infection risk unless it contains visible blood?', 
                 ['Saliva', 'Sweat', 'Vomitus', 'Cerebrospinal fluid'], 2),
                
                ('What is the 5th and final step of the Warewashing process?', 
                 ['Sanitizing', 'Towel-Drying', 'Air-Drying', 'Rinsing'], 3),
                
                ('What does an "Air Gap" prevent in a kitchen\'s plumbing system?', 
                 ['Leaky faucets', 'High water bills', 'Sewage backflow into the clean water supply', 'Air in the pipes'], 3),
                
                ('What is a "Critical Control Point" (CCP) in a HACCP plan?', 
                 ['A place to eat lunch', 'A point where a hazard can be prevented, eliminated, or reduced to safe levels', 'The front door of the restaurant', 'A type of thermometer'], 2),
                
                ('How often should food-contact surfaces in constant use be cleaned and sanitized?', 
                 ['Once a day', 'Every 4 hours', 'Every 8 hours', 'Only when they look dirty'], 2),
                
                ('What does the "A" stand for in the A.L.E.R.T. food defense system?', 
                 ['Alarm', 'Assure (know your sources)', 'Allergy', 'Accuracy'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Food Handler Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
