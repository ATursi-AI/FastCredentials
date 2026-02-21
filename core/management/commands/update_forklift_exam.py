from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Forklift Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Forklift Safety (Theory)')
            course.questions.all().delete()

            qs = [
                ('What is the "Stability Triangle" on a forklift?', 
                 ['A triangle painted on the floor', 'The three-point suspension system formed by the front wheels and the rear axle pivot', 'A type of safety cone', 'The shape of the steering wheel'], 2),
                
                ('What is the front wheel of a forklift considered in the "Fulcrum Principle"?', 
                 ['The load center', 'The pivot point (fulcrum)', 'The stabilizer', 'The steering point'], 2),
                
                ('How high should the forks be kept from the floor when traveling?', 
                 ['12 to 18 inches', '4 to 6 inches', 'As high as possible for visibility', 'Dragging on the floor'], 2),
                
                ('If a load blocks your forward view, what must you do according to OSHA?', 
                 ['Drive faster to get it over with', 'Travel in reverse', 'Stand up to see over the load', 'Have a coworker walk in front of you'], 2),
                
                ('Why is turning the forklift while a load is elevated dangerous?', 
                 ['It uses too much fuel', 'Centrifugal force will pull the Center of Gravity outside the Stability Triangle, causing a tip-over', 'It wears out the tires', 'It is only allowed in reverse'], 2),
                
                ('What should you do if a forklift has a safety-critical defect like a hydraulic leak?', 
                 ['Finish your shift first', 'Report it to the next driver', 'Red Tag it and remove it from service immediately', 'Try to fix it yourself'], 3),
                
                ('What is the risk of "Thermal Runaway" in 2026 Lithium-Ion batteries?', 
                 ['The battery won\'t charge', 'A chain reaction that causes uncontrollable heat, toxic gas, and self-ignition', 'The truck becomes too fast', 'The battery freezes'], 2),
                
                ('When traveling with a LOAD on a ramp, which way should the load face?', 
                 ['Always face down-grade', 'Always face up-grade (drive up, reverse down)', 'It doesn\'t matter', 'Only face up-grade when reversing'], 2),
                
                ('What is the purpose of the "Blue Spotlight" projected on the floor?', 
                 ['To light the path for the driver', 'To provide a visual warning to pedestrians before a forklift enters an intersection', 'To show the battery level', 'To mark the load center'], 2),
                
                ('What happens to a forklift\'s capacity when you add an attachment?', 
                 ['It increases', 'It stays the same', 'It decreases due to the weight of the attachment and the shift in load center', 'It only changes if the attachment is heavy'], 3),
                
                ('What is "Trailer Creep" at a loading dock?', 
                 ['A slow-moving forklift', 'The trailer slowly moving away from the dock due to the movement of the forklift', 'When the trailer floor breaks', 'A type of tire wear'], 2),
                
                ('Why is a "Nose Jack" required for un-coupled trailers?', 
                 ['To lift the trailer higher', 'To prevent the trailer from tipping forward (nose-diving) when a forklift enters', 'To change the tires', 'To lock the brakes'], 2),
                
                ('What is the survival protocol if a forklift begins to tip over?', 
                 ['Jump clear as fast as possible', 'Stay in the seat, grip the wheel, brace your feet, and lean AWAY from the fall', 'Try to push the forklift back up', 'Crouch on the floor of the cab'], 2),
                
                ('When should a pre-operational inspection be performed?', 
                 ['Once a week', 'At least daily, or at the beginning of every shift', 'Only if the truck feels "off"', 'Every 100 hours of use'], 2),
                
                ('What does a "Red Zone" LED light project around a forklift?', 
                 ['A path to the exit', 'The "Danger Zone" boundary where the rear-end swing occurs', 'The area for the charger', 'A high-speed lane'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Forklift Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
