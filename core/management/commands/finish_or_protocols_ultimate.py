from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes O.R. Protocols with Modules 5-12 at 2,000+ char density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Operating Room Protocols')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Gowning and Gloving: Closed vs. Open Techniques',
                    'content': """
                        <p>In 2026, the transition from the scrub sink to the sterile gown is the most vulnerable moment for contamination. The <strong>Closed Gloving Technique</strong> is the mandatory standard for the initial donning of sterile attire. In this method, the hands remain inside the sleeves of the gown until the gloves are pulled over the cuffs. This ensures that the bare skin of the hands never touches the exterior of the sterile gown or the gloves. If a glove is punctured during surgery, the <strong>Open Gloving Technique</strong> is used for replacement, but only after the contaminated glove is removed by a non-scrubbed circulator.</p>
                        
                        <p>Gown integrity is rated by <strong>AAMI Levels (1-4)</strong>. Level 4 gowns provide the highest fluid and viral penetration resistance, required for high-volume blood loss procedures like orthopedic or trauma surgery. In 2026, we also emphasize "Double Gloving" with an indicator under-glove. This system uses two different colored gloves; if the outer glove is nicked, the contrast color of the under-glove becomes visible, alerting the professional to a breach in the viral barrier. This "Visual Warning" system has reduced the risk of bloodborne pathogen exposure to surgical teams by over 70% in 2026 clinical data.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Closed gloving ensures bare skin never contacts the sterile exterior of the attire.</li><li>Double gloving with indicator gloves is the 2026 standard for viral protection.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: The 2026 Surgical Time-Out: Final Verification',
                    'content': """
                        <p>The <strong>Surgical Time-Out</strong> is a mandatory "Hard Stop" that occurs in the O.R. immediately before the first incision. In 2026, the Joint Commission "Universal Protocol" requires the participation of the <em>entire</em> surgical team, including the surgeon, anesthesia, and nursing. All other activities—including instrument setup and music—must cease. The team must verbally verify: 1. Correct Patient. 2. Correct Procedure. 3. Correct Site (and side). 4. Correct Positioning. 5. Availability of necessary implants or special equipment. In 2026, we also include a "Fire Risk Assessment" as part of this verbal check.</p>
                        <p>A "Culture of Safety" means that the Time-Out is not a checklist to be rushed through. If there is a discrepancy—even a minor one in the spelling of a name on an ID band—the "Stop the Line" protocol is activated, and the surgery does not proceed until the error is rectified. 2026 standards also emphasize the <strong>"Post-Procedure Debrief"</strong> before the patient leaves the room. The team confirms the name of the procedure performed, ensures all counts (sponges, needles, instruments) are correct, and identifies any equipment issues that occurred. This "Dual-Check" system is the primary defense against "Never Events" like retained foreign objects or wrong-site surgery.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Time-Out is a "Hard Stop" requiring 100% team engagement before incision.</li><li>The Debrief ensures all counts are correct before the patient leaves the suite.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Surgical Smoke Evacuation: Protecting the Team',
                    'content': """
                        <p>Surgical smoke, or "plume," is a hazardous byproduct of electrosurgery, lasers, and ultrasonic devices. In 2026, the <strong>Smoke-Free O.R. Initiative</strong> is a legal requirement in many jurisdictions. Plume contains carbon monoxide, polycyclic aromatic hydrocarbons, and aerosolized biological matter, including blood fragments and viruses (like HPV). Inhaling the smoke from one gram of tissue is equivalent to smoking 27 to 30 unfiltered cigarettes. In 2026, standard surgical masks are recognized as insufficient protection, as they do not filter out the sub-micron particles found in the plume.</p>
                        
                        <p>The 2026 protocol mandates the use of <strong>Dedicated Smoke Evacuation Systems</strong> with ULPA (Ultra-Low Particulate Air) filters. These systems must be placed within 2 inches of the surgical site to capture the plume at the source. Wall suction units are not designed for this purpose and can quickly become clogged or contaminated. As a professional in the O.R., you have a right to a smoke-free environment. Ensuring the evacuator is active during any "energy-based" tissue dissection is as critical to your long-term health as wearing lead aprons during X-rays. 2026 compliance means zero tolerance for visible or odorous plume in the surgical suite.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Surgical smoke is a biohazard containing viruses and carcinogens.</li><li>Smoke evacuators with ULPA filters must be used within 2 inches of the source.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Patient Positioning and Pressure Injury Prevention',
                    'content': """
                        <p>Safe patient positioning is a collaborative effort between anesthesia, the surgeon, and the nursing staff. In 2026, we focus on <strong>Preventing Perioperative Pressure Injuries (PPI)</strong>. When a patient is under anesthesia, they lose the ability to shift their weight or signal pain from nerve compression. Common positions—Supine, Prone, Lithotomy, and Lateral—each carry specific risks. For example, the <strong>Lithotomy Position</strong> (legs in stirrups) carries a high risk of "Compartment Syndrome" and peroneal nerve damage if the legs are not padded and positioned with anatomical alignment.</p>
                        <p>The 2026 standard requires <strong>Gel-based or Memory Foam Padding</strong> for all "Bony Prominences," including the heels, elbows, sacrum, and occiput (back of the head). If a surgery exceeds 4 hours, the risk of pressure injury increases exponentially. The team must document a "Skin Assessment" both before and after the procedure. Additionally, we monitor for "Shear" and "Friction"—ensuring that when a patient is moved, they are lifted rather than dragged across the table. In 2026, patient safety extends beyond the surgical site to the holistic protection of the body's largest organ: the skin.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Anesthetized patients cannot feel nerve compression; padding is mandatory.</li><li>The Lithotomy position requires specific care to prevent nerve damage and compartment syndrome.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Instrumentation and Sterilization Logistics',
                    'content': """
                        <p>In 2026, the logistics of surgical instrumentation are managed via <strong>Digital Tracking Systems</strong>. Every tray and individual tool is etched with a unique 2D barcode, allowing the team to verify its sterilization history instantly. You must distinguish between "Standard Terminal Sterilization" (autoclaving) and <strong>Immediate Use Steam Sterilization (IUSS)</strong>. IUSS, formerly known as "flash sterilization," is only for emergency situations where an essential instrument has been contaminated and no backup is available. In 2026, IUSS is heavily scrutinized and should never be used for "convenience" or as a substitute for an inadequate instrument inventory.</p>
                        
                        <p>Before any tray is opened onto the sterile field, the <strong>Chemical Indicator</strong> (Class 5 or 6) must be inspected. If the indicator has not reached the "pass" zone, the entire tray is considered non-sterile and must be rejected. Furthermore, the "Sterile Wrapper" must be checked for holes, moisture (strike-through), or an expired date. In 2026, we emphasize <strong>Instrument Integrity</strong>: if a tool is rusted, pitted, or stiff, it can harbor "Biofilms" that are resistant to standard cleaning. These tools must be removed from the fleet. Your vigilance in the "Back Table" setup is what prevents an SSI before the surgery even begins.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>IUSS is for emergencies only and requires specific documentation.</li><li>Always verify the internal chemical indicator before using an instrument tray.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: O.R. Emergencies: Code Blue and Fire',
                    'content': """
                        <p>Emergencies in the O.R. require a specialized response because the patient is often "Open" and "Intubated." In a <strong>Code Blue</strong> (Cardiac Arrest) scenario, the 2026 protocol mandates that the sterile field be covered with a sterile drape while the team prepares for compressions. If the surgery is "In-Chest" or "In-Abdomen," the surgeon may perform internal cardiac massage. The primary role of the non-clinical personnel (such as a device rep) is to <strong>Step Back and Stay Clear</strong> unless specifically asked by the Team Leader to assist with getting equipment. Your priority is to maintain your own sterility if possible, or de-scrub if you are in the way of the crash cart.</p>
                        <p><strong>O.R. Fires</strong> are a "Never Event" that still occur in 2026 due to the "Surgical Fire Triad" (Oxidizers, Fuel, and Ignition). If a fire occurs on the patient, the "Standard Operating Procedure" is: 1. Stop the flow of gases (Anesthesia). 2. Remove burning materials from the patient. 3. Extinguish with saline or water. In 2026, we use <strong>CO2 Fire Extinguishers</strong> for O.R. fires because ABC dry chemical extinguishers leave a toxic residue that can ruin millions in equipment and is lethal if inhaled by an open-cavity patient. Knowing the location of the nearest CO2 extinguisher and the "Gas Shut-off" valve is a mandatory 2026 competency for all O.R. staff.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>In a Code Blue, the sterile field is covered while resuscitation begins.</li><li>Use CO2 extinguishers in the O.R. to avoid toxic residue in surgical sites.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Robotic and Digital Protocols (Smart O.R.)',
                    'content': """
                        <p>The 2026 <strong>Robotic Surgical Suite</strong> introduces new challenges for the sterile field. Robotic arms must be "Draped" using specific, multi-layered sterile covers. Because the robot is a large, non-sterile piece of machinery that hovers over the patient, the "Sterile Volume" is constantly shifting. You must be hyper-aware of the <strong>"Proximity Hazard"</strong>—ensuring that the robotic joints do not touch the sterile drapes or the scrubbed personnel as they move. In 2026, we utilize "Laser Guarding" systems that provide a visual "light grid" to show the boundaries of the sterile field around the robot.</p>
                        <p>Digital integration also means the presence of more <strong>Portable Electronics</strong> (tablets, cameras, and integration screens). In 2026, any device that enters the "Sterile Perimeter" must be either placed in a sterile plastic sleeve or disinfected with a specific 2026-approved high-level disinfectant. "Cyber-Hygiene" is also a factor; O.R. systems must be protected from unauthorized USB drives which can introduce malware to critical life-support systems. As a professional, you are responsible for the physical and digital sterility of your equipment. The "Smart O.R." is only safe if the "Traditional O.R." principles of sterile technique are applied to every new piece of technology.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Robotic arms require specialized sterile drapes; monitor for "Proximity Hazards."</li><li>All portable electronics in the sterile field must be sleeved or high-level disinfected.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Surgical Conscience',
                    'content': """
                        <p>The final and most important module is <strong>Surgical Conscience</strong>. This is an internal, moral obligation that overrides hierarchy, ego, and the pressure of a busy schedule. It means doing the right thing for the patient even when no one is watching. In 2026, this is manifested in the <strong>"Speak Up" Culture</strong>. If a medical student sees a senior surgeon touch a non-sterile light handle, they have a professional duty to say, "I believe there was a break in technique." A world-class O.R. environment is one where "safety is higher than rank."</p>
                        <p>We conclude with <strong>Accountability and Reporting</strong>. In 2026, we treat "Near-Misses" with the same seriousness as actual errors. Reporting a break in sterility or a equipment malfunction is not about "blame"—it is about "Process Improvement." By completing this certification, you have joined the "Surgical Elite"—the professionals who ensure that the O.R. remains a sanctuary of healing. Your commitment to the 12-inch rule, the Time-out, and the 2026 smoke evacuation protocols is what saves lives every single day. Stay vigilant, stay ethical, and stay sterile.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Surgical Conscience is the internal moral drive to admit and correct breaks in technique.</li><li>A "Speak Up" culture means safety and sterility are more important than professional rank.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: O.R. Protocols 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
