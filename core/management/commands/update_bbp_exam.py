from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades BBP Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Bloodborne Pathogens')
            course.questions.all().delete()

            qs = [
                ('How often must an organization\'s Exposure Control Plan (ECP) be reviewed and updated?', 
                 ['Every 5 years', 'Once a year (annually)', 'Only when a breach occurs', 'Never'], 2),
                
                ('In 2026, clinical data confirms that Hepatitis B (HBV) can survive in dried blood on surfaces for at least:', 
                 ['2 hours', '24 hours', '7 days', '3 months'], 3),
                
                ('Which is an example of an "Engineering Control" for bloodborne pathogens?', 
                 ['Washing hands after glove removal', 'Using a self-retracting safety needle', 'Wearing a face shield', 'Not eating in the work area'], 2),
                
                ('What is the "3/4 Full Rule" regarding Sharps Containers?', 
                 ['You must empty it when it is 3/4 full', 'You must lock and replace it once it is 75% full', 'You should shake it to make more room', 'It is only a suggestion'], 2),
                
                ('Under "Standard Precautions," which body fluid is generally EXCLUDED (unless it contains visible blood)?', 
                 ['Saliva', 'Sweat', 'Cerebrospinal fluid', 'Vaginal secretions'], 2),
                
                ('Which is the PROPER technique for recapping a needle if it is medically necessary?', 
                 ['The two-handed "cap-push" technique', 'The one-handed "scoop" technique', 'Using a pair of pliers', 'Asking a coworker to hold the cap'], 2),
                
                ('When should you wash your hands with soap and water rather than using an alcohol-based rub?', 
                 ['After every patient', 'Only at the end of the day', 'When hands are visibly soiled with blood or OPIM', 'Never, alcohol is always better'], 3),
                
                ('What is the "First 60 Seconds" protocol for a contaminated needlestick?', 
                 ['Apply bleach to the wound', 'Squeeze the blood out as hard as possible', 'Immediately wash the area with soap and water', 'Wait for HR to give instructions'], 3),
                
                ('What is the "PEP Window" (Post-Exposure Prophylaxis) for HIV prevention?', 
                 ['Must be started within 24 hours', 'Must be started as soon as possible, and no later than 72 hours after exposure', 'Can be started up to one week later', 'There is no time limit'], 2),
                
                ('Which disinfectant is required for cleaning up a significant blood spill?', 
                 ['Warm soapy water', '1:100 diluted bleach', 'EPA-registered tuberculocidal agent or a fresh 1:10 bleach solution', 'Standard glass cleaner'], 3),
                
                ('What is the "Mechanical First" rule for blood spills?', 
                 ['Spray bleach directly on the pool of blood', 'Use absorbent material to soak up the bulk of the blood before applying disinfectant', 'Use a vacuum cleaner', 'Wipe it with a dry cloth only'], 2),
                
                ('When is an employer required to offer the Hepatitis B vaccination to a new at-risk employee?', 
                 ['After the 90-day probationary period', 'Within 10 days of initial assignment', 'Only if the employee asks', 'At the end of the first year'], 2),
                
                ('What color must the Biohazard symbol be according to OSHA?', 
                 ['Solid blue', 'Fluorescent orange or orange-red', 'Bright green', 'Yellow with black stripes'], 2),
                
                ('How long must an employer maintain your BBP Medical Records?', 
                 ['5 years', 'For the duration of employment', 'For the duration of employment plus 30 years', '10 years'], 3),
                
                ('Can an employer share your confidential exposure results with your manager?', 
                 ['Yes, for safety reasons', 'Only if you are fired', 'No, not without your specific written consent', 'Yes, if the manager asks'], 3)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: BBP Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
