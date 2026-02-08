from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Restores BBP with Big Buck Bunny (Guaranteed to Play)'

    def handle(self, *args, **kwargs):
        self.stdout.write("Injecting Test Content...")

        # 1. Get Course
        course = Course.objects.filter(title__icontains="Bloodborne").first()
        if not course:
            self.stdout.write(self.style.ERROR("Course not found."))
            return

        # 2. Clear old data (This removes the "Unavailable" videos)
        Lesson.objects.filter(course=course).delete()
        Question.objects.filter(course=course).delete()

        # 3. Define Content
        # We use the DIRECT EMBED URL. This works with your new HTML immediately.
        # This video (Big Buck Bunny) is open source and CANNOT be blocked.
        VIDEO = "https://www.youtube.com/embed/aqz-KE-bpKQ"

        # Lesson 1
        Lesson.objects.create(
            course=course,
            title="1. OSHA Standard 1910.1030 Overview",
            content=(
                "The Occupational Safety and Health Administration (OSHA) issued the Bloodborne Pathogens Standard (29 CFR 1910.1030) "
                "specifically to protect workers from the severe health risks associated with exposure to human blood. "
                "This federal regulation applies to all employees who have 'occupational exposure.'\n\n"
                "A central requirement is the Exposure Control Plan (ECP). This is a written document that every employer must compile and update annually. "
                "It must be accessible to employees at all times.\n\n"
                "KEY TAKEAWAY: The Exposure Control Plan (ECP) is your employer's written safety playbook. "
                "You have the legal right to review it at any time."
            ),
            video_url=VIDEO,
            order=1
        )

        # Lesson 2
        Lesson.objects.create(
            course=course,
            title="2. Epidemiology: HBV, HCV, HIV",
            content=(
                "The three most critical pathogens are Hepatitis B (HBV), Hepatitis C (HCV), and HIV. "
                "Hepatitis B is uniquely resilient. OSHA data indicates that HBV can survive in dried blood on environmental surfaces "
                "for at least 7 days and remain infectious.\n\n"
                "Hepatitis C is the leading cause of liver transplants in the U.S. "
                "HIV attacks the immune system but is more fragile outside the body than Hepatitis B.\n\n"
                "KEY TAKEAWAY: Hepatitis B is the most environmentally durable pathogen. "
                "It can survive in dried blood on surfaces for at least 7 days."
            ),
            video_url=VIDEO,
            order=2
        )

        # Lesson 3
        Lesson.objects.create(
            course=course,
            title="3. Modes of Transmission",
            content=(
                "Transmission occurs primarily through parenteral exposure (needlesticks) and mucous membrane contact. "
                "In orthopedic surgery, 'aerosolization' is a significant hazard. "
                "High-speed bone saws and reamers generate a fine mist of blood that can land in your eyes.\n\n"
                "KEY TAKEAWAY: In Orthopedics, aerosolized blood mist is a hidden danger. "
                "You must wear eye protection with side shields."
            ),
            video_url=VIDEO,
            order=3
        )

        # Lesson 4
        Lesson.objects.create(
            course=course,
            title="4. OPIM: Other Potentially Infectious Materials",
            content=(
                "The OSHA standard covers 'Other Potentially Infectious Materials' (OPIM). "
                "You must treat these fluids with the exact same level of caution as frank blood. "
                "For the orthopedic vendor, the most critical OPIM is Synovial Fluid (joint fluid).\n\n"
                "KEY TAKEAWAY: Synovial (Joint) Fluid is classified as OPIM. "
                "Treat it exactly like human blood."
            ),
            video_url=VIDEO,
            order=4
        )

        # Lesson 5
        Lesson.objects.create(
            course=course,
            title="5. Engineering Controls",
            content=(
                "Engineering Controls isolate the hazard from the worker (e.g., Sharps Containers). "
                "Never reach into a sharps container to retrieve a dropped item. "
                "Never overfill these containers—forcing a needle into a stuffed container is a leading cause of injury.\n\n"
                "KEY TAKEAWAY: Engineering Controls are your primary shield. "
                "Never reach into or overfill a Sharps container."
            ),
            video_url=VIDEO,
            order=5
        )

        # Lesson 6
        Lesson.objects.create(
            course=course,
            title="6. Work Practice Controls (Hand Hygiene)",
            content=(
                "Work Practice Controls rely on your behavior, primarily Hand Hygiene. "
                "Hands must be washed immediately after removing gloves. "
                "Alcohol-based rubs do NOT kill C. Difficile spores. If C. Diff is present, use soap and water.\n\n"
                "KEY TAKEAWAY: Hand washing is the most effective prevention. "
                "Use soap and water (not sanitizer) if C. Diff is present."
            ),
            video_url=VIDEO,
            order=6
        )

        # Lesson 7
        Lesson.objects.create(
            course=course,
            title="7. Personal Protective Equipment (PPE)",
            content=(
                "PPE is the 'last line of defense.' It must prevent blood from passing through to your skin. "
                "In orthopedics, knee-high fluid-resistant boot covers are often required. "
                "You must remove all PPE before leaving the work area.\n\n"
                "KEY TAKEAWAY: PPE must be removed BEFORE leaving the work area to prevent cross-contamination."
            ),
            video_url=VIDEO,
            order=7
        )

        # Lesson 8
        Lesson.objects.create(
            course=course,
            title="8. Hepatitis B Vaccination",
            content=(
                "Employers must make the Hepatitis B vaccination available within 10 days of assignment. "
                "It is a 3-dose series that is over 90% effective. "
                "It must be provided at no cost. You can decline it, but you can also change your mind later and accept it.\n\n"
                "KEY TAKEAWAY: The Hepatitis B vaccine is free, effective, and your legal right."
            ),
            video_url=VIDEO,
            order=8
        )

        # Lesson 9
        Lesson.objects.create(
            course=course,
            title="9. Emergency Exposure Protocol",
            content=(
                "If exposed: 1. Wash the area immediately. 2. Report it to a supervisor. 3. Seek medical evaluation. "
                "Time is critical. Post-Exposure Prophylaxis (PEP) is most effective if started within hours.\n\n"
                "KEY TAKEAWAY: If exposed, Wash immediately, then Report immediately. "
                "Do not wait—minutes matter."
            ),
            video_url=VIDEO,
            order=9
        )

        # Lesson 10
        Lesson.objects.create(
            course=course,
            title="10. Recordkeeping & Rights",
            content=(
                "Employers must maintain a 'Sharps Injury Log' and your confidential medical records. "
                "OSHA mandates that these records be maintained for the duration of your employment plus 30 years.\n\n"
                "KEY TAKEAWAY: Your exposure medical records are strictly confidential and must be kept for 30 years."
            ),
            video_url=VIDEO,
            order=10
        )

        # Quiz
        Question.objects.create(
            course=course,
            text="According to OSHA, how long can the Hepatitis B virus survive in dried blood on a surface?",
            option_1="1 hour",
            option_2="24 hours",
            option_3="At least 7 days",
            option_4="It dies immediately upon drying",
            correct_option=3
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: Content updated.'))