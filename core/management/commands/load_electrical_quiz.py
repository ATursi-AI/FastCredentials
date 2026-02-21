from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 10 General Industry Questions for Electrical Safety'

    def handle(self, *args, **kwargs):
        # 1. FIND THE COURSE
        try:
            course = Course.objects.get(title="Electrical Safety")
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}'"))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("Error: Course 'Electrical Safety' not found."))
            return

        # 2. CLEAR OLD QUESTIONS
        Question.objects.filter(course=course).delete()

        # 3. LOAD NEW QUESTIONS
        questions = [
            # BASICS
            {
                "text": "What is the primary factor in an electrical shock that causes injury or death?",
                "o1": "Voltage (Pressure)",
                "o2": "Current (Amps)",
                "o3": "Resistance (Ohms)",
                "o4": "Static Electricity",
                "correct": 2
            },
            {
                "text": "At approximately what current level does the 'Let-Go Threshold' occur, where you physically cannot let go of a wire?",
                "o1": "1 Amp",
                "o2": "10-20 Milliamps (mA)",
                "o3": "100 Volts",
                "o4": "5 Watts",
                "correct": 2
            },
            # CORDS & PLUGS
            {
                "text": "You find a 3-prong plug with the round grounding pin broken off. What should you do?",
                "o1": "Use it anyway.",
                "o2": "Tag it 'Do Not Use' and remove it from service.",
                "o3": "Use a 2-prong adapter.",
                "o4": "Bend the other prongs to make it fit.",
                "correct": 2
            },
            {
                "text": "Which of the following is TRUE regarding extension cords in the workplace?",
                "o1": "They can be used permanently if taped down.",
                "o2": "They are for temporary use only (e.g., 90 days or less).",
                "o3": "They can be run through walls or ceilings.",
                "o4": "They can be daisy-chained together to reach further.",
                "correct": 2
            },
            # POWER STRIPS
            {
                "text": "What is 'Daisy-Chaining'?",
                "o1": "Connecting multiple computers to one network.",
                "o2": "Plugging a power strip into another power strip (a fire hazard).",
                "o3": "Organizing cables with zip ties.",
                "o4": "A type of decorative lighting.",
                "correct": 2
            },
            {
                "text": "High-power devices like space heaters and microwaves should be plugged:",
                "o1": "Into a power strip.",
                "o2": "Directly into a wall outlet.",
                "o3": "Into an extension cord.",
                "o4": "Into a surge protector.",
                "correct": 2
            },
            # WATER / GFCI
            {
                "text": "What safety device is required in wet areas (kitchens, bathrooms) to shut off power instantly if a leak is detected?",
                "o1": "Surge Protector",
                "o2": "GFCI (Ground Fault Circuit Interrupter)",
                "o3": "Fuse Box",
                "o4": "Extension Cord",
                "correct": 2
            },
            # LOTO
            {
                "text": "If you see a machine with a Red Lock and a Tag on the power switch, what does it mean?",
                "o1": "The machine is broken and trash.",
                "o2": "Maintenance is working on it; do not touch or turn on.",
                "o3": "It is reserved for a manager.",
                "o4": "You can use it if you cut the lock off.",
                "correct": 2
            },
            # FIRES
            {
                "text": "What type of fire extinguisher is safe to use on an electrical (Class C) fire?",
                "o1": "Water Hose",
                "o2": "Class C (CO2 or Dry Chemical)",
                "o3": "A heavy blanket",
                "o4": "Soda",
                "correct": 2
            },
            # EMERGENCY
            {
                "text": "You see a coworker being shocked and they are unable to let go of the wire. What is your FIRST action?",
                "o1": "Grab their arm and pull them away.",
                "o2": "Cut the power (unplug or hit breaker) without touching them.",
                "o3": "Throw water on them.",
                "o4": "Call their name loudly.",
                "correct": 2
            }
        ]

        for q_data in questions:
            Question.objects.create(
                course=course,
                text=q_data['text'],
                option_1=q_data['o1'],
                option_2=q_data['o2'],
                option_3=q_data['o3'],
                option_4=q_data['o4'],
                correct_option=q_data['correct']
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(questions)} universal questions for {course.title}"))
