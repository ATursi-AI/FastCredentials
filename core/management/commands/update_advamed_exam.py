from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades AdvaMed Exam to 15 World-Class 2026 Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='AdvaMed Code of Ethics')
            course.questions.all().delete()

            qs = [
                ('What is the core philosophy of the 2026 AdvaMed Code?', 
                 ['Maximizing sales volume', 'Patient-Centricity: Decisions must be in the best interest of the patient', 'Lowering production costs', 'Avoiding all contact with doctors'], 2),
                
                ('Who is responsible for the ethical conduct of a "Channel Partner" (distributor)?', 
                 ['Only the distributor', 'The parent Medical Technology company is legally and ethically liable', 'The government', 'No one is responsible'], 2),
                
                ('What is "Fair Market Value" (FMV) in a consulting arrangement?', 
                 ['Paying whatever the doctor asks for', 'Compensation based on localized, data-driven benchmarks for expertise, not sales volume', 'A percentage of the sales the doctor generates', 'Free products in exchange for work'], 2),
                
                ('In 2026, can a company pay an HCP for "passive attendance" at a meeting?', 
                 ['Yes, if it\'s a long meeting', 'No, every dollar paid must correspond to a documented "Work Product"', 'Only if they are a key customer', 'Yes, for educational purposes'], 2),
                
                ('To whom must an educational grant be provided according to AdvaMed?', 
                 ['Directly to the individual HCP', 'To the institution or third-party organization, never an individual', 'To the HCP\'s spouse', 'To the local sales rep'], 2),
                
                ('What is the 2026 standard for "Business Meals"?', 
                 ['They must be modest, occasional, and in a setting conducive to business', 'They can be any price as long as the doctor is happy', 'They are strictly prohibited', 'They can only be at fast-food restaurants'], 1),
                
                ('In 2026, what is the policy regarding "Trinkets" like pens or mugs?', 
                 ['They are allowed if they have the logo', 'They are strictly prohibited', 'They are allowed if under $10', 'Only allowed for nurse stations'], 2),
                
                ('What is the value limit for a compliant "Educational Item" in 2026?', 
                 ['$500', '$100 (Fair Market Value)', '$25', 'There is no limit'], 2),
                
                ('What is the primary requirement for a Value-Based Care (VBC) risk-sharing contract?', 
                 ['It must be based on sales volume', 'It must be based on transparent, data-driven clinical outcomes', 'It must be a secret agreement', 'It only applies to small hospitals'], 2),
                
                ('How long is a "reasonable" evaluation period for capital equipment?', 
                 ['One year', 'Typically 30 to 90 days with a written agreement', 'Indefinitely', 'As long as the hospital wants it'], 2),
                
                ('What does the "Sunshine Act" (Open Payments) require companies to do?', 
                 ['Install solar panels', 'Publicly report all financial "Transfers of Value" made to HCPs', 'Provide free electricity to hospitals', 'Give a 10% discount to all doctors'], 2),
                
                ('In 2026, are Nurse Practitioners (NPs) and PAs included in Sunshine Act reporting?', 
                 ['No, only doctors', 'Yes, they are now fully included in the reporting requirements', 'Only if they work in surgery', 'Only in certain states'], 2),
                
                ('Which department should approve all charitable donations in a world-class company?', 
                 ['The Sales Team', 'The Compliance or Legal Department', 'The Marketing Manager', 'The CEO only'], 2),
                
                ('What is "Quid Pro Quo" in the context of AdvaMed?', 
                 ['A type of medical device', 'An improper exchange of "this for that" (e.g., a donation in exchange for a sale)', 'A legal term for a contract', 'A standard of excellence'], 2),
                
                ('What is the role of a "Whistleblower Hotline" in a compliance program?', 
                 ['To report late coworkers', 'To allow for the reporting of unethical behavior without fear of retaliation', 'To order supplies', 'To talk to the CEO'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: AdvaMed Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
