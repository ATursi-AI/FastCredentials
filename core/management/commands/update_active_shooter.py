from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Updates Active Shooter Preparedness to 2026 World-Class Standards'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Active Shooter Preparedness')
            Lesson.objects.filter(course=course).delete()
            Question.objects.filter(course=course).delete()

            lessons = [
                {'order': 1, 'title': 'Module 1: The Run, Hide, Fight Protocol', 'content': '<p>The FBI-endorsed standard for survival. <strong>RUN:</strong> Have an escape route and leave belongings. <strong>HIDE:</strong> Lock and blockade doors; silence phones. <strong>FIGHT:</strong> As a last resort, act with absolute aggression to incapacitate the shooter.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The protocol is non-linear; choose the best option for your location.</li><li>Silence your cell phone <strong>completely</strong> (no vibrate).</li></ul></div>'},
                {'order': 2, 'title': 'Module 2: Advanced Barricading Techniques', 'content': '<p>If a door opens inward, use heavy furniture. If it opens <strong>outward</strong>, furniture is ineffective. Use a belt or power cord to secure the door handle to a fixed object, or use a door wedge.</p>[Image of outward opening door barricade using a belt]<div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Furniture only works for inward-opening doors.</li><li>Use belts or cords for outward-opening doors.</li></ul></div>'},
                {'order': 3, 'title': 'Module 3: Situational Awareness & Indicators', 'content': '<p>Recognizing "Pre-Attack Indicators" such as "leakage" (sharing intent) or sudden changes in behavior. If you see something, say something.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>"Leakage" is the communication of intent to a third party.</li><li>Situational awareness means knowing at least two exits at all times.</li></ul></div>'},
                {'order': 4, 'title': 'Module 4: Interacting with Law Enforcement', 'content': '<p>Officers will not stop to help victims until the threat is neutralized. <strong>Keep hands visible and empty at all times.</strong> Do not point or scream at officers.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Hands must be visible and fingers spread.</li><li>Do not grab or approach officers for help.</li></ul></div>'},
                {'order': 5, 'title': 'Module 5: Stop the Bleed (Ballistic Trauma)', 'content': '<p>Ballistic injuries cause rapid blood loss. Use direct pressure or a <strong>Tourniquet</strong> (2-3 inches above the wound). Wound pack for junctional areas (groin/shoulder).</p>[Image of tourniquet application for a gunshot wound]<div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Bleeding is the #1 cause of preventable death.</li><li>Apply tourniquets "High and Tight" above the wound.</li></ul></div>'},
            ]
            for l in lessons: Lesson.objects.create(course=course, **l)

            qs = [
                ('What is the first and best option if an escape path is clear?', ['Hide', 'Fight', 'Run', 'Wait for police'], 3),
                ('When hiding, what should you do with your cell phone?', ['Put it on vibrate', 'Keep it on loud to hear 911', 'Turn it off or silence it completely', 'Call your family immediately'], 3),
                ('How do you secure a door that opens OUTWARD?', ['Blockade it with a desk', 'Use a belt or cord to secure the handle', 'Lean against it', 'Open it slightly'], 2),
                ('When Law Enforcement arrives, what should your hands look like?', ['In your pockets', 'Visible and empty with fingers spread', 'Holding your ID', 'Pointing at the shooter'], 2),
                ('What is the #1 cause of preventable death in a shooting?', ['Lack of oxygen', 'Severe bleeding', 'Head injury', 'Shock'], 2),
                ('Where should a tourniquet be placed on a limb?', ['Directly on the wound', 'On the nearest joint', '2-3 inches above the wound', 'Below the wound'], 3),
                ('What is "Leakage" in the context of situational awareness?', ['A gas leak', 'The communication of intent to harm by a potential shooter', 'Information shared by the police', 'A door left propped open'], 2),
                ('If you are in a safe room, when should you come out?', ['When the fire alarm pulls', 'When you hear someone yell "Police!"', 'Only when explicitly cleared by identifiable officers', 'When the shooting stops'], 3),
                ('As a last resort, if you must "Fight," how should you act?', ['Try to talk the shooter down', 'With absolute aggression and improvised weapons', 'Wait for the shooter to reload', 'Hide behind a chair'], 2),
                ('Why should you NOT pull the fire alarm during a shooting?', ['It costs money', 'It draws people into the hallways (kill zone)', 'The police won\'t hear the gunshots', 'It might scare the shooter'], 2),
            ]
            for q, o, c in qs:
                Question.objects.create(course=course, text=q, option_1=o[0], option_2=o[1], option_3=o[2], option_4=o[3], correct_option=c)

            self.stdout.write(self.style.SUCCESS("SUCCESS: Active Shooter course updated."))
        except Course.DoesNotExist:
             self.stdout.write(self.style.ERROR("Course not found."))
