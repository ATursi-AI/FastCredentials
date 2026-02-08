from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads the Universal Bloodborne Pathogens Exam questions into the database'

    def handle(self, *args, **kwargs):
        # 1. Get the Course by TITLE (The smart way)
        try:
            course = Course.objects.get(title="Bloodborne Pathogens")
            self.stdout.write(self.style.SUCCESS(f'Found Course: {course.title} (ID: {course.id})'))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course "Bloodborne Pathogens" not found. Please check your course list.'))
            return

        # 2. Clear existing questions
        Question.objects.filter(course=course).delete()
        self.stdout.write(self.style.WARNING('Cleared old questions.'))

        # 3. Define the Questions & Answers
        # Format: (Question Text, Option 1, Option 2, Option 3, Option 4, Correct Option Number)
        quiz_data = [
            (
                "What is the core principle of 'Standard Precautions' (formerly Universal Precautions)?",
                "Only patients with visible symptoms should be treated as infectious.",
                "Precautions are only necessary when working in the Emergency Department.",
                "All human blood and body fluids must be treated as if they are known to be infectious.",
                "You only need to wear gloves if you have an open cut on your hand.",
                3
            ),
            (
                "Under OSHA regulations, which activity is strictly prohibited in areas where blood is present?",
                "Applying lip balm or cosmetics.",
                "Drinking water from a sealed bottle.",
                "Handling contact lenses.",
                "All of the above.",
                4
            ),
            (
                "You have just removed a pair of gloves after working in a patient area. What is your next immediate step?",
                "Put on a new pair of gloves immediately.",
                "Wash your hands with soap and water or use an alcohol-based hand sanitizer.",
                "Inspect your hands for cuts; if none are found, no washing is needed.",
                "Report to the nurse's station.",
                2
            ),
            (
                "Which statement regarding the Hepatitis B vaccine is true for all personnel with occupational exposure?",
                "It is required by law for you to pay for it yourself.",
                "It must be offered by the employer at no cost to the employee.",
                "You can only get it after you have had an accident.",
                "It is 100% mandatory and you cannot sign a declination form.",
                2
            ),
            (
                "You encounter a refrigerator labeled with a fluorescent orange-red 'Biohazard' sticker. What does this indicate?",
                "The refrigerator is broken and needs repair.",
                "The refrigerator contains food for staff lunches.",
                "The refrigerator contains blood, tissue samples, or other potentially infectious materials.",
                "The refrigerator is for sterile medication storage only.",
                3
            ),
            (
                "You drop a glass vial containing a potential blood specimen, and it shatters. How should the broken glass be picked up?",
                "Carefully with your gloved hands.",
                "By wrapping a towel around your hand and picking it up.",
                "Using mechanical means only, such as a brush and dustpan, tongs, or forceps.",
                "Wait for the liquid to dry, then sweep it up.",
                3
            ),
            (
                "If blood or other potentially infectious material splashes into your eyes, nose, or mouth, what should you do immediately?",
                "Flush the area with water or saline for at least 15 minutes.",
                "Cover the area with a bandage.",
                "Wait until your shift ends to clean it.",
                "Report it to your supervisor before cleaning yourself.",
                1
            ),
            (
                "Which of the following items belongs in a Red Biohazard Bag?",
                "A paper towel used to dry clean hands.",
                "A soda can from a patient's room.",
                "Liquid or semi-liquid blood, or items that would release blood if compressed (squeezed).",
                "Used needles or scalpels.",
                3
            ),
            (
                "Bloodborne pathogens such as HIV and Hepatitis B are primarily transmitted through:",
                "Casual contact like shaking hands or hugging.",
                "Coughing or sneezing (airborne).",
                "Sexual contact, sharing needles, or contact with infected blood through broken skin.",
                "Sharing a water fountain.",
                3
            ),
            (
                "How should laundry (scrubs, lab coats, linens) that is wet with blood be handled?",
                "Rinse it in the nearest sink before bagging it.",
                "Take it home to wash it separately.",
                "Place it in a labeled or color-coded leak-proof bag or container at the location where it was used.",
                "Leave it on the floor for Environmental Services to find.",
                3
            ),
        ]

        # 4. Loop and Save
        for q in quiz_data:
            Question.objects.create(
                course=course,
                text=q[0],
                option_1=q[1],
                option_2=q[2],
                option_3=q[3],
                option_4=q[4],
                correct_option=q[5]
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded 10 BBP Exam Questions into Course ID {course.id}!'))