from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Radiation Safety to 12 Deep-Dive 2026 World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Radiation Safety')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Physics of Ionizing Radiation',
                    'content': """
                        <p>Ionizing radiation is energy in the form of waves or particles that has enough power to remove electrons from atoms, creating "ions." In the 2026 clinical environment, we primarily deal with <strong>X-rays</strong> and <strong>Gamma rays</strong>. Unlike non-ionizing radiation (like radio waves or microwaves), ionizing radiation can break chemical bonds within human DNA. This damage is the root cause of both "Deterministic" effects (immediate damage like radiation burns) and "Stochastic" effects (long-term risks like cancer). Understanding that radiation is invisible, odorless, and silent is the first step toward the "Zero Exposure" mindset required for surgical and radiological professionals.</p>
                        <p>In 2026, we measure radiation using three primary units: <strong>Roentgen (R)</strong> for exposure in the air, <strong>Rad/Gray (Gy)</strong> for the absorbed dose in tissue, and the <strong>Rem/Sievert (Sv)</strong> for the "dose equivalent" which accounts for the biological impact on specific organs. For the O.R. professional, the Sievert is the most critical metric. The 2026 NRC occupational limit for whole-body exposure is 5 Rem (50 mSv) per year, but world-class facilities aim for a much lower "Action Level." By understanding the "Inverse Square Law"—where doubling your distance from the source reduces your exposure to one-fourth—you gain the primary physical tool for self-protection without the need for heavy equipment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Ionizing radiation can break DNA bonds, leading to cancer or tissue damage.</li><li>The Inverse Square Law is your most effective protection: Distance = Safety.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The ALARA Principle in 2026',
                    'content': """
                        <p>The cornerstone of 2026 radiation safety is <strong>ALARA: As Low As Reasonably Achievable</strong>. This is not just a guideline; it is a regulatory requirement. ALARA assumes that there is no "safe" threshold for radiation exposure and that every mrem of exposure carries some risk. In 2026, the application of ALARA is built on the "Three Pillars of Protection": <strong>Time, Distance, and Shielding</strong>. 1. <strong>Time</strong>: Minimize the time spent near the source (e.g., using "Pulse Fluoroscopy" instead of continuous beam). 2. <strong>Distance</strong>: Maintain the maximum distance possible from the X-ray tube. 3. <strong>Shielding</strong>: Always use lead aprons, thyroid shields, and leaded glass barriers.</p>
                        
                        <p>A 2026 update to ALARA is the <strong>"Digital ALARA"</strong> approach. This involves using AI-enhanced imaging software that can produce high-resolution images with significantly lower radiation doses (dose reduction technology). As a professional, you have an ethical duty to advocate for the lowest dose possible for both the patient and the staff. "Good enough" imaging at a lower dose is always superior to "perfect" imaging at a lethal or high-accumulated dose. In 2026, we also focus on "Repeat Avoidance"—ensuring the patient is positioned correctly the first time to avoid the 100% increase in dose that comes from a second "take."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>ALARA means there is no safe dose; keep exposure at the absolute minimum.</li><li>The three pillars are Time (brief), Distance (far), and Shielding (lead).</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Scatter Radiation and the C-Arm',
                    'content': """
                        <p>In the Operating Room, the primary source of radiation exposure to staff is not the direct beam, but <strong>Scatter Radiation</strong>. When the X-ray beam hits the patient, the photons "bounce" or scatter in all directions, similar to light hitting a mirror. In 2026, we utilize <strong>Real-Time Scatter Visualization</strong> software that shows the team the "invisible cloud" of radiation in the room. The highest intensity of scatter radiation is found on the side of the patient where the X-ray tube is located. Therefore, standing on the "Image Intensifier" (receiver) side of the table is significantly safer than standing on the "Tube" side.</p>
                        
                        <p>Safe <strong>C-Arm Positioning</strong> in 2026 follows the "Under-Table" rule. Whenever possible, the X-ray tube should be positioned <em>under</em> the patient table with the image intensifier above. This ensures that the majority of scatter radiation is directed toward the floor rather than toward the heads and necks of the surgical team. If the C-arm must be used in a lateral (side) position, the staff should stand on the side of the intensifier. Understanding the "Scatter Geography" of your O.R. allows you to position yourself in "Cold Zones" where the radiation flux is at its lowest, even during high-dose fluoroscopy procedures.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Scatter radiation from the patient is the #1 source of staff exposure.</li><li>Always position the X-ray tube under the table to direct scatter toward the floor.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Personal Dosimetry and 2026 Tracking',
                    'content': """
                        <p>A <strong>Dosimeter</strong> is a personal monitoring device that measures the accumulated dose of ionizing radiation. In 2026, the standard is the <strong>OSL (Optically Stimulated Luminescence)</strong> dosimeter or the "Active Digital Dosimeter." Unlike older film badges, these devices are highly resistant to heat and moisture and provide more accurate readings for low-energy scatter. For O.R. personnel, the dosimeter must be worn <strong>at the collar, outside of the lead apron</strong>. This measures the dose to the most sensitive, unshielded parts of the body: the lens of the eye and the thyroid gland.</p>
                        <p>In 2026, many facilities use <strong>Real-Time Dosimetry Systems</strong> that provide an audible "chirp" or a visual display of the current dose rate. This allows the professional to adjust their distance or position <em>during</em> the procedure if the dose becomes too high. You are strictly prohibited from "sharing" a dosimeter or leaving it in the O.R. when not in use, as this will result in an inaccurate legal record of your exposure. Your dose history is a permanent legal record that follows you throughout your career. In 2026, the "Dose-to-Cloud" sync ensures that your total cumulative lifetime dose is monitored to prevent long-term stochastic risks.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Wear your dosimeter at the collar, outside the lead apron.</li><li>Real-time dosimeters provide immediate feedback to help you move to safer zones.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Radiation Safety Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
