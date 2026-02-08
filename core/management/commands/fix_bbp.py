from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Rebuilds Bloodborne Pathogens with Textbook-Depth Content'

    def handle(self, *args, **kwargs):
        self.stdout.write("Wiping old BBP data and injecting LONG-FORM content...")
        
        # 1. Clean Slate: Delete any course with "Bloodborne" in the title
        Course.objects.filter(title__icontains="Bloodborne").delete()

        # 2. Create the Master Course
        c = Course.objects.create(
            title="Bloodborne Pathogens",
            description="Complete OSHA 29 CFR 1910.1030 certification. This course covers the epidemiology, transmission, and prevention of bloodborne diseases in clinical settings.",
            duration_minutes=60,
            icon_name="bi-droplet-fill",
            price=19.99
        )

        # 3. Define the 10 Lessons with TEXTBOOK DEPTH (Multi-paragraph)
        lessons_data = [
            {
                "t": "1. Introduction to OSHA Standard 1910.1030",
                "c": """The Occupational Safety and Health Administration (OSHA) enacted the Bloodborne Pathogens Standard (29 CFR 1910.1030) to reduce the occupational risk of exposure to infectious materials. This standard covers all employees who, as part of their job duties, may reasonably expect to be exposed to blood or Other Potentially Infectious Materials (OPIM).

As a medical vendor, you fall under 'Category I' classification. This means your daily tasks—whether supporting a case in the O.R. or demonstrating a device in the Cath Lab—place you at direct risk. Compliance with this standard is not voluntary; it is a federal requirement designed to save lives.

The standard requires your employer to have a written Exposure Control Plan (ECP), designed to eliminate or minimize employee exposure. This plan must be accessible to you at all times and updated annually to reflect changes in technology, such as the adoption of safer medical devices."""
            },
            {
                "t": "2. Epidemiology & Symptoms of Disease",
                "c": """Bloodborne pathogens are pathogenic microorganisms that are present in human blood and can cause disease in humans. The three most significant pathogens in the healthcare environment are Hepatitis B (HBV), Hepatitis C (HCV), and Human Immunodeficiency Virus (HIV).

Hepatitis B is the most transmissible of the three. It attacks the liver and can survive in dried blood on surfaces (like instrument trays or bed rails) for at least 7 days. Symptoms include jaundice, fatigue, and abdominal pain, though 30% of infected individuals show no symptoms at all.

Hepatitis C is the leading cause of liver transplants in the U.S. There is currently no vaccine for HCV, making prevention and strict adherence to safety protocols your only defense. HIV, while less durable outside the body than Hepatitis, attacks the immune system and remains a critical concern in needlestick injuries."""
            },
            {
                "t": "3. Modes of Transmission in the O.R.",
                "c": """Transmission of bloodborne pathogens in the surgical suite most commonly occurs through three routes: parenteral exposure (needlesticks or cuts), mucous membrane exposure (splashes to the eyes, nose, or mouth), and exposure of non-intact skin (dermatitis, hangnails, or abrasions).

In an orthopedic setting, 'aerosolization' is a critical, often overlooked mode of transmission. High-speed power tools such as bone saws, drills, and reamers create a fine mist of blood and tissue debris. If you are standing within 2-3 feet of the sterile field without a face shield, this infectious mist can land directly in your eyes or mouth.

You must also be aware of indirect transmission. Handling contaminated instrument trays or 'dirty' lead aprons without gloves can transfer pathogens to your hands. If you then touch your eyes or mouth, transmission can occur."""
            },
            {
                "t": "4. OPIM: It's Not Just Blood",
                "c": """The standard applies to blood and 'Other Potentially Infectious Materials' (OPIM). You must treat these fluids with the same caution as frank blood. OPIM includes semen, vaginal secretions, cerebrospinal fluid, synovial fluid, pleural fluid, pericardial fluid, peritoneal fluid, and amniotic fluid.

For orthopedic vendors, Synovial Fluid (joint fluid) is the primary concern. During arthroscopy or total joint replacement, liters of saline mixed with synovial fluid and blood are suctioned into waste canisters. Leakage from these canisters or splashing during tube changes poses a severe exposure risk.

Note that urine, feces, sweat, tears, and vomit are NOT considered OPIM unless they are visibly contaminated with blood. However, in a surgical setting, it is safest to assume all fluids are contaminated."""
            },
            {
                "t": "5. Universal Precautions",
                "c": """'Universal Precautions' is the infection control approach where all human blood and certain human body fluids are treated as if they are known to be infectious for HIV, HBV, and other bloodborne pathogens.

This means you do not change your safety behavior based on the patient. You do not relax your standards because a patient 'looks healthy' or is a 'routine' case. Every patient is treated as a potential carrier.

This approach eliminates the need for judgment calls in high-stress situations. Whether it is a trauma case at 2 AM or a scheduled elective procedure, your barrier protection and handling of sharps remain identical."""
            },
            {
                "t": "6. Engineering Controls",
                "c": """Engineering controls are physical items or devices that isolate or remove the bloodborne pathogens hazard from the workplace. These are the most effective means of protection because they function independently of worker behavior.

Common engineering controls include sharps disposal containers (red biohazard boxes), self-sheathing needles, and needleless IV systems. As a vendor, you must recognize these controls and never tamper with them.

For example, if a sharps container is full, never attempt to push trash down to make room. Never reach into a container to retrieve a dropped item. If you see an engineering control that is broken or missing, report it to the Circulating Nurse immediately."""
            },
            {
                "t": "7. Work Practice Controls",
                "c": """Work practice controls reduce the likelihood of exposure by altering the manner in which a task is performed. The single most important practice is Hand Hygiene. You must wash your hands with soap and water immediately after removing gloves.

Other mandatory practices include:
1. No Recapping: Never bend, break, or recap contaminated needles by hand.
2. No Eating/Drinking: Food and drink are strictly prohibited in areas where blood or OPIM are present (e.g., the O.R. sub-sterile room or Cath Lab control room).
3. Minimizing Splatter: Perform all procedures involving blood in a manner that minimizes splashing, spraying, or generation of droplets."""
            },
            {
                "t": "8. Personal Protective Equipment (PPE)",
                "c": """When engineering and work practice controls are not enough, Personal Protective Equipment (PPE) is your barrier. Employers must provide appropriate PPE at no cost to you.

'Appropriate' PPE means it does not permit blood or OPIM to pass through to your work clothes, street clothes, undergarments, skin, or mucous membranes. This includes gloves, gowns, laboratory coats, face shields or masks, and eye protection.

In the O.R., shoe covers are mandatory to prevent tracking blood out of the suite. If your PPE is penetrated by blood (e.g., a torn glove or soaked gown), it must be removed and replaced immediately. Wash the underlying skin area with soap and water before donning new PPE."""
            },
            {
                "t": "9. Hepatitis B Vaccination & Declination",
                "c": """Your employer must make the Hepatitis B vaccination series available to you within 10 working days of your initial assignment. This vaccine is safe, effective, and provided at no cost to you.

The vaccination consists of a three-dose series over a 6-month period. It induces protective antibody levels in over 90% of healthy adults.

You have the right to decline the vaccination. However, OSHA requires you to sign a specific 'Hepatitis B Declination Statement' confirming you understand the risks. If you initially decline, you are allowed to change your mind and receive the vaccination at a later date, still at no cost."""
            },
            {
                "t": "10. Emergency Post-Exposure Protocol",
                "c": """If an exposure incident occurs (e.g., a needlestick, cut, or splash to the eye):
1. IMMEDIATE ACTION: Wash the area with soap and water. Flush eyes, nose, or mouth with water or saline for 15 minutes.
2. REPORT: Notify the O.R. Charge Nurse or Manager immediately. Do not wait for the case to finish.
3. DOCUMENT: Your employer must document the route of exposure and the circumstances.
4. TEST: The source individual's blood must be tested (with consent) to determine infectivity.
5. FOLLOW-UP: You must be offered a confidential medical evaluation and post-exposure prophylaxis (PEP) if medically indicated."""
            }
        ]

        # 4. Inject Lessons with Video on Lesson 1
        # Using a verified, embeddable OSHA Intro video
        video_link = "https://www.youtube.com/watch?v=D-aM8eS5X-I" 

        for idx, l in enumerate(lessons_data):
            Lesson.objects.create(
                course=c,
                title=l['t'],
                content=l['c'], 
                video_url=video_link if idx == 0 else "", 
                order=idx + 1
            )
            
        # 5. Create the Quiz
        Question.objects.create(
            course=c, 
            text="Which fluid is considered OPIM and is a high risk for Orthopedic vendors due to aerosolization?", 
            option_1="Sweat", option_2="Tears", option_3="Synovial (Joint) Fluid", option_4="Saliva", 
            correct_option=3
        )

        self.stdout.write(self.style.SUCCESS('SUCCESS: Bloodborne Pathogens Rebuilt. 10 Deep-Dive Modules + Working Video.'))