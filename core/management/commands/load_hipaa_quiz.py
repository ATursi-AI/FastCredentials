from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for HIPAA Training (Appends Only - No Deletes)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the HIPAA Course
        # Searching for "HIPAA" is safe and specific.
        courses = Course.objects.filter(title__icontains="HIPAA")
        
        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'HIPAA' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion)
        # We are strictly ADDING to the existing bank.
        
        questions = [
            # FOUNDATIONS & IDENTIFIERS
            {
                "text": "Which of the following is included in the 18 specific HIPAA Identifiers?",
                "o1": "Political affiliation",
                "o2": "Internet Protocol (IP) address",
                "o3": "Eye color",
                "o4": "Favorite food",
                "correct": 2
            },
            {
                "text": "Under the HIPAA Omnibus Rule, which entities are directly liable for federal compliance penalties?",
                "o1": "Only Hospitals (Covered Entities)",
                "o2": "Only Doctors",
                "o3": "Both Covered Entities and Business Associates (Vendors)",
                "o4": "Only Insurance Companies",
                "correct": 3
            },
            {
                "text": "The 'Minimum Necessary Standard' implies that you should:",
                "o1": "Access the entire medical record to be safe.",
                "o2": "Access only the specific information required to perform your job duty.",
                "o3": "Ask the patient for permission before looking at any file.",
                "o4": "Only access data during business hours.",
                "correct": 2
            },
            # SECURITY & TECHNOLOGY
            {
                "text": "Regarding 'Technical Safeguards,' why is encryption considered the most critical protection for mobile devices?",
                "o1": "It makes the device run faster.",
                "o2": "It prevents viruses.",
                "o3": "If an encrypted device is lost, it is generally NOT considered a reportable breach.",
                "o4": "It is required by the FDA.",
                "correct": 3
            },
            {
                "text": "Is sending a patient's diagnosis and name via standard SMS text messaging compliant with HIPAA?",
                "o1": "Yes, if the doctor asks for it.",
                "o2": "No, standard SMS is unencrypted and not secure.",
                "o3": "Yes, if you delete it afterwards.",
                "o4": "Yes, if you use abbreviations.",
                "correct": 2
            },
            {
                "text": "Which of the following cloud storage practices is a HIPAA violation?",
                "o1": "Storing patient lists on a personal Dropbox or Google Drive account.",
                "o2": "Using an enterprise Box account with a signed BAA.",
                "o3": "Using an encrypted company server.",
                "o4": "Storing data on a hospital-issued encrypted tablet.",
                "correct": 1
            },
            # BREACH & HITECH
            {
                "text": "What is the absolute maximum federal deadline for notifying the authorities of a PHI breach?",
                "o1": "24 hours",
                "o2": "30 days",
                "o3": "60 calendar days (though contracts may require sooner)",
                "o4": "1 year",
                "correct": 3
            },
            {
                "text": "Under the HITECH Act, if a breach affects 500 or more individuals, the organization must notify HHS and:",
                "o1": " The local police",
                "o2": "Prominent media outlets (The 'Wall of Shame')",
                "o3": "The FBI",
                "o4": "The Governor",
                "correct": 2
            },
            {
                "text": "What does the term 'Willful Neglect' imply in terms of penalties?",
                "o1": "It means the violation was an accident.",
                "o2": "It means the rules were ignored, leading to mandatory maximum fines.",
                "o3": "It is a minor warning.",
                "o4": "It only applies to doctors.",
                "correct": 2
            },
            # DAILY OPERATIONS & SOCIAL MEDIA
            {
                "text": "You take a selfie in the OR to celebrate a successful case. In the background, a patient's leg is visible (but not their face). Is this a HIPAA violation?",
                "o1": "No, because the face is not visible.",
                "o2": "Yes, because context and location can still identify the patient.",
                "o3": "No, because you didn't post it yet.",
                "o4": "Yes, but only if the patient complains.",
                "correct": 2
            },
            {
                "text": "What is the correct way to dispose of a physical paper document containing PHI?",
                "o1": "Crumple it up and throw it in the trash.",
                "o2": "Recycle bin.",
                "o3": "Shred it or place it in a locked 'burn bin'.",
                "o4": "Take it home to throw away.",
                "correct": 3
            },
            {
                "text": "An 'Incidental Disclosure' (like a patient overhearing a doctor) is permitted ONLY if:",
                "o1": "The doctor speaks very loudly.",
                "o2": "Reasonable safeguards (like lowered voices) were in place.",
                "o3": "The patient signs a waiver.",
                "o4": "It happens in the lobby.",
                "correct": 2
            },
            # ADVANCED / PENALTIES
            {
                "text": "What does TPO stand for regarding permitted disclosures?",
                "o1": "Time, Place, Occasion",
                "o2": "Treatment, Payment, Healthcare Operations",
                "o3": "Total Patient Observation",
                "o4": "Technical Privacy Officer",
                "correct": 2
            },
            {
                "text": "A Tier 4 HIPAA penalty involves 'Willful Neglect - Not Corrected.' What is the maximum annual penalty cap for such violations (as of 2024)?",
                "o1": "$10,000",
                "o2": "$100,000",
                "o3": "Over $2 million",
                "o4": "$500",
                "correct": 3
            },
            {
                "text": "Can a full-face photograph be considered PHI even if no name is attached?",
                "o1": "No, a face is not data.",
                "o2": "Yes, full-face photographic images are one of the 18 specific identifiers.",
                "o3": "Only if it is a celebrity.",
                "o4": "Only if the patient is smiling.",
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