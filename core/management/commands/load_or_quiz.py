from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for OR Protocols (Appends Only - No Deletes)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the OR Protocols Course
        # We search for "Operating Room" or "OR Protocols"
        courses = Course.objects.filter(title__icontains="Operating Room")
        
        if not courses.exists():
            # Fallback search in case you named it "OR Protocols"
            courses = Course.objects.filter(title__icontains="OR Protocol")

        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'Operating Room' or 'OR Protocol' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion)
        # 15 Questions covering the 10 Modules
        
        questions = [
            # ZONES & ATTIRE
            {
                "text": "In which zone of the Operating Room are street clothes permitted?",
                "o1": "The Semi-Restricted Area (Corridors)",
                "o2": "The Restricted Area (OR Suite)",
                "o3": "The Unrestricted Area (Locker Room/Front Desk)",
                "o4": "Anywhere, if you are a vendor.",
                "correct": 3
            },
            {
                "text": "What is the requirement for head coverings in the Semi-Restricted and Restricted areas?",
                "o1": "Only the top of the head needs to be covered.",
                "o2": "All hair, including sideburns and the nape of the neck, AND ears must be covered.",
                "o3": "Hats are optional if you have short hair.",
                "o4": "Personal cloth caps are always preferred over disposables.",
                "correct": 2
            },
            {
                "text": "Why must warm-up jackets be snapped closed in the Restricted Area?",
                "o1": "To look more professional.",
                "o2": "To prevent air turbulence and the shedding of skin squames onto the sterile field.",
                "o3": "To keep the vendor warm.",
                "o4": "To hide your badge.",
                "correct": 2
            },
            # HYGIENE & DEVICES
            {
                "text": "According to AORN guidelines, what should you do with your cell phone before entering the Restricted Area?",
                "o1": "Put it in silent mode only.",
                "o2": "Wipe it down with a hospital-grade disinfectant.",
                "o3": "Leave it in the car.",
                "o4": "Hide it in your pocket.",
                "correct": 2
            },
            {
                "text": "Is it permissible to take a photograph of your instrument tray if a patient is in the room?",
                "o1": "Yes, if the patient's face is not visible.",
                "o2": "Yes, if the surgeon says it's okay.",
                "o3": "No. Photography requires explicit written consent and is generally strictly prohibited.",
                "o4": "Only if you post it to a private group.",
                "correct": 3
            },
            # VENDOR ROLE
            {
                "text": "If a surgeon asks you to 'hold this retractor' while they tie a suture, what is the correct response?",
                "o1": "Grab the retractor immediately to help.",
                "o2": "Politely decline, stating you are not scrubbed or credentialed to touch the patient.",
                "o3": "Ask the nurse for permission first.",
                "o4": "Put on sterile gloves and then help.",
                "correct": 2
            },
            {
                "text": "As a vendor, your primary role in the OR is:",
                "o1": "To assist with surgery.",
                "o2": "To provide technical expertise on the specific mechanics and assembly of your device.",
                "o3": "To train the residents on anatomy.",
                "o4": "To manage the music volume.",
                "correct": 2
            },
            # TIME OUT & ENVIRONMENT
            {
                "text": "During the 'Time Out' before incision, what should the vendor do?",
                "o1": "Continue setting up the back table.",
                "o2": "Stop all activity, be silent, and listen. Speak up ONLY if there is a discrepancy with your equipment.",
                "o3": "Check emails.",
                "o4": "Leave the room.",
                "correct": 2
            },
            {
                "text": "The Operating Room is maintained at 'Positive Pressure.' What does this mean?",
                "o1": "Air pushes OUT of the room into the hall to keep germs out.",
                "o2": "Air is sucked INTO the room from the hall.",
                "o3": "The room is pressurized like an airplane.",
                "o4": "The temperature is higher than the hallway.",
                "correct": 1
            },
            # FIELD AWARENESS
            {
                "text": "What is the '12-Inch Rule' regarding sterile fields?",
                "o1": "Sterile tables must be 12 inches high.",
                "o2": "Unsterile personnel must maintain a distance of at least 12 inches from any sterile field.",
                "o3": "Implants must be opened from 12 inches away.",
                "o4": "You must speak 12 inches from the surgeon's ear.",
                "correct": 2
            },
            {
                "text": "If you need to identify an instrument on the sterile back table, you should:",
                "o1": "Reach over and point to it.",
                "o2": "Touch it with a pen.",
                "o3": "Use a laser pointer or describe it verbally; never reach over a sterile field.",
                "o4": "Ask the surgeon to get it.",
                "correct": 3
            },
            {
                "text": "The color Blue (or Green) in an OR typically signifies:",
                "o1": "Trash.",
                "o2": "Sterile areas (drapes, gowns, table covers).",
                "o3": "Biohazard.",
                "o4": "Unrestricted zones.",
                "correct": 2
            },
            # ETIQUETTE & WASTE
            {
                "text": "When is 'social conversation' (sports, weekend plans) considered inappropriate in the OR?",
                "o1": "Always.",
                "o2": "Only during closing.",
                "o3": "During 'Critical Phases' such as induction, incision, counts, and emergence.",
                "o4": "Only if the patient is awake.",
                "correct": 3
            },
            {
                "text": "Where should a vendor's hospital ID badge be worn while in the OR?",
                "o1": "On a lanyard around the neck.",
                "o2": "Clipped or adhered to the upper chest/shoulder area (no lanyards).",
                "o3": "On the belt/pants.",
                "o4": "In a pocket.",
                "correct": 2
            },
            {
                "text": "Why are cardboard shipping boxes generally prohibited in the Restricted Area (OR rooms)?",
                "o1": "They are too heavy.",
                "o2": "They shed dust and can harbor insect eggs/larvae.",
                "o3": "They are a fire hazard.",
                "o4": "They are hard to recycle.",
                "correct": 2
            }
        ]

        self.stdout.write(f"Adding {len(questions)} new questions to '{course.title}'...")
        
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

        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(questions)} questions!"))