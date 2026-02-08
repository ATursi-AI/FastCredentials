from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for Aseptic Technique (Appends Only - No Deletes)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the Course
        # We search for "Aseptic" (correct spelling)
        courses = Course.objects.filter(title__icontains="Aseptic")
        
        if not courses.exists():
            # Fallback in case it was saved with the typo "Asceptic"
            courses = Course.objects.filter(title__icontains="Asceptic")

        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'Aseptic' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion)
        
        questions = [
            # FOUNDATIONS & STERILE FIELD
            {
                "text": "In the context of the Operating Room, what is the difference between 'Clean' and 'Sterile'?",
                "o1": "They mean the same thing.",
                "o2": "Clean reduces pathogens; Sterile eliminates ALL microbial life, including spores.",
                "o3": "Clean is for surgery; Sterile is for the hallway.",
                "o4": "Sterile means washed with soap.",
                "correct": 2
            },
            {
                "text": "What color are sterile drapes and gowns typically in Western hospitals?",
                "o1": "Red or Orange",
                "o2": "Blue or Green",
                "o3": "Yellow",
                "o4": "Black",
                "correct": 2
            },
            {
                "text": "Which part of a sterile draped table is considered sterile?",
                "o1": "The top, sides, and legs.",
                "o2": "Only the top surface (tabletop level).",
                "o3": "Everything except the wheels.",
                "o4": "Only the center.",
                "correct": 2
            },
            # SURGICAL CONSCIENCE & GOWNING
            {
                "text": "What is 'Surgical Conscience'?",
                "o1": "The fear of getting sued.",
                "o2": "The ethical duty to admit and report any break in sterility immediately, even if no one saw it.",
                "o3": "Knowing the names of the instruments.",
                "o4": "Memorizing the surgeon's preferences.",
                "correct": 2
            },
            {
                "text": "Which parts of a surgical gown are considered sterile (The 'Box')?",
                "o1": "The entire gown from neck to feet.",
                "o2": "The front from Chest to Waist, and sleeves from 2 inches above elbow to cuff.",
                "o3": "The back and the front.",
                "o4": "Only the sleeves.",
                "correct": 2
            },
            {
                "text": "Is the back of a sterile gown considered sterile?",
                "o1": "Yes, if it wraps around.",
                "o2": "No, the back is never considered sterile.",
                "o3": "Yes, but only for the surgeon.",
                "o4": "Only if a nurse tied it.",
                "correct": 2
            },
            # OPENING ITEMS & PACKAGING
            {
                "text": "What is the correct technique for opening a 'Peel Pack'?",
                "o1": "Tear the paper quickly to get it open.",
                "o2": "Peel the layers apart smoothly/evenly to prevent releasing airborne lint.",
                "o3": "Poke the item through the paper.",
                "o4": "Use scissors to cut the middle.",
                "correct": 2
            },
            {
                "text": "Before opening a wrapped instrument tray, what is the first thing you must check?",
                "o1": "The weight of the tray.",
                "o2": "The integrity of the wrap (looking for holes, tears, or water stains).",
                "o3": "The brand name.",
                "o4": "The color of the handle.",
                "correct": 2
            },
            {
                "text": "If the internal chemical indicator (dot/strip) inside a package has NOT changed color, what must you do?",
                "o1": "Use it anyway; it's probably fine.",
                "o2": "Consider the item unsterile and discard/return it.",
                "o3": "Ask the surgeon if they want to risk it.",
                "o4": "Wipe it with alcohol.",
                "correct": 2
            },
            # EVENT RELATED & STRIKE-THROUGH
            {
                "text": "What is 'Strike-Through' contamination?",
                "o1": "When a surgeon strikes the patient.",
                "o2": "When moisture soaks through a sterile barrier, wicking bacteria from the unsterile surface below.",
                "o3": "When an instrument falls on the floor.",
                "o4": "When a light bulb burns out.",
                "correct": 2
            },
            {
                "text": "Under 'Event-Related Sterility' rules, what happens if a sterile peel-pack falls on the floor?",
                "o1": "It is safe if you pick it up within 5 seconds.",
                "o2": "It is generally considered contaminated due to the 'bellows effect' (forcing air/dust inside).",
                "o3": "It is fine as long as it didn't land in water.",
                "o4": "You should wipe the outside and use it.",
                "correct": 2
            },
            {
                "text": "If a wrapped instrument tray comes out of the autoclave with visible moisture on the wrap ('Wet Pack'), is it sterile?",
                "o1": "Yes, water is sterile.",
                "o2": "No. Moisture creates a pathway for bacteria; it is contaminated.",
                "o3": "Yes, if you let it dry.",
                "o4": "Only if it is warm.",
                "correct": 2
            },
            # MOVEMENT & FIELD AWARENESS
            {
                "text": "When moving around a sterile field as an unscrubbed vendor, you should:",
                "o1": "Walk backwards to protect your back.",
                "o2": "Always face the sterile field to ensure you do not brush against it.",
                "o3": "Squeeze between the back table and the wall.",
                "o4": "Walk as fast as possible.",
                "correct": 2
            },
            {
                "text": "Can you walk between two sterile fields (e.g., between the Back Table and the Mayo Stand)?",
                "o1": "Yes, if you are skinny enough.",
                "o2": "No. That space is restricted; you must walk around the perimeter.",
                "o3": "Yes, if you hold your breath.",
                "o4": "Only if the nurse says so.",
                "correct": 2
            },
            {
                "text": "If you witness a contamination event (e.g., a rep brushes a table), what is the immediate correct action?",
                "o1": "Ignore it to be polite.",
                "o2": "Stop the Line immediately and announce the contamination clearly.",
                "o3": "Wait until after the surgery to mention it.",
                "o4": "Try to wipe the spot clean yourself.",
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