from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Updates Standard CPR / AED to 2026 World-Class Standards'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Standard CPR / AED')
            Lesson.objects.filter(course=course).delete()
            Question.objects.filter(course=course).delete()

            lessons = [
                {'order': 1, 'title': 'The Chain of Survival (2026 Update)', 'content': '<p>The Chain of Survival represents the sequential actions that increase survival rates. The 2026 standard utilizes a <strong>6-link chain</strong>: 1. Early Recognition, 2. High-Quality CPR, 3. Rapid Defibrillation, 4. Advanced Resuscitation, 5. Post-Arrest Care, 6. <strong>Recovery</strong>.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>There are 6 links in the modern Chain of Survival.</li><li>Recovery is the newest link, focusing on long-term rehabilitation.</li></ul></div>'},
                {'order': 2, 'title': 'Safety, PPE, and Scene Assessment', 'content': '<p>Your safety is the priority. Use Universal Precautions (gloves/masks). If the scene is unsafe, do not enter. If you are uncomfortable with breaths, <strong>Hands-Only CPR</strong> is highly effective for adults.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Check scene safety before approaching.</li><li>Always use a barrier device if providing rescue breaths.</li></ul></div>'},
                {'order': 3, 'title': 'Assessing the Victim', 'content': '<p>Use the "Tap and Shout" method. Check for normal breathing (no more than 10 seconds). <strong>Agonal gasps are not normal breathing</strong>—treat them as cardiac arrest.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Agonal gasps = Start CPR immediately.</li><li>Point to a specific bystander to call 911/get an AED.</li></ul></div>'},
                {'order': 4, 'title': 'Chest Compressions (The Engine)', 'content': '<p>Depth: 2 to 2.4 inches (5-6 cm). Rate: 100-120 beats per minute. Allow for <strong>full chest recoil</strong> between compressions to let the heart refill.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Depth: 2-2.4 inches.</li><li>Rate: 100-120 BPM.</li></ul></div>'},
                {'order': 5, 'title': 'Rescue Breaths and 30:2 Ratio', 'content': '<p>The ratio for all single rescuers is <strong>30 compressions to 2 breaths</strong>. Use the Head-Tilt/Chin-Lift to open the airway. Deliver breaths over 1 second until the chest rises.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Ratio: 30:2 for adults.</li><li>Avoid excessive ventilation (don’t blow too hard).</li></ul></div>'},
                {'order': 6, 'title': 'AED: The Only Reset', 'content': '<p>Turn the AED <strong>ON</strong> immediately. Follow voice prompts. Apply pads to bare skin. Stand clear during analysis and shock.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Step 1: Power ON the AED.</li><li>Do not touch the victim during analysis or shock delivery.</li></ul></div>'},
                {'order': 7, 'title': 'The Recovery Position', 'content': '<p>If a victim is <strong>unresponsive but breathing</strong>, place them in the Lateral Recovery Position to keep the airway clear and prevent aspiration.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use the Recovery Position for breathing, unconscious victims.</li></ul></div>'},
                {'order': 8, 'title': 'Opioid Overdose and Naloxone', 'content': '<p>Opioid overdoses can mimic cardiac arrest. Administer <strong>Naloxone (Narcan)</strong> nasal spray if suspected. Do not delay CPR for Narcan administration.</p><div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Naloxone reverses opioid-induced respiratory depression.</li></ul></div>'},
            ]
            for l in lessons: Lesson.objects.create(course=course, **l)

            qs = [
                ('How many links are in the 2026 Chain of Survival?', ['4', '5', '6', '10'], 3),
                ('What is the correct depth of adult compressions?', ['1 inch', '2 to 2.4 inches', '3 inches', '4 inches'], 2),
                ('What is the first step when using an AED?', ['Apply pads', 'Press shock', 'Power on the device', 'Clear the victim'], 3),
                ('What should you do if a victim is gasping (Agonal Breaths)?', ['Wait for normal breathing', 'Start CPR immediately', 'Give water', 'Check for 2 minutes'], 2),
                ('What is the compression rate for all victims?', ['60-80 BPM', '100-120 BPM', '140-160 BPM', 'As slow as possible'], 2),
                ('If a victim is breathing but unconscious, you should use:', ['CPR', 'Abdominal thrusts', 'The Recovery Position', 'The AED'], 3),
                ('Where should an adult AED pad be placed?', ['On the stomach', 'Upper right chest and lower left side', 'Both on the back', 'On the neck'], 2),
                ('What is the ratio of compressions to breaths for adult CPR?', ['15:2', '30:2', '5:1', '100:0'], 2),
                ('What drug reverses an opioid overdose?', ['Aspirin', 'Naloxone (Narcan)', 'Insulin', 'Epinephrine'], 2),
                ('Why is full chest recoil important?', ['It looks better', 'It allows the heart to refill with blood', 'It saves energy', 'It prevents broken ribs'], 2),
            ]
            for q, o, c in qs:
                Question.objects.create(course=course, text=q, option_1=o[0], option_2=o[1], option_3=o[2], option_4=o[3], correct_option=c)

            self.stdout.write(self.style.SUCCESS("SUCCESS: Standard CPR / AED course updated."))
        except Course.DoesNotExist:
             self.stdout.write(self.style.ERROR("Course not found."))
