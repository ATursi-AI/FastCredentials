from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades O.R. Protocols to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Operating Room Protocols')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Perioperative Environment',
                    'content': """
                        <p>The Operating Room (O.R.) is a highly controlled, high-stakes environment where technical precision meets rigid safety standards. In 2026, the O.R. has evolved into the "Hybrid Suite"—integrating traditional surgery with advanced imaging and robotic systems. Perioperative safety is governed by the <strong>AORN Guidelines for Perioperative Practice</strong> and the <strong>Joint Commission (TJC)</strong> standards. This module establishes the three distinct zones of the surgical suite: 1. <strong>Unrestricted</strong> (Street clothes allowed). 2. <strong>Semi-Restricted</strong> (Scrub attire and hair covers required). 3. <strong>Restricted</strong> (The Sterile Field, requiring masks and full surgical attire).</p>
                        <p>The 2026 standard emphasizes <strong>Airflow Dynamics</strong> as a primary infection control measure. Modern O.R.s utilize "Laminar Airflow" systems that provide 20 to 30 air changes per hour, maintaining a positive pressure environment so that air flows <em>out</em> of the room when doors are opened, preventing outside contaminants from entering. As a professional, you must understand that "Door Traffic"—the unnecessary opening and closing of O.R. doors—disrupts this pressure and significantly increases the risk of <strong>Surgical Site Infections (SSI)</strong>. Your role is to minimize movement and maintain the integrity of the room's environmental barriers.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Restricted Zone includes the sterile field and requires masks and surgical attire.</li><li>Positive pressure and Laminar airflow are critical for maintaining room sterility.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Surgical Attire and Personal Hygiene',
                    'content': """
                        <p>In 2026, surgical attire is the first line of defense against the "Shedding" of human skin cells and bacteria. A single person sheds approximately 10 million skin particles per day, many of which carry <i>Staphylococcus aureus</i>. World-class attire protocols require that scrubs be facility-laundered (not brought from home) and tucked into the pants to prevent "bellowing" of skin cells. Hair covers (bouffant or surgical caps) must completely cover all hair, including sideburns and the nape of the neck. In 2026, "Skull Caps" that leave hair exposed are prohibited in most high-tier surgical centers due to the risk of particulate fallout.</p>
                        
                        <p>Personal hygiene in 2026 includes strict <strong>Jewelry and Grooming Standards</strong>. All jewelry, including rings, watches, and earrings, must be removed before entering the semi-restricted zone, as they harbor high concentrations of pathogens and can tear sterile gloves. Artificial nails and nail polish are strictly forbidden; they are known vectors for fungal and bacterial growth that cannot be reached by standard scrubbing. If you have any skin lesions, respiratory infections, or "weeping" wounds, you are ethically and legally obligated to report them to the O.R. manager, as you represent a significant bio-burden risk to the patient.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Scrubs must be facility-laundered and tucked to minimize skin cell shedding.</li><li>Artificial nails and all jewelry are strictly prohibited in the surgical suite.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Hand Hygiene and Surgical Scrubbing',
                    'content': """
                        <p>The 2026 surgical hand scrub is designed to remove transient flora and reduce resident flora to a minimum. There are two primary methods: the <strong>Traditional Brush Scrub</strong> (using Chlorhexidine Gluconate or Povidone-Iodine) and the <strong>Alcohol-Based Surgical Hand Rub</strong> (e.g., Avagard). For the first case of the day, a 3-to-5 minute brush scrub is often required to clean the subungual (under the nail) areas. For subsequent cases, alcohol-based rubs are the "2026 Gold Standard" as they are faster, more effective at sustained bacterial suppression, and cause less skin irritation.</p>
                        
                        <p>The "Physics of the Scrub" requires that you always keep your hands above your elbows. Gravity must allow the water and soap to flow from the cleanest area (the fingertips) to the less clean area (the elbows). If your hands drop below your waist or touch any non-sterile surface, you are contaminated and must restart the entire process. Once scrubbed and dried with a sterile towel, you must maintain the <strong>"Praying Position"</strong>—hands clasped in front of the chest, away from the body—until you are gowned and gloved. This "Constant Awareness" of hand position is what defines an O.R. professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Always keep hands above elbows to ensure water flows toward the non-sterile area.</li><li>Alcohol-based rubs are preferred for subsequent cases due to higher bacterial suppression.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Maintaining the Sterile Field',
                    'content': """
                        <p>The <strong>Sterile Field</strong> is the area immediately around the patient and the instrument tables. In 2026, the "Golden Rule" is: <strong>Sterile touches Sterile; Non-sterile touches Non-sterile.</strong> A sterile gown is only considered sterile from the chest to the level of the sterile field (table height) and from the cuffs to two inches above the elbows. The back of the gown, the armpits, and any area below the table level are considered "Contaminated." If you are scrubbed, you must never reach across a non-sterile area, and if you are non-scrubbed (circulating), you must never reach over the sterile field.</p>
                        <p>Movement around the field is strictly regulated to prevent <strong>Airborne Contamination</strong>. Non-scrubbed personnel must maintain a minimum distance of <strong>12 inches (1 foot)</strong> from the sterile field at all times. When two scrubbed individuals pass each other, they must pass "back-to-back" or "front-to-front" to minimize the risk of accidental contact with non-sterile areas. If a sterile drape is punctured, wet (strike-through), or if a non-sterile item touches it, the field is considered contaminated. In 2026, "Surgical Conscience" is the mandatory ethical standard: if you see a break in technique, you MUST speak up, even if it delays the start of the surgery.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The back of the surgical gown and the area below the table are always non-sterile.</li><li>Maintain at least 12 inches of distance from the sterile field if you are not scrubbed.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: O.R. Protocols Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
