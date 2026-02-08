from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for AdvaMed Code of Ethics (Appends Only - No Deletes)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the Course
        # We search for "AdvaMed" or "Ethics"
        courses = Course.objects.filter(title__icontains="AdvaMed")
        
        if not courses.exists():
            # Fallback search
            courses = Course.objects.filter(title__icontains="Ethics")

        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'AdvaMed' or 'Ethics' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion)
        
        questions = [
            # GIFTS & ENTERTAINMENT
            {
                "text": "Under the AdvaMed Code, are you allowed to take a doctor to a professional sporting event (NFL/NBA) if you discuss business during the game?",
                "o1": "Yes, if the ticket price is under $100.",
                "o2": "No. Entertainment is strictly prohibited, regardless of business discussion.",
                "o3": "Yes, if the doctor pays for their own hot dog.",
                "o4": "Only if it is a playoff game.",
                "correct": 2
            },
            {
                "text": "Are 'Branded Gifts' like coffee mugs, pens, or golf balls with your company logo permitted?",
                "o1": "Yes, as long as they are not worth much.",
                "o2": "No. Providing non-educational branded items is prohibited.",
                "o3": "Yes, but only at Christmas.",
                "o4": "Yes, if the doctor asks for them.",
                "correct": 2
            },
            {
                "text": "Which of the following is an acceptable gift for a Healthcare Professional?",
                "o1": "A bottle of wine.",
                "o2": "A medical textbook or anatomical model (modest value) that benefits patients.",
                "o3": "A gift card to Amazon.",
                "o4": "Cash.",
                "correct": 2
            },

            # MEALS
            {
                "text": "When providing a business meal to a physician, which condition must be met?",
                "o1": "The meal must be subordinate to a legitimate business/educational presentation.",
                "o2": "The meal can be at a nightclub.",
                "o3": "You can leave your credit card at the restaurant ('Dine and Dash').",
                "o4": "Spouses are invited.",
                "correct": 1
            },
            {
                "text": "Can you pay for a meal for a doctor's spouse if they attend the dinner?",
                "o1": "Yes, if the spouse is nice.",
                "o2": "No. You cannot pay for guests or spouses.",
                "o3": "Yes, if the bill is split.",
                "o4": "Only if it is their anniversary.",
                "correct": 2
            },

            # CONSULTANTS & GRANTS
            {
                "text": "When hiring a surgeon as a consultant, how is the Fair Market Value (FMV) of their payment determined?",
                "o1": "By how much product they buy from you.",
                "o2": "By their expertise and the nature of the work, independent of sales volume.",
                "o3": "By how much they ask for.",
                "o4": "By a percentage of the revenue they generate.",
                "correct": 2
            },
            {
                "text": "Can a sales representative select which specific residents receive an educational scholarship grant?",
                "o1": "Yes, to build relationships.",
                "o2": "No. Selection must be independent and handled by the conference organizers or a grant committee.",
                "o3": "Yes, if the resident uses your product.",
                "o4": "Only if the sales manager approves.",
                "correct": 2
            },

            # SAMPLES & DEMOS
            {
                "text": "Is it legal for a hospital to bill Medicare/Insurance for a free 'Evaluation Sample' you provided?",
                "o1": "Yes, that is pure profit for the hospital.",
                "o2": "No. This constitutes fraud (False Claims Act). Samples cannot be billed.",
                "o3": "Yes, if they call it a 'loaner'.",
                "o4": "Only in emergency cases.",
                "correct": 2
            },
            {
                "text": "How long can a piece of Capital Equipment (like a laser) generally be loaned for evaluation?",
                "o1": "Indefinitely.",
                "o2": "For a reasonable, defined period (e.g., 30-90 days) with a written agreement.",
                "o3": "Until the next model comes out.",
                "o4": "Just for the weekend.",
                "correct": 2
            },

            # OFF-LABEL & INTEGRITY
            {
                "text": "If a surgeon asks you how to use your device for an 'Off-Label' indication (unapproved use), what should you do?",
                "o1": "Tell them exactly how to do it.",
                "o2": "State that you can only discuss approved indications and refer them to Medical Affairs.",
                "o3": "Draw a diagram on a napkin.",
                "o4": "Show them a YouTube video of another doctor doing it.",
                "correct": 2
            },
            {
                "text": "Is it acceptable to wear a colleague's hospital badge if you forgot yours?",
                "o1": "Yes, as long as you look alike.",
                "o2": "No. This is badge swapping and violates security/credentialing protocols.",
                "o3": "Yes, if you return it later.",
                "o4": "Only for short cases.",
                "correct": 2
            },

            # GENERAL ETHICS
            {
                "text": "The primary goal of the AdvaMed Code is to ensure medical decisions are based on:",
                "o1": "Financial gain.",
                "o2": "Patient benefit and clinical need.",
                "o3": "Friendship.",
                "o4": "Stock prices.",
                "correct": 2
            },
            {
                "text": "Which federal law is closely tied to the AdvaMed Code regarding bribery?",
                "o1": "The Anti-Kickback Statute.",
                "o2": "The Clean Air Act.",
                "o3": "The Traffic Safety Act.",
                "o4": "The First Amendment.",
                "correct": 1
            },
            {
                "text": "Where is an acceptable venue for a company training meeting?",
                "o1": "A luxury ski resort in Aspen.",
                "o2": "A hotel with conference facilities or a corporate lab.",
                "o3": "A casino.",
                "o4": "A cruise ship.",
                "correct": 2
            },
            {
                "text": "If you witness a violation of the Code (like bribery), what is your duty?",
                "o1": "Ignore it.",
                "o2": "Report it (See Something, Say Something) via non-retaliatory channels.",
                "o3": "Post about it on Facebook.",
                "o4": "Ask for a raise.",
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