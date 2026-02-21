from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades BBP Body Art Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Bloodborne Pathogens (Body Art & Tattoo)')
            course.questions.all().delete()

            qs = [
                ('How long can Hepatitis B (HBV) survive in dried blood on a studio surface?', 
                 ['2 hours', '24 hours', '7 days', '30 days'], 3),
                
                ('What is the "3/4 Full Rule" for sharps containers in a tattoo studio?', 
                 ['Empty it once it is 75% full', 'Lock and replace it once it is 75% full', 'Only empty it when it is overflowing', 'It only applies to piercings'], 2),
                
                ('Which is an example of an "Engineering Control" in tattooing?', 
                 ['Washing hands', 'A needle cartridge with an internal safety membrane', 'Wearing a mask', 'Cleaning the station'], 2),
                
                ('Why is Nitrile preferred over Latex in the body art industry?', 
                 ['It is cheaper', 'It is immune to degradation from petroleum-based ointments (A&D/Vaseline)', 'It comes in more colors', 'It is thinner'], 2),
                
                ('What is "Dipper Contamination" in an ink bottle?', 
                 ['Ink leaking from the bottle', 'When a contaminated needle or tip touches the ink bottle, contaminating the whole supply', 'When ink dries out', 'A type of ink allergy'], 2),
                
                ('Where should a sharps container be located in a studio?', 
                 ['In the break room', 'Within arm\'s reach of the artist\'s workstation', 'In the sterilization room', 'Under the front desk'], 2),
                
                ('What is the "One-Handed Scoop" technique used for?', 
                 ['Eating lunch', 'Safely recapping a needle if medically necessary', 'Cleaning up a spill', 'Applying ointment'], 2),
                
                ('Why is vaping or drinking prohibited in the procedure area?', 
                 ['It is distracting', 'Aerosolized blood (splatter) can contaminate the mouthpiece/bottle, leading to hand-to-mouth transmission', 'It is unprofessional', 'It affects the ink'], 2),
                
                ('How often should a studio autoclave be "Spore Tested" (Biological Indicator)?', 
                 ['Once a year', 'Every month', 'At least weekly', 'Never'], 3),
                
                ('What is the "First 60 Seconds" protocol for an artist who sticks themselves?', 
                 ['Apply bleach to the wound', 'Wash the area immediately with soap and water', 'Finish the tattoo first', 'Squeeze the blood out as hard as possible'], 2),
                
                ('What is "Thermal Runaway" in the context of mobile tattoo carts?', 
                 ['The cart rolling away', 'A Lithium-Ion battery fire chain-reaction', 'The machine getting too hot to touch', 'A type of engine failure'], 2),
                
                ('What is the "Contact Time" for an EPA-registered disinfectant?', 
                 ['The time it takes to wipe the surface', 'The amount of time the surface must stay WET with the disinfectant to kill pathogens', 'The time it takes for the smell to go away', 'The time before the next client sits down'], 2),
                
                ('How should contaminated broken glass be picked up in a studio?', 
                 ['With gloved hands', 'With a brush and dustpan or tongs (mechanical means)', 'With a wet towel', 'It should be left for the cleaning crew'], 2),
                
                ('What is "Post-Exposure Prophylaxis" (PEP)?', 
                 ['A type of tattoo bandage', 'Anti-viral medication that must be started within 72 hours of an exposure', 'A cleaning agent for machines', 'A vaccine for Hepatitis C'], 2),
                
                ('What must an artist do if they touch a non-barrier surface (like their phone) during a procedure?', 
                 ['Wipe the phone with a towel', 'Immediately remove gloves, wash hands, and re-glove', 'Spray their gloves with alcohol', 'Nothing, if they are fast'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: BBP Body Art Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
