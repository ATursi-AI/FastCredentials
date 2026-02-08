from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Rebuilds the Core 12 Grid with BBP First (High Quality)'

    def handle(self, *args, **kwargs):
        self.stdout.write("Resorting Grid: Placing Bloodborne Pathogens at #1...")
        
        # 1. WIPE EVERYTHING TO RESET IDs
        Question.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        # --- COURSE 1: BLOODBORNE PATHOGENS (The High-Quality Version) ---
        c1 = Course.objects.create(
            title="1. Bloodborne Pathogens",
            description="Complete OSHA 29 CFR 1910.1030 certification. Deep-dive into exposure control, O.R. transmission risks, and Universal Precautions.",
            duration_minutes=60,
            icon_name="bi-droplet-fill",
            price=19.99
        )
        # The 10 "Textbook" Modules we just verified
        bbp_lessons = [
             {"t": "1. Introduction to OSHA Standard 1910.1030", "c": """The Occupational Safety and Health Administration (OSHA) enacted the Bloodborne Pathogens Standard (29 CFR 1910.1030) to reduce the occupational risk of exposure to infectious materials. This standard covers all employees who, as part of their job duties, may reasonably expect to be exposed to blood or Other Potentially Infectious Materials (OPIM).\n\nAs a medical vendor, you fall under 'Category I' classification. This means your daily tasks—whether supporting a case in the O.R. or demonstrating a device in the Cath Lab—place you at direct risk. Compliance with this standard is not voluntary; it is a federal requirement designed to save lives."""},
             {"t": "2. Epidemiology & Symptoms", "c": """Bloodborne pathogens are pathogenic microorganisms that are present in human blood and can cause disease in humans. The three most significant pathogens in the healthcare environment are Hepatitis B (HBV), Hepatitis C (HCV), and Human Immunodeficiency Virus (HIV).\n\nHepatitis B is the most transmissible. It attacks the liver and can survive in dried blood on surfaces for at least 7 days. Symptoms include jaundice and fatigue, though many show no symptoms at all."""},
             {"t": "3. Modes of Transmission", "c": """Transmission most commonly occurs through needlesticks, cuts, or splashes to mucous membranes. In orthopedics, 'aerosolization' is a critical risk. High-speed power tools create a mist of blood and tissue. Without a face shield, this infectious mist can land directly in your eyes or mouth."""},
             {"t": "4. OPIM: Not Just Blood", "c": """You must treat OPIM with the same caution as frank blood. OPIM includes semen, vaginal secretions, cerebrospinal fluid, and most importantly for you: Synovial Fluid (joint fluid). In a surgical setting, assume all fluids are contaminated."""},
             {"t": "5. Universal Precautions", "c": """Universal Precautions is the approach where ALL human blood is treated as if known to be infectious. You do not relax standards for 'healthy-looking' patients. Every case is treated as a high-risk biohazard case."""},
             {"t": "6. Engineering Controls", "c": """Engineering controls isolate the hazard. Examples: Sharps containers, self-sheathing needles, and needleless systems. Never reach into a sharps container. If it's full, report it."""},
             {"t": "7. Work Practice Controls", "c": """Work practices alter how a task is done. The #1 rule: Hand Hygiene. Wash hands immediately after glove removal. No eating, drinking, or applying lip balm in the O.R."""},
             {"t": "8. Personal Protective Equipment (PPE)", "c": """When exposure remains, PPE is mandatory. This includes gloves, fluid-resistant gowns, and face shields. If blood penetrates your PPE, remove it immediately and wash the skin."""},
             {"t": "9. Hepatitis B Vaccine", "c": """Your employer must offer the Hep B vaccine series free of charge within 10 days of employment. It is 90% effective. You may decline, but must sign a waiver."""},
             {"t": "10. Emergency Protocol", "c": """If exposed: 1. WASH with soap/water. 2. FLUSH eyes/mouth. 3. REPORT to Charge Nurse immediately. 4. DOCUMENT the incident. 5. SEEK medical evaluation."""}
        ]
        for idx, l in enumerate(bbp_lessons):
            Lesson.objects.create(course=c1, title=l['t'], content=l['c'], video_url="https://www.youtube.com/watch?v=D-aM8eS5X-I" if idx==0 else "", order=idx+1)
        
        Question.objects.create(course=c1, text="Which fluid is considered OPIM and high-risk in Orthopedics?", option_1="Sweat", option_2="Tears", option_3="Synovial Fluid", option_4="Saliva", correct_option=3)


        # --- COURSES 2-12: PLACEHOLDERS (To be updated one-by-one later) ---
        placeholder_courses = [
            ("2. HIPAA Privacy", "bi-shield-lock"),
            ("3. Aseptic Technique", "bi-mask"),
            ("4. Fire Safety", "bi-fire"),
            ("5. Radiation Safety", "bi-radioactive"),
            ("6. Electrical Safety", "bi-lightning-fill"),
            ("7. AdvaMed Ethics", "bi-briefcase-fill"),
            ("8. O.R. Protocol", "bi-people-fill"),
            ("9. Infection Control", "bi-bug-fill"),
            ("10. Sunshine Act", "bi-sun-fill"),
            ("11. Hazardous Materials", "bi-exclamation-triangle-fill"),
            ("12. Patient Rights", "bi-heart-pulse-fill"),
        ]

        for title, icon in placeholder_courses:
            c = Course.objects.create(title=title, description="Content coming soon in Phase 2 update.", duration_minutes=45, icon_name=icon, price=19.99)
            Lesson.objects.create(course=c, title="Overview", content="This module is currently being updated to World-Class standards.", order=1)
            Question.objects.create(course=c, text="Placeholder Question", option_1="A", option_2="B", option_3="C", option_4="D", correct_option=1)

        self.stdout.write(self.style.SUCCESS('SUCCESS: Grid restored. BBP is #1 with Full Content.'))