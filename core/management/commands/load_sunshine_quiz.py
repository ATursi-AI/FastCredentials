from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for The Sunshine Act (Appends Only - No Deletes)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the Course
        # Search for "Sunshine" or "Open Payments"
        courses = Course.objects.filter(title__icontains="Sunshine")
        
        if not courses.exists():
            # Fallback search
            courses = Course.objects.filter(title__icontains="Open Payments")

        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'Sunshine' or 'Open Payments' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion)
        
        questions = [
            # BASICS & SCOPE
            {
                "text": "What is the primary purpose of the Physician Payments Sunshine Act (Open Payments)?",
                "o1": "To tax doctors more.",
                "o2": "To increase transparency by creating a public database of financial relationships between industry and providers.",
                "o3": "To ban all meals.",
                "o4": "To track patient outcomes.",
                "correct": 2
            },
            {
                "text": "Which of the following groups was added to the 'Covered Recipients' list in 2021?",
                "o1": "Hospital Janitors.",
                "o2": "Nurse Practitioners (NPs) and Physician Assistants (PAs).",
                "o3": "Veterinarians.",
                "o4": "Medical Students.",
                "correct": 2
            },
            {
                "text": "Who can access the Open Payments database to see how much money a doctor received?",
                "o1": "Only the FBI.",
                "o2": "Only the hospital admin.",
                "o3": "The general public (including patients, lawyers, and journalists).",
                "o4": "Only the doctor.",
                "correct": 3
            },

            # TRANSFERS OF VALUE & MEALS
            {
                "text": "If you buy a business lunch for 1 Doctor and 3 Office Staff members, and the total bill is $200, what amount is reportable?",
                "o1": "$200 (The whole bill).",
                "o2": "$50 (The doctor's share: $200 divided by 4).",
                "o3": "$0 (Staff meals cancel it out).",
                "o4": "$100.",
                "correct": 2
            },
            {
                "text": "What is the approximate 'De Minimis' threshold (2024 standards) for a single small transfer of value?",
                "o1": "About $12 (unless the annual aggregate exceeds ~$120).",
                "o2": "$50.",
                "o3": "$100.",
                "o4": "$1.",
                "correct": 1
            },
            {
                "text": "If you drop off donuts for a clinic but do NOT stay to eat/educate ('Dine and Dash'), how is this categorized?",
                "o1": "A business meal.",
                "o2": "A non-educational gift (often prohibited by AdvaMed policies).",
                "o3": "Charity.",
                "o4": "A sample.",
                "correct": 2
            },

            # EXCLUSIONS & OWNERSHIP
            {
                "text": "Which of the following items is EXEMPT (Excluded) from Sunshine Act reporting?",
                "o1": "A branded coffee mug.",
                "o2": "An iPad.",
                "o3": "Educational materials that directly benefit patients (e.g., anatomical wall chart, textbook).",
                "o4": "A golf trip.",
                "correct": 3
            },
            {
                "text": "Is a product sample (e.g., an implant used for free evaluation in surgery) reportable as income?",
                "o1": "Yes, it is a gift.",
                "o2": "No. Evaluation samples are excluded from reporting.",
                "o3": "Yes, but only if it works.",
                "o4": "Only if it costs over $1,000.",
                "correct": 2
            },
            {
                "text": "If a physician owns stock (equity) in a medical device distributor, is this ownership reportable?",
                "o1": "No, investments are private.",
                "o2": "Yes. Ownership and investment interests (including those of immediate family) must be reported.",
                "o3": "Only if they own more than 50%.",
                "o4": "Only if they sell the stock.",
                "correct": 2
            },

            # RESEARCH & LOGISTICS
            {
                "text": "How are payments for Clinical Research (trials) reported?",
                "o1": "They are not reported.",
                "o2": "They are reported separately as 'Research Payments' linked to the Principal Investigator.",
                "o3": "They are reported as 'Food and Beverage'.",
                "o4": "They are listed as 'Charity'.",
                "correct": 2
            },
            {
                "text": "Why is it critical for a sales rep to have the doctor's correct NPI (National Provider Identifier) number?",
                "o1": "To call them.",
                "o2": "To ensure the payment is attributed to the correct 'Dr. Smith' in the federal system.",
                "o3": "To check their credit score.",
                "o4": "To send them Christmas cards.",
                "correct": 2
            },
            {
                "text": "Can you avoid reporting a payment to a doctor by funneling the money through a third party (like a medical society)?",
                "o1": "Yes, that is a loophole.",
                "o2": "No. 'Indirect Payments' are fully reportable if you know the ultimate recipient.",
                "o3": "Yes, if you use cash.",
                "o4": "Only in California.",
                "correct": 2
            },

            # DISPUTES & PENALTIES
            {
                "text": "What happens during the annual 'Dispute Period' (April-May)?",
                "o1": "Doctors can delete their data.",
                "o2": "Doctors can review reported payments and file a dispute if they disagree with the amount.",
                "o3": "The database is deleted.",
                "o4": "Vendors pay fines.",
                "correct": 2
            },
            {
                "text": "What is the penalty for 'Knowing Failure' to report (intentionally hiding payments)?",
                "o1": "$100 fine.",
                "o2": "Up to $100,000 per record (capped at $1 Million) and potential DOJ investigation.",
                "o3": "A warning letter.",
                "o4": "Suspension of driver's license.",
                "correct": 2
            },
            {
                "text": "If a State Law conflicts with the Sunshine Act regarding *reporting*, which one wins?",
                "o1": "The State Law.",
                "o2": "The Sunshine Act generally preempts (overrules) state reporting laws to create one uniform federal standard.",
                "o3": "Neither.",
                "o4": "The Hospital policy.",
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