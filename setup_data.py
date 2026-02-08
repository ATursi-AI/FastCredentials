import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Course, Question
from django.contrib.auth.models import User

def run():
    print("--- STARTING DATA SETUP ---")

    # 1. Create Superuser (so you can login)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@fastcredentials.com', 'password')
        print("CREATED ADMIN USER: (Username: admin / Password: password)")
    else:
        print("Admin user already exists.")

    # 2. Create the Course
    course, created = Course.objects.get_or_create(
        title="Bloodborne Pathogens (BBP) 2026",
        defaults={
            'description': "OSHA-compliant training for medical device representatives. Covers 29 CFR 1910.1030 standards for exposure control, PPE, and Hepatitis B.",
            'pass_score': 100
        }
    )
    print(f"COURSE READY: {course.title}")

    # 3. Clear old questions (to prevent duplicates) and Add New Ones
    course.questions.all().delete()
    
    questions_data = [
        {
            "text": "According to Universal Precautions, how should you treat human blood?",
            "o1": "Only as infectious if the patient is known to be sick.",
            "o2": "As if it is known to be infectious for HIV, HBV, and other bloodborne pathogens.",
            "o3": "Harmless unless it touches an open wound.",
            "o4": "Infectious only in the Operating Room.",
            "correct": 2,
            "exp": "Universal Precautions require treating ALL human blood and certain human body fluids as if they are known to be infectious."
        },
        {
            "text": "Which of the following is NOT an example of a sharp?",
            "o1": "Needles",
            "o2": "Scalpels",
            "o3": "Broken glass contaminated with blood",
            "o4": "Plastic tongue depressor",
            "correct": 4,
            "exp": "Sharps are objects that can penetrate the skin. A plastic tongue depressor is not a sharp."
        },
        {
            "text": "If you are exposed to blood (e.g., a splash to the eye or a needlestick), what is the FIRST thing you should do?",
            "o1": "Fill out an incident report.",
            "o2": "Wash the area with soap and water (or flush eyes with water) immediately.",
            "o3": "Find the nurse manager.",
            "o4": "Check the patient's chart.",
            "correct": 2,
            "exp": "Immediate washing reduces the risk of infection. Reporting comes second."
        },
        {
            "text": "The Hepatitis B Vaccine must be offered to employees who have occupational exposure:",
            "o1": "At a 50% discount.",
            "o2": "Only after they have been employed for 1 year.",
            "o3": "At no cost to the employee.",
            "o4": "Only if they are over 50 years old.",
            "correct": 3,
            "exp": "OSHA mandates that the Hepatitis B vaccination be made available at no cost to the employee."
        },
        {
            "text": "Which color or symbol indicates 'Biohazard' on a container?",
            "o1": "Blue containers.",
            "o2": "Fluorescent orange or orange-red containers with the biohazard symbol.",
            "o3": "Green bags.",
            "o4": "Clear plastic bags.",
            "correct": 2,
            "exp": "Red bags or orange-red containers with the biohazard symbol indicate regulated waste."
        },
        {
            "text": "When removing personal protective equipment (PPE), which item should be removed first?",
            "o1": "Mask",
            "o2": "Gown",
            "o3": "Gloves",
            "o4": "Shoe covers",
            "correct": 3,
            "exp": "Gloves are the most contaminated and should be removed first to avoid touching your face or other clean areas."
        },
        {
            "text": "How often is Bloodborne Pathogen training required by OSHA?",
            "o1": "Once upon hiring.",
            "o2": "Every 5 years.",
            "o3": "Annually (Every year).",
            "o4": "Only if an exposure occurs.",
            "correct": 3,
            "exp": "BBP training is required at the time of initial assignment and at least annually thereafter."
        },
        {
            "text": "What is the safest way to recap a needle?",
            "o1": "Use both hands to steady the cap.",
            "o2": "Never recap a needle unless using a mechanical device or the one-handed scoop technique.",
            "o3": "Ask a nurse to do it.",
            "o4": "Bend the needle before recapping.",
            "correct": 2,
            "exp": "Recapping is a major cause of needlesticks. It is prohibited unless strictly necessary and done with the one-handed technique."
        },
        {
            "text": "Which virus is most durable outside the body (can survive in dried blood for up to 7 days)?",
            "o1": "HIV",
            "o2": "Hepatitis B (HBV)",
            "o3": "Influenza",
            "o4": "Common Cold",
            "correct": 2,
            "exp": "Hepatitis B is highly resilient and can survive in dried blood on surfaces for at least a week."
        },
        {
            "text": "Hand hygiene (washing hands) should be performed:",
            "o1": "Only before putting gloves on.",
            "o2": "Only if hands are visibly dirty.",
            "o3": "Immediately after removing gloves.",
            "o4": "Before leaving the hospital only.",
            "correct": 3,
            "exp": "Gloves are not a substitute for hand washing. Hands must be washed immediately after gloves are removed."
        }
    ]

    for q in questions_data:
        Question.objects.create(
            course=course,
            text=q['text'],
            option_1=q['o1'],
            option_2=q['o2'],
            option_3=q['o3'],
            option_4=q['o4'],
            correct_option=q['correct'],
            explanation=q['exp']
        )
    
    print(f"SUCCESS: Added {len(questions_data)} questions to the database.")
    print("--- SETUP COMPLETE ---")

if __name__ == '__main__':
    run()