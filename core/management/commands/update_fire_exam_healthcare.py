from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Fire Safety Exam to 15 World-Class Healthcare Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Fire Safety')
            course.questions.all().delete()

            qs = [
                ('What is the "Defend-in-Place" strategy in healthcare?', 
                 ['Running out of the building immediately', 'Containing fire in its compartment of origin and moving patients horizontally', 'Using only one fire extinguisher', 'Waiting for the police to arrive'], 2),
                
                ('What three elements make up the "Surgical Fire Triad"?', 
                 ['Water, Smoke, Heat', 'Ignition Source, Fuel Source, and Oxidizer', 'Oxygen, Nitrogen, and Carbon', 'Electricity, Gas, and Fire'], 2),
                
                ('Why is the R.A.C.E. acronym used in healthcare?', 
                 ['To win a fire drill contest', 'To provide a structured response (Rescue, Alarm, Confine, Extinguish)', 'To identify the shooter', 'To report a chemical spill'], 2),
                
                ('What is the primary function of a Line Isolation Monitor (LIM) in the O.R.?', 
                 ['To monitor the patient\'s heart rate', 'To monitor the integrity of the isolated power system and warn of a "first fault"', 'To turn off the lights automatically', 'To signal the start of surgery'], 2),
                
                ('When a LIM alarm sounds, what should the surgical team do first?', 
                 ['Scream and run', 'Identify and unplug the most recently added piece of equipment', 'Ignore the alarm if the patient is stable', 'Call the fire department immediately'], 2),
                
                ('Which power strip standard is mandatory for the "Patient Care Vicinity" (within 6 feet of a bed)?', 
                 ['Standard hardware store strip', 'UL 1363A or UL 60601-1', 'Any strip with a fuse', 'Power strips are prohibited'], 2),
                
                ('What is "Thermal Runaway" in a Lithium-Ion battery?', 
                 ['A battery that runs out of power', 'A chain reaction that causes uncontrollable heating, toxic gas release, and self-ignition', 'A battery that is too cold to work', 'A type of fast-charging'], 2),
                
                ('In 2026, why is "Daisy-Chaining" power strips a fire hazard?', 
                 ['It uses too much electricity', 'It overloads circuits and causes dangerous heat buildup in the cords', 'It makes the cords too long', 'It is only a hazard in California'], 2),
                
                ('What does a "Green Dot" on an electrical plug signify?', 
                 ['It is eco-friendly', 'It is a Hospital Grade/Medical Grade plug with extra grounding protection', 'It is used for oxygen only', 'It is a recycled plug'], 2),
                
                ('Why is Oxygen considered a fire hazard if it doesn\'t "burn"?', 
                 ['It is a liquid', 'It is an oxidizer that makes materials ignite easier and burn much hotter', 'It causes smoke to be more toxic', 'It is not a fire hazard'], 2),
                
                ('Where should medical gas cylinders be stored according to NFPA 99?', 
                 ['Lying flat on the floor', 'Upright, secured with chains/racks, and in a ventilated room', 'In the patient room at all times', 'Near the emergency exit'], 2),
                
                ('What is the "Verification" step in a Lockout/Tagout (LOTO) procedure?', 
                 ['Checking the paperwork', 'Attempting to start the machine (the "Try" step) to ensure no energy remains', 'Asking the manager if it\'s safe', 'Writing the time on the tag'], 2),
                
                ('When using the P.A.S.S. method, where should you aim the extinguisher?', 
                 ['At the top of the flames', 'At the base of the fire', 'At the smoke', 'In a circle around the fire'], 2),
                
                ('Why are extension cords prohibited for permanent use in healthcare?', 
                 ['They are too expensive', 'They are prone to physical damage and can lead to arcing and fires', 'They are not long enough', 'They only work for 24 hours'], 2),
                
                ('What is a "Smoke Compartment" designed to do?', 
                 ['Let smoke out through the roof', 'Isolate smoke and fire for at least 2 hours to allow for horizontal evacuation', 'Keep the building warm', 'Detect fires early'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Healthcare Fire Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
