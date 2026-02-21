from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades BLS Exam to 15 World-Class Clinical Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Healthcare BLS (Basic Life Support)')
            course.questions.all().delete()

            qs = [
                ('What is the 2026 clinical goal for Chest Compression Fraction (CCF)?', 
                 ['At least 50%', 'At least 60%', 'At least 80%', '100%'], 3),
                
                ('In a High-Performance Team, what is "Closed-Loop Communication"?', 
                 ['Talking only to the leader', 'Repeating an order back and confirming when it is finished', 'Using hand signals only', 'Writing orders on a whiteboard'], 2),
                
                ('What does an EtCO2 reading of LESS than 10 mmHg indicate during CPR?', 
                 ['ROSC is occurring', 'Compressions are of poor quality and need improvement', 'The patient is breathing on their own', 'The AED is charging'], 2),
                
                ('What is the compression-to-ventilation ratio for 2-Rescuer PEDIATRIC BLS?', 
                 ['30:2', '15:2', '3:1', 'Continuous breaths'], 2),
                
                ('When a patient has an ADVANCED AIRWAY, what is the ventilation rate?', 
                 ['1 breath every 2 seconds', '1 breath every 6 seconds (10/min)', '1 breath every 10 seconds', '30:2 ratio'], 2),
                
                ('What is the compression-to-ventilation ratio for NEONATAL resuscitation?', 
                 ['15:2', '30:2', '3:1', '10:1'], 3),
                
                ('At what heart rate should you begin CPR on a pediatric patient with signs of poor perfusion?', 
                 ['Below 100 bpm', 'Below 60 bpm', 'Only if there is no pulse', 'Below 40 bpm'], 2),
                
                ('Where should you move oxygen sources before discharging a defibrillator shock?', 
                 ['At least 1 foot away', 'At least 3 feet away', 'Into the hallway', 'No need to move it'], 2),
                
                ('What is the 2026 "PEP Window" for starting Naloxone in a suspected overdose?', 
                 ['Give it immediately but do not delay starting CPR', 'Wait for a pulse check', 'Give only if the patient is breathing', 'Wait for ALS to arrive'], 1),
                
                ('What modification is required for a pregnant patient (>20 weeks) during CPR?', 
                 ['Tilt the whole bed to the right', 'Manual Lateral Uterine Displacement (LUD) to the left', 'Put a pillow under her head', 'No modifications required'], 2),
                
                ('What is the 2026 standard for drowning resuscitation?', 
                 ['Start with 100 compressions', 'Provide 5 initial rescue breaths before starting compressions', 'Drain the water from the lungs first', 'Wait for the patient to cough'], 2),
                
                ('When should you perform a "Blind Finger Sweep" on a choking victim?', 
                 ['Always, to find the object', 'Only on infants', 'Never, as it can push the object deeper', 'Only if the patient is conscious'], 3),
                
                ('What energy waveform is the 2026 standard for healthcare defibrillators?', 
                 ['Monophasic', 'Biphasic', 'Triphasic', 'Direct Current'], 2),
                
                ('If a valid DNR/POLST form is produced during a code, what must you do?', 
                 ['Finish the current cycle of CPR', 'Stop resuscitation efforts immediately', 'Wait for the doctor to call it', 'Ignore it if the family is crying'], 2),
                
                ('What is the "Two-Thumb Encircling Hands" technique used for?', 
                 ['Adult choking', 'Neonatal chest compressions', 'Opening the airway', 'Moving a patient'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: BLS Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
