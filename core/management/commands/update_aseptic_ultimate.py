from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Aseptic Technique to 12 Deep-Dive 2026 World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Aseptic Technique')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: Sterile vs. Aseptic: The 2026 Distinction',
                    'content': """
                        <p>In 2026, healthcare professionals must distinguish between <strong>Sterile Technique</strong> and <strong>Aseptic Technique</strong>. Sterility is an absolute state: the total absence of all living microorganisms and spores. Aseptic technique, however, is a <em>process</em> designed to prevent the introduction of pathogens into a vulnerable area. While "Sterile" is used for major surgery, "Aseptic" is the standard for peripheral IV starts, urinary catheterization, and wound care. The 2026 goal is <strong>Asepsis</strong>—the state of being free from disease-causing contaminants.</p>
                        <p>The 2026 standard is built on the <strong>ANTT® (Aseptic Non-Touch Technique)</strong> framework. This framework classifies procedures as either "Standard ANTT" (simple, short procedures) or "Surgical ANTT" (complex, long-duration procedures). The core philosophy of ANTT is that you only need to maintain the "Key Parts" and "Key Sites" as sterile. For example, during an IV start, the "Key Site" is the puncture point on the skin, and the "Key Part" is the needle tip. By focusing your technical precision on these specific micro-boundaries, you reduce the risk of Healthcare-Associated Infections (HAIs) by over 40% compared to traditional, less-defined methods.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Sterile is an absolute state; Aseptic is a process to maintain asepsis.</li><li>ANTT® focuses on protecting "Key Parts" and "Key Sites" during a procedure.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Biofilms and the Science of Contamination',
                    'content': """
                        <p>In 2026, the primary enemy of aseptic technique is the <strong>Biofilm</strong>. A biofilm is a complex colony of bacteria that adheres to surfaces (like catheters or implants) and secretes a protective, slimy matrix. Once a biofilm forms, the bacteria inside are up to 1,000 times more resistant to antibiotics and disinfectants than "free-floating" bacteria. Aseptic technique is designed to prevent the initial "attachment phase" of these bacteria. If even a single bacterium reaches a "Key Part" (like a heart valve or an orthopedic screw), it can establish a biofilm that leads to chronic, non-treatable infection.</p>
                        
                        <p>Contamination occurs through three primary routes: <strong>Airborne</strong> (dust and skin cells), <strong>Contact</strong> (touching a non-sterile surface), and <strong>Self-Inoculation</strong> (pathogens from the patient's own skin). 2026 research shows that the patient's own skin flora is the source of 80% of surgical site infections. This is why "Skin Antisepsis" with 2% Chlorhexidine Gluconate (CHG) in 70% Alcohol is the mandatory 2026 standard. The CHG provides "Residual Kill Power," staying active on the skin for up to 48 hours after application, preventing bacteria from migrating back into the wound or puncture site.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Biofilms make bacteria 1,000x more resistant; prevention is the only effective cure.</li><li>CHG with Alcohol is the 2026 skin-prep standard due to its 48-hour residual effect.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: The "Key Part" Protection Rule',
                    'content': """
                        <p>The 2026 "Key Part" rule is the cornerstone of aseptic safety. A <strong>Key Part</strong> is any component of the medical equipment that, if contaminated, will directly infect the patient. This includes the tip of a syringe, the inside of a needle hub, the surface of a sterile dressing, and the ends of IV tubing. In Standard ANTT, you do not necessarily need a "Full Sterile Field" or sterile gloves, provided you can <strong>ensure you never touch a Key Part</strong>. If you cannot perform the task without touching the Key Part (e.g., during complex wound packing), you MUST transition to Surgical ANTT and wear sterile gloves.</p>
                        
                        <p>Handling sterile items requires "Point-to-Point" awareness. When opening a sterile package, the 1-inch border around the edge of the wrapper is considered <strong>Non-Sterile</strong>. You must peel the package open so that the sterile item "drops" onto the sterile field without touching the non-sterile edges. If a Key Part touches the 1-inch border, it is contaminated. In 2026, we utilize the "Shadow Shield" concept—positioning your body and hands so that you are never reaching over a Key Part, as microscopic dust and skin cells from your arms can fall onto the sterile surface and compromise the procedure.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A "Key Part" is any item that directly enters or contacts the patient's sterile system.</li><li>The 1-inch border of a sterile wrapper is always considered non-sterile.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Environmental Asepsis and "Air-Shedding"',
                    'content': """
                        <p>Aseptic technique is not performed in a vacuum; the environment plays a critical role. In 2026, we monitor for <strong>Air-Shedding</strong>—the release of particulates from human movement. Every time you walk quickly, wave your arms, or talk loudly, you increase the "Bio-Burden" in the air. For high-risk aseptic procedures (like spinal taps or central line insertions), the room must be in a "Low-Traffic" state. Doors must be closed, and unnecessary personnel must be removed. Talking should be kept to a minimum to prevent "Droplet Spread" from the mouth and nose.</p>
                        <p>Surface disinfection in 2026 utilizes <strong>"Kill-Time" Verification</strong>. You must know the difference between "cleaning" and "disinfecting." Before setting up a "Plastic-Backed Sterile Field" on a bedside table, the surface must be cleaned with an EPA-registered disinfectant and allowed to stay wet for the full manufacturer-recommended contact time (usually 1–3 minutes for modern wipes). If you place a sterile drape on a damp surface that hasn't finished its kill-time, "Strike-Through" contamination can occur, where moisture wicks bacteria from the table through the drape and onto your sterile instruments.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Minimize movement and talking to reduce "Air-Shedding" near sterile sites.</li><li>Ensure "Kill-Time" is complete on surfaces before placing sterile drapes to prevent strike-through.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Aseptic Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
