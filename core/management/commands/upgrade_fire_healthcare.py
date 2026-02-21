from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades Healthcare Fire Safety to 2,000+ char World-Class density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Fire Safety')
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: Foundations of Healthcare Fire Safety',
                    'content': """
                        <p>Fire safety in healthcare facilities is governed by a strict intersection of OSHA standards (29 CFR 1910.38/39) and the NFPA 101 Life Safety Code. In 2026, the standard has evolved to incorporate advanced "Defend-in-Place" strategies, acknowledging that modern healthcare architecture is designed to contain fire within its compartment of origin for a minimum of 2 hours. This is critical because, unlike a standard office building, a hospital or surgical center contains "non-ambulatory" patients—individuals who are sedated, connected to life-support, or physically unable to evacuate. As a credentialed professional, your duty is to understand the building's <strong>Smoke Compartments</strong> and fire doors, which are designed to shut automatically to isolate the threat.</p>
                        <p>The 2026 NFPA updates emphasize the <strong>Integrated Life Safety (ILS)</strong> framework. This involves the active synchronization of smoke dampers, automatic sprinkler systems, and high-sensitivity smoke detection (HSSD) systems that can detect "incipient" stage fires before they are visible to the human eye. You must be able to identify the location of the nearest manual pull station and fire extinguisher in your assigned zone within 10 seconds. Furthermore, healthcare staff must be familiar with the distinction between "Total Evacuation" and "Horizontal Evacuation"—the latter being the movement of patients across smoke barriers into an adjacent safe compartment rather than exiting the building entirely, which poses its own clinical risks to critical patients.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Healthcare uses "Defend-in-Place" and "Horizontal Evacuation" across smoke compartments.</li><li>The 2026 ILS framework integrates automated dampers and HSSD systems.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The Surgical Fire Triad and 2026 Risks',
                    'content': """
                        <p>A surgical fire is a devastating event that occurs when three elements converge in the Operating Room: an <strong>Ignition Source</strong>, a <strong>Fuel Source</strong>, and an <strong>Oxidizer</strong>. In 2026, the complexity of this "Triad" has increased due to the prevalence of laser surgery and advanced electrosurgical units (ESU). Ignition sources include lasers, cautery pens, and even fiber-optic light cables, which can reach temperatures high enough to ignite surgical drapes in seconds. Fuel sources include alcohol-based skin prepping agents (like ChloraPrep), intestinal gases, surgical drapes, and the patient themselves (hair and skin). Oxidizers are almost always oxygen-enriched atmospheres or nitrous oxide administered by anesthesia.</p>
                        
                        <p>Prevention in 2026 requires a mandatory <strong>"Fire Risk Assessment"</strong> during the pre-surgical time-out. The surgical team must verbally confirm that the skin-prep agent is completely dry (evaporated) before draping begins; alcohol vapors trapped under drapes are a primary cause of flash fires. For procedures above the xiphoid process (chest and head), the 2026 standard mandates the use of the lowest possible concentration of oxygen. If a fire occurs on a patient, the protocol is immediate: stop the flow of gases, remove the burning materials, and douse the area with sterile water or saline. Speed is the only variable that prevents catastrophic full-thickness burns in the O.R. environment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Triad consists of Ignition (lasers/ESU), Fuel (alcohol/drapes), and Oxidizers (O2).</li><li>Prep-agents must be 100% dry before draping to prevent vapor ignition.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Emergency Response: R.A.C.E. and P.A.S.S.',
                    'content': """
                        <p>In a healthcare fire, panic is prevented by the rigorous application of the <strong>R.A.C.E. acronym</strong>. 1. <strong>Rescue</strong>: Remove anyone in immediate danger, prioritizing those who can move themselves first to clear the path for bed-bound patients. 2. <strong>Alarm</strong>: Activate the nearest pull station and call the facility's emergency number (e.g., "Code Red" or "Dr. Red"). 3. <strong>Confine</strong>: Close all doors and windows to isolate the smoke and heat. 4. <strong>Extinguish/Evacuate</strong>: Use an extinguisher on small fires or prepare for horizontal evacuation. In 2026, the "Confine" step is emphasized as it prevents "Flashover"—the point where every surface in a room reaches its ignition temperature simultaneously.</p>
                        <p>When operating a fire extinguisher, the <strong>P.A.S.S. technique</strong> ensures mechanical efficiency under stress: 1. <strong>Pull</strong> the pin. 2. <strong>Aim</strong> at the base of the fire. 3. <strong>Squeeze</strong> the handle. 4. <strong>Sweep</strong> from side to side. In 2026, healthcare facilities are increasingly using <strong>Clean Agent (Halotron)</strong> or Water Mist extinguishers in O.R. and MRI suites. Standard ABC dry chemical extinguishers can destroy millions of dollars of sensitive medical equipment and are a respiratory hazard for patients on ventilators. You must verify that the extinguisher in your area is the correct type for the equipment present (e.g., CO2 for electrical, Water Mist for MRI).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>R.A.C.E. is the standard healthcare response protocol.</li><li>Use P.A.S.S. and ensure the extinguisher type (CO2/Water Mist) matches the room hazard.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Electrical Safety and Line Isolation Monitors (LIM)',
                    'content': """
                        <p>Electrical safety in wet-procedure areas, such as Operating Rooms, requires specialized protection beyond standard GFCI outlets. Healthcare facilities use <strong>Isolated Power Systems</strong> to protect patients from electric shock. Because patients may be physically grounded or have internal catheters/electrodes, even a tiny "micro-shock" can cause ventricular fibrillation. The <strong>Line Isolation Monitor (LIM)</strong> is the "watchdog" for this system. It continuously monitors the integrity of the isolated power and alerts staff if a "first fault" occurs. A LIM alarm (typically a red light and a buzz) indicates that the system is no longer isolated and has become a standard grounded system.</p>
                        <p>When a LIM alarm sounds, the 2026 protocol is <strong>Investigation, Not Panic</strong>. It does not necessarily mean an immediate shock is occurring, but it means the safety "buffer" is gone. The surgical team should systematically unplug the last piece of equipment that was connected until the alarm stops. If the alarm continues, it may indicate a cumulative "leakage current" from multiple devices. In 2026, all biomedical equipment must be inspected annually for leakage current standards. Never "ignore" a LIM alarm by silencing it; this is a violation of the NFPA 99 Health Care Facilities Code and puts the patient at risk of a lethal electrical discharge during a procedure.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LIM monitors the safety of isolated power in wet-procedure environments.</li><li>If the LIM alarms, unplug the most recently added equipment to identify the fault.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: 2026 Battery Threats: Lithium-Ion Safety',
                    'content': """
                        <p>The proliferation of mobile medical carts, portable ventilators, and wearable patient monitors has introduced a new fire hazard to the healthcare environment: <strong>Lithium-Ion (Li-ion) Batteries</strong>. In 2026, Li-ion fires are a top-tier safety concern due to <strong>Thermal Runaway</strong>—a chain reaction where an internal short-circuit causes the battery to heat up uncontrollably, releasing toxic gases and self-igniting. A Li-ion fire is particularly dangerous because it produces its own oxygen as it burns, making standard "smothering" techniques ineffective. These fires can burn at temperatures exceeding 1,000°C and can reignite hours after they appear to be extinguished.</p>
                        <p>Safe management of medical battery systems requires strict adherence to charging protocols. Never charge a medical device near a patient’s bed or in a cluttered area where heat cannot dissipate. If a battery is swollen, "hissing," or emitting a sweet-smelling vapor, it is in the early stages of thermal runaway. Immediately isolate the device and notify facility security. For small Li-ion fires, 2026 standards recommend a <strong>Class D extinguisher</strong> or large volumes of water to cool the surrounding cells and break the thermal chain reaction. Never use an ABC dry chemical extinguisher as your primary tool, as it will not cool the battery enough to stop the runaway process.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Lithium-Ion batteries can enter "Thermal Runaway" and reignite after being put out.</li><li>Isolate and report any batteries that are swollen or emitting a sweet smell.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Fire Safety (Healthcare-Specialized) Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
