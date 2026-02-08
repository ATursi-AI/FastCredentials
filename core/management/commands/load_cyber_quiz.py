from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for Cybersecurity & Ransomware (Appends Only)'

    def handle(self, *args, **kwargs):
        # 1. FIND COURSE
        courses = Course.objects.filter(title__icontains="Cyber")
        if not courses.exists():
             courses = Course.objects.filter(title__icontains="Ransomware")
             
        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}'"))
        else:
            self.stdout.write(self.style.ERROR("Error: Course not found."))
            return

        # 2. QUESTIONS
        questions = [
            # RANSOMWARE & VECTORS
            {
                "text": "What is a 'Supply Chain Attack' or 'Hub and Spoke' attack?",
                "o1": "Attacking the hospital cafeteria.",
                "o2": "Hackers targeting smaller vendors to gain access to the larger hospital network.",
                "o3": "Stealing delivery trucks.",
                "o4": "Cutting the power lines.",
                "correct": 2
            },
            {
                "text": "What characterizes 'Ransomware 2.0' (Double Extortion)?",
                "o1": "It only locks the files.",
                "o2": "It steals the data first to blackmail the victim, THEN locks the files.",
                "o3": "It is free.",
                "o4": "It only affects Macs.",
                "correct": 2
            },
            {
                "text": "If you suspect your laptop is infected with ransomware, what is the immediate first step?",
                "o1": "Turn it off.",
                "o2": "Disconnect from the network immediately (unplug cable/Wi-Fi) to stop the spread.",
                "o3": "Email IT.",
                "o4": "Pay the ransom.",
                "correct": 2
            },

            # PHISHING & MFA
            {
                "text": "What is 'MFA Fatigue'?",
                "o1": "Getting tired of typing passwords.",
                "o2": "Hackers spamming your phone with login requests hoping you accidentally click Approve.",
                "o3": "A virus that deletes MFA.",
                "o4": "Using the same password everywhere.",
                "correct": 2
            },
            {
                "text": "What is 'Vishing'?",
                "o1": "Visual Phishing.",
                "o2": "Voice Phishing (using phone calls, often with AI voice cloning, to steal credentials).",
                "o3": "Video Phishing.",
                "o4": "Virtual Phishing.",
                "correct": 2
            },
            {
                "text": "Which authentication method is considered 'Phishing-Resistant'?",
                "o1": "A sticky note on the monitor.",
                "o2": "Passkeys / Biometrics (FaceID/TouchID).",
                "o3": "SMS Text Codes.",
                "o4": "Security Questions (Mother's maiden name).",
                "correct": 2
            },

            # PHYSICAL & USB
            {
                "text": "What should you do if you find a USB drive labeled 'Payroll' in the parking lot?",
                "o1": "Plug it in to see who it belongs to.",
                "o2": "Do NOT plug it in; hand it to Security or IT.",
                "o3": "Format it and keep it.",
                "o4": "Throw it in the trash.",
                "correct": 2
            },
            {
                "text": "What is 'Juice Jacking'?",
                "o1": "Stealing juice from the fridge.",
                "o2": "Stealing data via a public USB charging station.",
                "o3": "Overclocking your CPU.",
                "o4": "Spilling liquid on a laptop.",
                "correct": 2
            },
            {
                "text": "Why should you use a Privacy Filter on your screen in public?",
                "o1": "To reduce glare.",
                "o2": "To prevent 'Shoulder Surfing' (people reading sensitive data from side angles).",
                "o3": "To save battery.",
                "o4": "It looks cool.",
                "correct": 2
            },

            # NETWORK & CLOUD
            {
                "text": "Is it safe to use personal cloud storage (Google Drive/Dropbox) for hospital files?",
                "o1": "Yes, if it's convenient.",
                "o2": "No. This is 'Shadow IT' and a major security violation.",
                "o3": "Yes, if you delete it later.",
                "o4": "Only for Excel files.",
                "correct": 2
            },
            {
                "text": "When using public Wi-Fi (e.g., at an airport), what must you use to secure your connection?",
                "o1": "Incognito Mode.",
                "o2": "A Virtual Private Network (VPN).",
                "o3": "A strong password.",
                "o4": "Bluetooth.",
                "correct": 2
            },
            {
                "text": "What is an 'Evil Twin' Wi-Fi attack?",
                "o1": "Two hackers working together.",
                "o2": "A fake Wi-Fi hotspot with a name similar to the real one (e.g., 'Hospital_Guest_Free').",
                "o3": "A virus that doubles your files.",
                "o4": "A blocked router.",
                "correct": 2
            },

            # REGULATIONS & REPORTING
            {
                "text": "Under the CIRCIA 2026 rules, what is the deadline for reporting a substantial cyber incident?",
                "o1": "30 Days.",
                "o2": "72 Hours.",
                "o3": "1 Week.",
                "o4": "24 Hours.",
                "correct": 2
            },
            {
                "text": "If a ransom payment is made, how quickly must it be reported under CIRCIA?",
                "o1": "72 Hours.",
                "o2": "24 Hours.",
                "o3": "Never.",
                "o4": "30 Days.",
                "correct": 2
            },
            {
                "text": "What is the 'Clean Desk Policy'?",
                "o1": "Using sanitizer on your desk.",
                "o2": "Ensuring no sensitive documents or passwords are left visible/unsecured when you leave.",
                "o3": "Throwing away all papers daily.",
                "o4": "Cleaning the mouse.",
                "correct": 2
            }
        ]

        self.stdout.write(f"Adding {len(questions)} questions...")
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
        self.stdout.write(self.style.SUCCESS("Success!"))