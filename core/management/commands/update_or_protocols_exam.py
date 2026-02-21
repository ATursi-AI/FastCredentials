from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades O.R. Protocols Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Operating Room Protocols')
            course.questions.all().delete()

            qs = [
                ('What is the function of "Positive Pressure" in the Operating Room?', 
                 ['To make the staff feel better', 'To ensure air flows OUT of the room when doors open, preventing contaminants from entering', 'To help the patient breathe', 'To keep the room warm'], 2),
                
                ('Which zone of the surgical suite requires full scrubs, hair covers, and masks?', 
                 ['Unrestricted Zone', 'Semi-Restricted Zone', 'Restricted Zone (The Sterile Field)', 'The Cafeteria'], 3),
                
                ('What is the "2026 Gold Standard" for hair covers in high-tier O.R.s?', 
                 ['A standard baseball cap', 'A bouffant or cap that completely covers all hair and the nape of the neck', 'A skull cap that leaves sideburns exposed', 'No hair cover is needed'], 2),
                
                ('Why is the "Closed Gloving" technique used during the initial gowning?', 
                 ['It is faster', 'To ensure the bare skin of the hands never touches the sterile exterior of the gown or gloves', 'To keep the hands warm', 'It is only used for orthopedic cases'], 2),
                
                ('Where is a surgical gown considered STERILE after it is donned?', 
                 ['The entire front and back of the gown', 'From the chest to the sterile field level and from the cuffs to 2 inches above the elbow', 'Only the sleeves', 'From the neck to the floor'], 2),
                
                ('What is the minimum distance non-scrubbed personnel must maintain from the sterile field?', 
                 ['6 inches', '12 inches (1 foot)', '3 feet', '5 feet'], 2),
                
                ('What is a "Surgical Time-Out" according to 2026 standards?', 
                 ['A 15-minute coffee break', 'A mandatory "Hard Stop" before incision to verify patient, site, and procedure', 'The time spent cleaning the room', 'A period where the surgeon talks to the family'], 2),
                
                ('In 2026, why is Surgical Smoke (Plume) considered a major biohazard?', 
                 ['It smells bad', 'It contains aerosolized viruses, chemicals, and carcinogens equivalent to smoking 27-30 cigarettes', 'It makes the room too foggy', 'It interferes with the robotic sensors'], 2),
                
                ('Where must a smoke evacuator nozzle be placed to be effective?', 
                 ['Near the ceiling vent', 'Within 2 inches of the surgical site', 'Outside the O.R. door', 'Attached to the anesthesia machine'], 2),
                
                ('What is the 2026 protocol for "IUSS" (flash sterilization)?', 
                 ['It is the preferred method for all trays', 'It should only be used in emergency situations where no backup is available', 'It is only for plastic instruments', 'It is no longer legal in any state'], 2),
                
                ('What must you check on an instrument tray BEFORE opening it onto the sterile field?', 
                 ['The price of the instruments', 'The internal Chemical Indicator (Class 5 or 6)', 'The name of the technician who cleaned it', 'The weight of the tray'], 2),
                
                ('What type of fire extinguisher is mandatory for O.R. fires?', 
                 ['Water or Foam', 'ABC Dry Chemical', 'CO2 (Carbon Dioxide)', 'A bucket of sand'], 3),
                
                ('What is "LUD" (Lateral Uterine Displacement) used for in an O.R. Code Blue?', 
                 ['To help the surgeon see better', 'To move the gravid uterus to the left to restore venous return during CPR', 'A type of robotic arm movement', 'To prevent patient snoring'], 2),
                
                ('How must scrubbed personnel pass each other in the O.R.?', 
                 ['They should never pass each other', 'Back-to-back or front-to-front', 'One must leave the room', 'They must crawl under the table'], 2),
                
                ('What is "Surgical Conscience"?', 
                 ['A type of medical textbook', 'An internal moral obligation to admit and correct any break in sterile technique', 'The surgeon\'s final decision on a case', 'A rule about O.R. music'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: O.R. Protocols Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
