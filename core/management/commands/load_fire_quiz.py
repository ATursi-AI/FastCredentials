from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 10 High-Quality Randomized Questions for Fire Safety (NFPA 101)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP
        try:
            course = Course.objects.get(title="Fire Safety")
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("Error: Could not find course 'Fire Safety'."))
            return

        # 2. SURGICAL DELETE
        count = Question.objects.filter(course=course).count()
        self.stdout.write(f"Deleting {count} old questions for '{course.title}'...")
        Question.objects.filter(course=course).delete()

        # 3. LOAD NEW QUESTIONS (10 Total)
        questions = [
            # --- SURGICAL FIRE TRIAD (3 Questions) ---
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
            # --- PREVENTION (2 Questions) ---
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
            # --- EMERGENCY RESPONSE / R.A.C.E / P.A.S.S (3 Questions) ---
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
            # --- NFPA 101 LIFE SAFETY CODE (2 NEW QUESTIONS) ---
            {
                "text": "According to NFPA 101, what is 'Horizontal Evacuation' in a healthcare setting?",
                "o1": "Moving patients down the stairs immediately.",
                "o2": "Moving patients laterally through a smoke barrier door into an adjacent safe smoke compartment.",
                "o3": "Taking patients to the roof.",
                "o4": "Evacuating only ambulatory patients first.",
                "correct": 2
            },
            {
                "text": "Who is typically authorized to shut off the Medical Gas (Oxygen) zone valves during a fire emergency?",
                "o1": "Any staff member who smells smoke.",
                "o2": "Only the Charge Nurse, Respiratory Therapist, or Fire Marshal (typically upon order).",
                "o3": "Only the hospital CEO.",
                "o4": "The security guard.",
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
