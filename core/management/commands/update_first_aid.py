from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Updates Standard First Aid to 2026 World-Class Standards'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Standard First Aid')
            Lesson.objects.filter(course=course).delete()
            Question.objects.filter(course=course).delete()

            lessons = [
                {'order': 1, 'title': "Module 1: What's New for 2026", 'content': '<h3>The 2026 Standard</h3><p>Good Samaritan laws now protect Naloxone/Epi-Pen use. Life-threatening bleeding is the #1 priority.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Narcan/Epi use is legally protected.</li><li>Stop the bleed first.</li></ul></div>'},
                {'order': 2, 'title': 'Module 2: Major Bleeding', 'content': '<h3>Tourniquets 2.0</h3><p>Apply 2-3 inches above the wound. Tighten until bleeding stops.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>High and tight (2-3 inches above).</li><li>Stop the flow completely.</li></ul></div>'},
                {'order': 3, 'title': 'Module 3: Shock', 'content': '<p>Lie flat, keep warm. No food/water.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Flat and warm.</li></ul></div>'},
                {'order': 4, 'title': 'Module 4: Burns', 'content': '<p>Cool with running water for 10+ mins. No ice.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>10 mins cool water.</li></ul></div>'},
                {'order': 5, 'title': 'Module 5: R.I.C.E.', 'content': '<p>Rest, Ice, Compression, Elevation.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>R.I.C.E. sequence.</li></ul></div>'},
                {'order': 6, 'title': 'Module 6: Spine Safety', 'content': '<p>Minimize movement. Keep head still.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Manual stabilization.</li></ul></div>'},
                {'order': 7, 'title': 'Module 7: Stroke (F.A.S.T.)', 'content': '<p>Face, Arm, Speech, Time.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>F.A.S.T. signs.</li></ul></div>'},
                {'order': 8, 'title': 'Module 8: Diabetes', 'content': '<p>Sugar only if conscious/swallowing.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Conscious sugar only.</li></ul></div>'},
                {'order': 9, 'title': 'Module 9: Seizures', 'content': '<p>Protect head. Nothing in mouth.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>No mouth objects.</li></ul></div>'},
                {'order': 10, 'title': 'Module 10: Environmental', 'content': '<p>Heat stroke: cool immediately. Hypothermia: warm slowly.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cool heat stroke fast.</li></ul></div>'},
                {'order': 11, 'title': 'Module 11: Anaphylaxis', 'content': '<p>Epi-Pen in outer thigh. Call 911.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Outer thigh; call 911.</li></ul></div>'},
                {'order': 12, 'title': 'Module 12: Narcan', 'content': '<p>Naloxone for opioid overdose.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Narcan for overdoses.</li></ul></div>'},
            ]
            for l in lessons: Lesson.objects.create(course=course, **l)

            qs = [
                ('Priority for spurting blood?', ['Pulse', 'Pressure/Tourniquet', 'Airway', 'Head injury'], 2),
                ('Tourniquet placement?', ['On wound', '2-3 inches above', 'On joint', 'Below wound'], 2),
                ('Shock treatment?', ['Water', 'Warm and Flat', 'Sit up', 'Snack'], 2),
                ('Cool a thermal burn?', ['Ice', 'Cool water (10m)', 'Butter', 'Freezing water'], 2),
                ('R.I.C.E stands for?', ['Run/Ice', 'Rest/Ice/Compression/Elevation', 'Rest/Insulin', 'Reaction/Ice'], 2),
                ('Spine head handling?', ['Straighten', 'Hold still', 'Pillow', 'Move to check'], 2),
                ('F.A.S.T stands for?', ['Feet/Arms', 'Face/Arm/Speech/Time', 'Faint/Ache', 'Face/Airway'], 2),
                ('Give sugar if?', ['Unconscious', 'Conscious/Swallowing', 'Nauseous', 'Sleeping'], 2),
                ('Seizure priority?', ['Hold down', 'Spoon in mouth', 'Clear area/Protect head', 'CPR'], 3),
                ('Heat Stroke signs?', ['Sweating', 'Hot/Dry and Confused', 'Shivering', 'Headache'], 2),
                ('Epi-Pen location?', ['Arm', 'Outer Thigh', 'Stomach', 'Neck'], 2),
                ('After Epi-Pen?', ['Sleep', 'Call 911', 'Drink water', 'Go home'], 2),
                ('Opioid reversal?', ['Aspirin', 'Naloxone', 'Epinephrine', 'Glucose'], 2),
                ('Remove helmet if?', ['Always', 'Airway blocked', 'Motorcycle only', 'Police ask'], 2),
                ('Flush chemical burn?', ['5 mins', '20+ mins', 'Stop pain', 'No water'], 2),
            ]
            for q, o, c in qs: 
                Question.objects.create(course=course, text=q, option_1=o[0], option_2=o[1], option_3=o[2], option_4=o[3], correct_option=c)

            self.stdout.write(self.style.SUCCESS('SUCCESS: 12 Modules and 15 Questions uploaded for First Aid.'))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course "Standard First Aid" not found.'))
