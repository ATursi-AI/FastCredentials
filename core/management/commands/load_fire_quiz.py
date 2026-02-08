from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Randomizable Questions for Fire Safety (Safely)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Broader search to find "Fire And Electrical..."
        # We search for just "Fire" to ensure we catch the course title.
        courses = Course.objects.filter(title__icontains="Fire")
        
        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find any course with 'Fire' in the title."))
            self.stdout.write(self.style.WARNING("Here are the courses currently in your database:"))
            all_courses = Course.objects.all()
            for c in all_courses:
                self.stdout.write(f" - {c.title}")
            return

        # 2. SURGICAL DELETE: Remove ONLY questions attached to THIS course ID
        count = Question.objects.filter(course=course).count()
        self.stdout.write(f"Deleting {count} old questions for '{course.title}' only...")
        Question.objects.filter(course=course).delete()

        # 3. LOAD NEW QUESTIONS
        questions = [
            # SURGICAL FIRE TRIAD
            {
                "text": "A flash fire occurs on a patient's shoulder during surgery. The surgeon was using an electrosurgical pencil (Bovie). What was the likely 'Oxidizer' in this triad?",
                "o1": "The alcohol-based skin prep",
                "o2": "The surgical drapes",
                "o3": "Supplemental oxygen trapped under the drapes",
                "o4": "The electrosurgical pencil tip",
                "correct": 3
            },
            {
                "text": "Which of the following represents the 'Surgical Fire Triad'?",
                "o1": "Heat, Smoke, Fuel",
                "o2": "Oxidizer, Ignition Source, Fuel",
                "o3": "Oxygen, Nitrogen, Hydrogen",
                "o4": "Laser, Bovie, Drill",
                "correct": 2
            },
            {
                "text": "When a fiber-optic light cable is disconnected from the scope but left 'On', what is the safest place for the tip?",
                "o1": "Resting on the patient's drapes",
                "o2": "In a safety holster or held by a scrub tech (Standby Mode)",
                "o3": "On the instrument tray",
                "o4": "Draped over the patient's shoulder",
                "correct": 2
            },
            # PREVENTION
            {
                "text": "Why must alcohol-based skin preparations (like ChloraPrep) be allowed to dry for at least 3 minutes before draping?",
                "o1": "To ensure the bacteria are killed",
                "o2": "To allow flammable vapors to dissipate and prevent pooling",
                "o3": "To prevent staining the drapes",
                "o4": "To ensure the adhesive sticks better",
                "correct": 2
            },
            {
                "text": "What is 'Tenting,' and why is it a fire hazard?",
                "o1": "Using a tent to cover the sterile field",
                "o2": "Arranging drapes in a way that traps pockets of oxygen near the surgical site",
                "o3": "A method of storing gas cylinders",
                "o4": "The practice of covering equipment overnight",
                "correct": 2
            },
            # EMERGENCY RESPONSE
            {
                "text": "In the event of a fire in the facility, what does the acronym R.A.C.E. stand for?",
                "o1": "Run, Alert, Call, Escape",
                "o2": "Rescue, Alarm, Confine, Extinguish/Evacuate",
                "o3": "Report, Assess, Contain, Eliminate",
                "o4": "React, Ask, Call, Exit",
                "correct": 2
            },
            {
                "text": "You witness a small fire in a trash can. Using the P.A.S.S. technique with an extinguisher, what is the first step?",
                "o1": "Point at the fire",
                "o2": "Pull the pin",
                "o3": "Press the button",
                "o4": "Shake the canister",
                "correct": 2
            },
            {
                "text": "If a surgical fire occurs ON a patient (e.g., drapes catch fire), what is the immediate first action?",
                "o1": "Run to find a fire extinguisher",
                "o2": "Pull the fire alarm",
                "o3": "Remove the burning materials (drapes) from the patient immediately",
                "o4": "Pour saline on the floor",
                "correct": 3
            },
            # ELECTRICAL SAFETY
            {
                "text": "What is the primary difference between Macroshock and Microshock?",
                "o1": "Macroshock is AC power; Microshock is DC power.",
                "o2": "Macroshock causes burns; Microshock is invisible but can cause fatal heart arrhythmia via catheters.",
                "o3": "Macroshock is dangerous; Microshock is safe.",
                "o4": "There is no difference.",
                "correct": 2
            },
            {
                "text": "You notice a 3-prong plug on a piece of demo equipment has the round 'grounding pin' broken off. What should you do?",
                "o1": "Use it anyway; the other two prongs work fine.",
                "o2": "Use a 'cheater plug' (adapter) to fit it into the wall.",
                "o3": "Tag it 'Do Not Use' and remove it from service immediately.",
                "o4": "Tape it into the outlet so it stays tight.",
                "correct": 3
            },
            # ISOLATED POWER / LIM
            {
                "text": "A Line Isolation Monitor (LIM) alarm sounds in the Operating Room. What does this usually indicate?",
                "o1": "The power has gone out in the hospital.",
                "o2": "The system has become grounded (leakage current detected), and a single fault could now cause a shock.",
                "o3": "The backup generator is broken.",
                "o4": "There is a fire in the walls.",
                "correct": 2
            },
            {
                "text": "If the LIM alarm sounds immediately after you plug in a piece of equipment, what is the correct response?",
                "o1": "Ignore it; it's probably a false alarm.",
                "o2": "Unplug the device you just connected to see if the alarm stops.",
                "o3": "Call the fire department.",
                "o4": "Continue the surgery and check it later.",
                "correct": 2
            },
            # EQUIPMENT / LOTO
            {
                "text": "Which type of power strip is permitted for use in the 'Patient Care Vicinity' (within 6 feet of a patient)?",
                "o1": "Any power strip bought at a hardware store.",
                "o2": "Only Medical Grade strips meeting UL 1363A standards.",
                "o3": "Extension cords only.",
                "o4": "No power strips are ever allowed.",
                "correct": 2
            },
            {
                "text": "What is 'Daisy-Chaining,' and why is it prohibited?",
                "o1": "Connecting multiple medical devices to one patient.",
                "o2": "Plugging a power strip into another power strip or extension cord (Overheating risk).",
                "o3": "Using a chain to secure gas cylinders.",
                "o4": "Organizing cables with zip ties.",
                "correct": 2
            },
            {
                "text": "You see a machine with a Red Lock and a Tag on the power cord. What does this mean?",
                "o1": "The machine is reserved for a VIP patient.",
                "o2": "Lockout/Tagout (LOTO) is in effect; do not touch or plug in the machine.",
                "o3": "The machine is brand new.",
                "o4": "You can use it if you cut the lock off.",
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

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(questions)} randomized questions for {course.title}"))