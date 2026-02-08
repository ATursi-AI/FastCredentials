from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Loads 15 Questions for Radiation Safety (Modules 1-15 Only)'

    def handle(self, *args, **kwargs):
        # 1. SURGICAL LOOKUP: Find the Course
        courses = Course.objects.filter(title__icontains="Radiation")
        
        if courses.exists():
            course = courses.first()
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}' (ID: {course.id})"))
        else:
            self.stdout.write(self.style.ERROR("Error: Could not find a course with 'Radiation' in the title."))
            return

        # 2. ADD QUESTIONS (No Deletion - Append Only)
        # These questions are strictly vetted to match ONLY Modules 1-15.
        
        questions = [
            # ALARA & PHYSICS (Modules 1-2)
            {
                "text": "What does the ALARA principle stand for?",
                "o1": "Always Leave Area Radiation Active",
                "o2": "As Low As Reasonably Achievable",
                "o3": "Allow Least Amount of Rads Allowed",
                "o4": "Anti-Lateral Anterior Ray Adjustment",
                "correct": 2
            },
            {
                "text": "In X-ray production, what percentage of energy is converted into Heat versus actual X-rays?",
                "o1": "50% Heat, 50% X-ray",
                "o2": "99% Heat, 1% X-ray (Inefficient)",
                "o3": "1% Heat, 99% X-ray (Efficient)",
                "o4": "100% X-ray",
                "correct": 2
            },

            # DISTANCE & POSITIONING (Modules 4, 6, 7)
            {
                "text": "According to the Inverse Square Law, if you double your distance from the radiation source, your exposure is reduced to:",
                "o1": "One half (50%)",
                "o2": "One quarter (25%)",
                "o3": "One tenth (10%)",
                "o4": "Zero",
                "correct": 2
            },
            {
                "text": "What is the primary source of scatter radiation exposure to the staff in the OR?",
                "o1": "The X-ray tube leakage.",
                "o2": "The Patient (radiation bounces off the patient's body).",
                "o3": "The floor.",
                "o4": "The monitor.",
                "correct": 2
            },
            {
                "text": "Which C-Arm orientation results in the HIGHEST radiation dose to the staff's head and neck?",
                "o1": "Tube Down (Tube under table)",
                "o2": "Tube Up (Tube over patient)",
                "o3": "Lateral",
                "o4": "Oblique",
                "correct": 2
            },
            {
                "text": "Where is the safest place to stand when a C-Arm is in the Lateral position?",
                "o1": "On the X-Ray Tube side.",
                "o2": "On the Image Intensifier (Detector) side.",
                "o3": "Directly behind the tube.",
                "o4": "Holding the patient.",
                "correct": 2
            },

            # TIME & MODES (Module 3, 13)
            {
                "text": "Which imaging mode generates the highest radiation dose per minute?",
                "o1": "Standard Fluoroscopy",
                "o2": "Cine (Cinematography) / High-Dose Recording",
                "o3": "Pulsed Fluoroscopy",
                "o4": "Static X-Ray",
                "correct": 2
            },
            {
                "text": "What is the purpose of the '5-Minute Timer' alarm on a fluoroscopy machine?",
                "o1": "It shuts the machine off automatically.",
                "o2": "It alerts the team to the cumulative beam-on time so they can assess risk.",
                "o3": "It indicates the machine is overheating.",
                "o4": "It means the procedure is over.",
                "correct": 2
            },

            # BIOLOGICAL EFFECTS & DOSIMETRY (Modules 8, 9)
            {
                "text": "Where should a standard radiation dosimetry badge be worn to get an accurate reading?",
                "o1": "On the belt, under the lead apron.",
                "o2": "At collar level, OUTSIDE the lead apron.",
                "o3": "In a pocket.",
                "o4": "Left in the car.",
                "correct": 2
            },
            {
                "text": "What is the difference between Deterministic and Stochastic effects?",
                "o1": "There is no difference.",
                "o2": "Deterministic has a threshold (burns); Stochastic is random probability (cancer).",
                "o3": "Deterministic is cancer; Stochastic is burns.",
                "o4": "Stochastic only affects bones.",
                "correct": 2
            },

            # PPE & PREGNANCY (Modules 5, 10)
            {
                "text": "How often should lead aprons be inspected for cracks and integrity?",
                "o1": "Once every 10 years.",
                "o2": "Annually (Once a year).",
                "o3": "Monthly.",
                "o4": "Never.",
                "correct": 2
            },
            {
                "text": "If a worker declares pregnancy, what is the dose limit for the fetus during the entire gestation?",
                "o1": "5,000 mrem",
                "o2": "500 mrem (approx 10% of the adult limit)",
                "o3": "0 mrem",
                "o4": "100 mrem",
                "correct": 2
            },

            # CT & MRI (Modules 14, 15)
            {
                "text": "Does a CT Scan deliver more or less radiation than a standard Chest X-ray?",
                "o1": "Less.",
                "o2": "Significantly more (100-500 times higher).",
                "o3": "About the same.",
                "o4": "CT uses sound waves, so zero radiation.",
                "correct": 2
            },
            {
                "text": "What is the single most important safety rule in MRI?",
                "o1": "Wear lead aprons.",
                "o2": "The Magnet is ALWAYS ON.",
                "o3": "Do not eat before the scan.",
                "o4": "Turn off the lights.",
                "correct": 2
            },
            {
                "text": "Why must ferromagnetic objects (oxygen tanks, scissors) be kept out of the MRI scanner room?",
                "o1": "They will melt.",
                "o2": "They become lethal projectiles due to the magnetic field.",
                "o3": "They cause static on the radio.",
                "o4": "They are too heavy.",
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

        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(questions)} questions (Modules 1-15 compliant)!"))