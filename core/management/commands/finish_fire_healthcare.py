from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Healthcare Fire Safety with Modules 6-10 at World-Class Density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Fire Safety')
            
            lessons = [
                {
                    'order': 6,
                    'title': 'Module 6: Extension Cords, Power Strips, and UL 1363A',
                    'content': """
                        <p>Electrical fires in healthcare are frequently caused by the misuse of temporary power taps (power strips) and extension cords. In 2026, CMS and The Joint Commission have strict regulations: <strong>Extension cords are prohibited for permanent use.</strong> They are classified as "temporary" and must be removed immediately after a task is completed. Using an extension cord to power a piece of medical equipment permanently is a high-level fire code violation because these cords are prone to physical damage (being crushed by bed wheels or doors), which leads to arcing and ignition of floor coverings or bedding.</p>
                        <p>For power strips, healthcare facilities must use <strong>UL 1363A or UL 60601-1</strong> certified Special Purpose Relocatable Power Taps (SPRPT). Standard "home-use" power strips from a hardware store are strictly forbidden in the "Patient Care Vicinity" (within 6 feet of a patient bed). Standard strips lack the leakage current protections and robust grounding required for clinical environments. Furthermore, "Daisy-Chaining"—plugging one power strip into another—is a major fire hazard that causes circuit overload and heat buildup within the cords. You must ensure that every piece of equipment in the patient vicinity is plugged directly into a wall outlet or an approved healthcare-grade power tap with a medical-grade plug (marked with a green dot).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Only UL 1363A/60601-1 power strips are allowed in the patient care vicinity.</li><li>"Daisy-Chaining" power strips is a critical fire code violation.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Biomedical Equipment and Preventive Maintenance',
                    'content': """
                        <p>Biomedical equipment—from infusion pumps to ventilators—represents a significant electrical and fire load. In 2026, the <strong>Safe Medical Devices Act</strong> requires a rigorous Preventive Maintenance (PM) program. Every device used for patient care must be inspected by a Biomedical Equipment Technician (BMET) and must display a current inspection tag. Equipment that is overdue for inspection, or that shows any signs of physical damage (such as a frayed cord or a cracked casing), must be removed from service immediately ("Red Tagged") and sent for repair. Fires often start within these devices due to internal dust accumulation or component failure that goes unnoticed without regular testing.</p>
                        <p>Leakage current is a hidden fire and shock hazard. All biomedical equipment "leaks" a tiny amount of electricity to the chassis; if this current exceeds 100 microamperes in the patient care vicinity, it can be lethal. Modern 2026 testing involves <strong>Chassis Leakage and Lead Leakage</strong> checks to ensure the equipment's internal insulation has not degraded. As a professional, you are the first line of defense: before plugging in any device, perform a visual sweep for "Hot Spots" or the smell of ozone (a sharp, metallic scent), which indicates electrical arcing. By ensuring only "Green Dot" medical-grade plugs and recently inspected devices are used, you eliminate the primary ignition source for non-surgical healthcare fires.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>All medical equipment must have a current "PM" inspection tag.</li><li>Frayed cords or ozone smells are "immediate stop" indicators for medical devices.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Compressed Medical Gases and Oxidizer Safety',
                    'content': """
                        <p>Compressed medical gases—Oxygen, Nitrous Oxide, and Medical Air—are not flammable themselves, but they are <strong>Oxidizers</strong> that make fires burn much hotter and faster. In an oxygen-enriched atmosphere (above 23.5% O2), materials that normally won't burn (like fire-resistant drapes) can ignite instantly. In 2026, the management of gas cylinders is strictly regulated by NFPA 99. Cylinders must be stored in a well-ventilated room, secured in an upright position using chains or racks to prevent them from falling, and segregated so that "Full" and "Empty" tanks are never mixed. A fallen cylinder can shear off its valve, turning the tank into a "unguided missile" capable of breaching walls.</p>
                        
                        <p>Oxygen delivery systems in hospitals utilize <strong>Zone Valve Boxes</strong>. These valves allow staff to shut off the flow of oxygen to a specific room or wing during a fire. You must know the location of the zone valve for your assigned area and understand who has the authority to shut it. Typically, the "Authority Having Jurisdiction" or the Charge Nurse/Anesthesiologist makes the call. Shutting off oxygen is a life-altering decision for patients on ventilators, so it is only done when the fire directly threatens the gas lines. Additionally, ensure that "No Smoking" and "No Open Flames" signs are prominently displayed wherever oxygen is in use or stored, as even a small spark in an enriched environment can lead to an uncontainable blaze.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Oxidizers like Oxygen make fires burn significantly faster and hotter.</li><li>Cylinders must be stored upright, secured, and away from heat sources.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Lockout/Tagout (LOTO) for Facility Systems',
                    'content': """
                        <p>Lockout/Tagout (LOTO) in healthcare extends beyond machinery to include the complex life-safety systems of the building—HVAC, medical vacuum, and emergency generators. 2026 OSHA standards (29 CFR 1910.147) mandate that before any maintenance is performed on these systems, they must be brought to a <strong>Zero Energy State</strong>. This prevents the accidental release of hazardous energy—such as an electrical surge, a burst of steam, or the activation of a fan—that could injure a worker or spark a fire. LOTO is a "One Person, One Lock" system; if three people are working on a system, there must be three separate locks on the energy-isolating device.</p>
                        <p>For healthcare professionals, the risk often involves <strong>Contractor Oversight</strong>. When third-party vendors are working on the hospital's infrastructure, they must follow the facility's LOTO program. You should never attempt to operate a switch or valve that has a "Danger: Do Not Operate" tag attached to it. In 2026, we also emphasize <strong>Stored Energy</strong>. Even after a machine is unplugged, it may hold a charge in capacitors or pressure in hydraulic lines. A world-class LOTO process includes "Verification"—attempting to start the machine after it is locked to ensure it is truly de-energized. This prevents the "surprise" energization that leads to workplace fatalities and electrical fires.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO requires a physical lock and a tag for every individual working on a system.</li><li>Verification (the "Try" step) ensures no stored energy remains in the system.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Sustaining the Life Safety Code',
                    'content': """
                        <p>The final module focuses on the <strong>Life Safety Code (NFPA 101)</strong> and the "Statement of Conditions." In 2026, healthcare fire safety is a continuous audit process. You are responsible for identifying and reporting "Life Safety Deficiencies," such as fire doors that don't latch, penetrations in smoke barriers (holes in the wall for cables), or items stored in hallways that narrow the required "Egress Width." In a hospital, the hallway is not just a walkway; it is a critical evacuation route for beds and stretchers. Blocking these routes with "parked" equipment is a major code violation that can result in immediate fines during a Joint Commission survey.</p>
                        <p>We conclude with the <strong>Culture of Readiness</strong>. A world-class healthcare professional participates in fire drills as if they were real events, understanding that "Muscle Memory" is the only thing that functions during the high-stress environment of a Code Red. You should be able to locate the fire extinguishers, pull stations, and zone valves in your sleep. Safety is a shared clinical responsibility; by maintaining these standards, you protect the most vulnerable members of society—the patients who trust you with their lives. By completing this certification, you have proven your competence in the most rigorous fire safety standards in the modern workforce.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Identify and report "Life Safety Deficiencies" like unlatched fire doors or blocked exits.</li><li>Muscle memory from regular drills is the key to an effective emergency response.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Healthcare Fire Safety is now World-Class.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
