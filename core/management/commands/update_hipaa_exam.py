from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades HIPAA Exam to 15 World-Class 2026 Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='HIPAA Patient Confidentiality')
            course.questions.all().delete()

            qs = [
                ('What is the February 16, 2026, deadline regarding HIPAA compliance?', 
                 ['Finalizing all paper shredding', 'Updating the Notice of Privacy Practices (NPP) and 42 CFR Part 2 alignment', 'Hiring a new IT manager', 'Switching to paper records'], 2),
                
                ('In 2026, how many days does a provider have to fulfill a patient\'s request for medical records?', 
                 ['30 days', '60 days', '15 days', '5 days'], 3),
                
                ('What is "Minimum Necessary" in the context of HIPAA PHI access?', 
                 ['Accessing only the smallest amount of data required to do your specific job', 'Using a small font on medical forms', 'Talking in a whisper', 'Only keeping records for 1 year'], 1),
                
                ('Which of these is considered one of the 18 HIPAA identifiers?', 
                 ['State of residence', 'IP Address and Full-face photographs', 'General age (over 89)', 'Type of medical insurance'], 2),
                
                ('What is the "Safe Harbor" for a lost or stolen laptop in 2026?', 
                 ['Reporting it within a year', 'The laptop was unencrypted but in a locked car', 'The data on the laptop was fully encrypted to NIST standards', 'The laptop was old'], 3),
                
                ('How are Substance Use Disorder (SUD) records (42 CFR Part 2) handled in 2026?', 
                 ['They are treated exactly like regular PHI with no extra protection', 'They have heightened protections and generally cannot be used in court against the patient without consent', 'They are public record', 'They must be deleted after 30 days'], 2),
                
                ('Under the 2026 Reproductive Health Privacy Rule, can you share PHI with law enforcement for the purpose of investigating lawful medical care?', 
                 ['Yes, always', 'Only if the officer is friendly', 'No, HIPAA now provides a Federal Privacy Shield for lawful reproductive health data', 'Only in certain states'], 3),
                
                ('What is required before sharing sensitive health data with an administrative or law enforcement body in 2026?', 
                 ['A verbal agreement', 'A signed Attestation stating the request is for a permitted purpose', 'A copy of the patient\'s ID', 'Nothing is required'], 2),
                
                ('In 2026, what is the mandatory security requirement for any system accessing ePHI?', 
                 ['A long password', 'Multi-Factor Authentication (MFA)', 'A specialized mouse', 'A private office'], 2),
                
                ('How often should a Business Associate Agreement (BAA) be reviewed in 2026?', 
                 ['Every 10 years', 'Annually or when technology/regulations change', 'Only after a breach', 'BAAs are no longer required'], 2),
                
                ('What is the internal reporting timeline for a suspected PHI breach in a 2026 world-class organization?', 
                 ['24 hours', '60 days', 'One week', 'When you have time'], 1),
                
                ('What is "Internal Snooping" in a healthcare facility?', 
                 ['Cleaning the patient rooms', 'Accessing the records of friends, celebrities, or coworkers out of curiosity', 'Repairing the EHR system', 'Looking for a patient\'s room number for a delivery'], 2),
                
                ('According to the 2026 NIST standard, how should paper PHI be disposed of?', 
                 ['Recycling bin', 'Trash can with a lid', 'Shredding (cross-cut), burning, or pulping', 'Tearing it in half'], 3),
                
                ('Which body fluid is NOT considered an infection risk unless it contains visible blood?', 
                 ['Saliva', 'Sweat', 'Vomitus', 'Cerebrospinal fluid'], 2),
                
                ('What is the "Accounting of Disclosures" patients can request?', 
                 ['A bill for their services', 'A list of all medical treatments received', 'A 6-year history of everyone who saw their PHI for purposes outside of Treatment, Payment, or Operations', 'A list of their prescriptions'], 3)
            ]

            for text, options, correct in qs:
                Question.objects.create(
                    course=course,
                    text=text,
                    option_1=options[0],
                    option_2=options[1],
                    option_3=options[2],
                    option_4=options[3],
                    correct_option=correct
                )

            self.stdout.write(self.style.SUCCESS('SUCCESS: HIPAA 2026 Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
