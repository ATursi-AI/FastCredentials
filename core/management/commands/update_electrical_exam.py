from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Electrical Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Electrical Safety')
            course.questions.all().delete()

            qs = [
                ('What is the primary factor that causes a fatal electrical shock to the heart?', 
                 ['High Voltage', 'High Resistance', 'Current (Amperage)', 'The color of the wire'], 3),
                
                ('What is the temperature of an Arc Flash capable of reaching?', 
                 ['1,000°F', '5,000°F', '35,000°F', '100,000°F'], 3),
                
                ('At what level of leakage current does a GFCI trip to protect a human life?', 
                 ['5mA', '50mA', '100mA', '15 Amps'], 1),
                
                ('What is the most critical step in a Lockout/Tagout (LOTO) procedure?', 
                 ['Putting on the tag', 'Telling the manager', 'Verification (the "Try" step) to ensure a Zero Energy State', 'Using a colored lock'], 3),
                
                ('What is the "Air Test" performed on rubber insulating gloves?', 
                 ['Checking the weight', 'Rolling the glove to trap air and check for microscopic punctures', 'Blowing into it with a machine', 'Testing it in a vacuum'], 2),
                
                ('Why is high-voltage DC in EV chargers specifically dangerous?', 
                 ['It is louder', 'It can cause "muscle tetany," making it impossible to let go of the circuit', 'It only works in the rain', 'It doesn\'t use a ground'], 2),
                
                ('What is "Daisy-Chaining" in electrical safety?', 
                 ['Using a specific type of wire', 'Plugging one power strip or extension cord into another', 'A method of grounding', 'Using a ladder near a power line'], 2),
                
                ('Which fire extinguisher should be used on an energized electrical fire (Class C)?', 
                 ['Water or Foam', 'ABC Dry Chemical or CO2', 'A bucket of sand', 'Only a Halon system'], 2),
                
                ('What does a "square-within-a-square" symbol on a power tool mean?', 
                 ['It is for heavy duty use', 'It is double-insulated and does not require a ground pin', 'It is a high-voltage tool', 'It is waterproof'], 2),
                
                ('Which ladder material is mandatory when working near electricity?', 
                 ['Aluminum', 'Steel', 'Fiberglass', 'Any clean ladder'], 3),
                
                ('What is the minimum clearance distance for unqualified persons from overhead power lines (up to 50kV)?', 
                 ['3 feet', '5 feet', '10 feet', '20 feet'], 3),
                
                ('If your vehicle hits a power line and catches fire, how should you exit?', 
                 ['Step out carefully while touching the metal', 'Jump clear with both feet together and "shuffle-step" away', 'Wait for the power company to arrive', 'Run as fast as possible'], 2),
                
                ('How should you help someone who is "frozen" to a live electrical circuit?', 
                 ['Grab them by the shoulders and pull', 'Use a non-conductive object (like a wooden broom or rescue hook) to push them away', 'Throw water on them to short the circuit', 'Kick them as hard as you can'], 2),
                
                ('Why must a shock victim receive an EKG even if they appear fine?', 
                 ['To check for broken bones', 'Because cardiac arrhythmias can manifest hours after an electrical shock', 'To check their blood pressure', 'It is only required for children'], 2),
                
                ('Who is considered a "Qualified Person" under OSHA electrical standards?', 
                 ['Anyone with a college degree', 'Anyone who has worked at the company for 10 years', 'Someone specifically trained on the construction, operation, and hazards of the specific equipment', 'Anyone who knows how to use a screwdriver'], 3)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Electrical Safety Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
