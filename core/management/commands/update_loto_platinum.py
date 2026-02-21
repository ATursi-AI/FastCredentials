from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades LOTO to Platinum Standard (High Density)'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Lockout/Tagout (LOTO)')
            # We keep the questions, only rewriting the lesson content for density.
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Regulatory Mandate: OSHA 1910.147',
                    'content': """
                        <p><strong>The Control of Hazardous Energy (Lockout/Tagout)</strong>, codified in 29 CFR 1910.147, is written in blood. It addresses practices and procedures necessary to disable machinery or equipment to prevent the release of hazardous energy while employees perform servicing and maintenance activities. In 2026, LOTO violations remain in OSHA's "Top 10 Most Cited." The standard applies to the control of energy during servicing and/or maintenance of machines and equipment.
                        <br><strong>Normal Production Operations vs. Servicing:</strong>
                        <br>LOTO is <em>not</em> required for minor tool changes and adjustments which are routine, repetitive, and integral to the use of the equipment for production, <em>provided</em> that the work is performed using alternative measures which provide effective protection (e.g., machine guarding). However, if an employee is required to remove or bypass a guard or other safety device, or is required to place any part of their body into an area on a machine or piece of equipment where work is actually performed (point of operation), LOTO is <strong>Mandatory</strong>.
                        <br><strong>The "Zero Energy" Goal:</strong> The objective is not just "turning it off." It is achieving a state of <strong>Zero Energy</strong> where the machine is incapable of movement, electrical shock, or release of pressure, regardless of what buttons are pushed.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO is mandatory whenever a safety guard is bypassed or an employee enters the point of operation.</li><li>"Minor Servicing" exception only applies if alternative effective protection is used.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The "Fatal Five" Causes of LOTO Injuries',
                    'content': """
                        <p>Forensic analysis of LOTO fatalities reveals five primary causes. A "Platinum" safety culture specifically targets these failure points:
                        <br><strong>1. Failure to Stop Equipment:</strong> The operator assumes the machine is "off" because it isn't moving, but it is actually in a "dwell" cycle or standby mode.
                        <br><strong>2. Failure to Disconnect from Power Source:</strong> Turning off a control circuit (like a Start/Stop button or E-Stop) is NOT isolation. You must physically disconnect the energy (open the breaker, pull the plug).
                        <br><strong>3. Failure to Dissipate (Bleed) Residual Energy:</strong> Ignoring gravity, capacitors, or pressurized lines. A raised hydraulic arm can fall even if the pump is off.
                        <br><strong>4. Accidental Restarting:</strong> A coworker, unaware of the maintenance, tries to start the machine. This is prevented by the lock.
                        <br><strong>5. Failure to Clear Work Areas Before Restarting:</strong> Turning the machine back on while tools or people are still inside the danger zone.
                        <br>In 2026, we emphasize that <strong>Control Circuit Devices</strong> (push buttons, selector switches) are NOT energy isolating devices. They can fail, short circuit, or be overridden by logic controllers.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Control circuits (buttons/switches) are NOT isolation devices; you must disconnect the main power.</li><li>Residual energy (gravity, pressure) kills just as often as active electricity.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Roles and Responsibilities: Authorized vs. Affected',
                    'content': """
                        <p>OSHA strictly defines three categories of employees in a LOTO program:
                        <br><strong>1. Authorized Employee:</strong> A person who locks out or tags out machines or equipment in order to perform servicing or maintenance on that machine or equipment. They are the <em>only</em> ones legally permitted to apply and remove locks. They must receive comprehensive training on energy control procedures.
                        <br><strong>2. Affected Employee:</strong> An employee whose job requires them to operate or use a machine or equipment on which servicing or maintenance is being performed under lockout or tagout, or whose job requires them to work in an area in which such servicing or maintenance is being performed. They must be instructed in the <em>purpose</em> of the procedure and the prohibition against restarting machines.
                        <br><strong>3. Other Employee:</strong> An employee whose work operations are or may be in an area where energy control procedures may be utilized. They must be instructed about the procedure and the prohibition against restarting machines.
                        <br><strong>The Golden Rule:</strong> An Affected employee must <em>never</em> attempt to restart a machine that is locked out. If you see a lock, it means "Do Not Touch."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Only Authorized Employees can apply or remove locks.</li><li>Affected Employees must be trained never to touch or bypass a lock.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Hardware Requirements: Durable, Standardized, Substantial',
                    'content': """
                        <p>LOTO devices (locks and tags) must meet strict hardware specifications (29 CFR 1910.147(c)(5)):
                        <br><strong>1. Durable:</strong> Capable of withstanding the environment to which they are exposed for the maximum period of time that exposure is expected. Tags must not deteriorate or become illegible in wet or corrosive environments.
                        <br><strong>2. Standardized:</strong> Lockout and tagout devices must be standardized within the facility by at least one of the following criteria: Color, shape, or size. (e.g., "All Red Locks are for Electrical LOTO").
                        <br><strong>3. Substantial:</strong> Lockout devices must be substantial enough to prevent removal without the use of excessive force or unusual techniques (such as bolt cutters). Tagout devices must have an attachment strength of at least 50 lbs (non-reusable zip tie).
                        <br><strong>4. Identifiable:</strong> Lockout devices and tagout devices must indicate the identity of the employee applying the device(s).
                        <br><strong>Singular Use:</strong> LOTO locks must be used for <em>no other purpose</em>. You cannot use your LOTO lock to secure your toolbox or locker. This ensures that the sight of that specific lock triggers an immediate safety response.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO locks must be "Substantial" enough to require bolt cutters to remove.</li><li>LOTO locks must be used exclusively for safety, never for personal storage.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: The Energy Control Procedure (ECP)',
                    'content': """
                        <p>Employers must develop, document, and utilize procedures for the control of potentially hazardous energy. This document is the <strong>Energy Control Procedure (ECP)</strong>.
                        <br>The ECP must be machine-specific (unless machines are identical) and include:
                        <br>1. A specific statement of the intended use of the procedure.
                        <br>2. Specific procedural steps for shutting down, isolating, blocking, and securing machines or equipment to control hazardous energy.
                        <br>3. Specific procedural steps for the placement, removal, and transfer of lockout devices or tagout devices and the responsibility for them.
                        <br>4. Specific requirements for testing a machine or equipment to determine and verify the effectiveness of lockout devices, tagout devices, and other energy control measures.
                        <br>In 2026, "Generic" LOTO procedures are a citation magnet. If the procedure doesn't tell you <em>exactly</em> which valve to turn or which breaker to flip, it is non-compliant.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Procedures must be machine-specific, detailing exact valves and breakers.</li><li>Generic procedures are insufficient for complex machinery.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Execution: The 6-Step LOTO Process (Steps 1-3)',
                    'content': """
                        <p>The execution of LOTO follows a strict 6-step sequence.
                        <br><strong>Step 1: Preparation.</strong> The authorized employee must investigate the equipment to identify all energy sources (electrical, hydraulic, pneumatic, etc.) and the methods to control them. Notify all affected employees that LOTO is about to begin.
                        <br><strong>Step 2: Shutdown.</strong> Turn off the machine using the normal operating controls (stop button, toggle switch). This is a controlled shutdown to prevent damage or instability.
                        <br><strong>Step 3: Isolation.</strong> Operate the energy-isolating devices to physically separate the machine from its energy sources. This means opening circuit breakers, closing valves, or disconnecting lines. *Remember: A push button is NOT an isolation device.*</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Preparation involves identifying every energy source (not just electricity).</li><li>Shutdown uses normal controls; Isolation uses physical disconnects.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Execution: The 6-Step LOTO Process (Steps 4-6)',
                    'content': """
                        <p><strong>Step 4: Application.</strong> Apply the lockout and/or tagout device to the energy-isolating device. The lock must hold the device in the "Safe" or "Off" position. Tags should be applied with the lock.
                        <br><strong>Step 5: Stored Energy Control.</strong> All potentially hazardous stored or residual energy must be relieved, disconnected, restrained, and otherwise rendered safe.
                        <br>- <em>Electrical:</em> Discharge capacitors (grounding).
                        <br>- <em>Hydraulic/Pneumatic:</em> Bleed pressure from lines.
                        <br>- <em>Gravity:</em> Block or pin elevated parts that could fall.
                        <br>- <em>Mechanical:</em> Release tension in springs or block rotating parts.
                        <br><strong>Step 6: Verification ("The Try").</strong> Verify that isolation and de-energization have been accomplished. Press the "Start" button to ensure the machine does not start. Check gauges to ensure zero pressure. *Return the controls to the "Off" position after testing.* This step saves lives.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Stored energy (gravity/pressure) must be dissipated or restrained.</li><li>Verification ("Trying" to start) is the final confirmation of Zero Energy.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Group Lockout and the Lockbox System',
                    'content': """
                        <p>When multiple authorized employees work on the same machine, a <strong>Group Lockout</strong> procedure is required.
                        <br><strong>The Primary Responsibility:</strong> One authorized employee is designated with primary responsibility for the lockout.
                        <br><strong>The Lockbox Method:</strong> The primary authorized employee applies a single lock to the machine's energy isolation point. The key to that lock is placed inside a <strong>Group Lockbox</strong>. Every other authorized employee places their <em>own</em> personal lock on the outside of the lockbox.
                        <br><strong>The Logic:</strong> The machine cannot be re-energized until the primary lock is removed. The primary lock cannot be removed (because the key is trapped) until <em>every single</em> authorized employee has removed their personal lock from the box. This ensures that the last person to leave is protected just as much as the first.
                        <br><strong>No Piggybacking:</strong> Never trust someone else's lock. If your lock is not on the box, you are not protected.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>In Group Lockout, every worker applies a personal lock to the Group Lockbox.</li><li>The machine cannot be restarted until the last worker removes their lock.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Shift and Personnel Changes',
                    'content': """
                        <p>The continuity of LOTO protection must be maintained during shift or personnel changes.
                        <br><strong>The Hand-Off:</strong> There must be an orderly transfer of lockout/tagout device protection between outgoing and incoming employees to minimize exposure to hazards.
                        <br><strong>Direct Handoff:</strong> The incoming employee applies their lock and tag <em>before</em> the outgoing employee removes theirs.
                        <br><strong>Master Lock Method:</strong> If there is a gap between shifts, the supervisor may apply a "Departmental Lock" or "Master Lock" to ensure the machine stays isolated until the next shift arrives. The incoming shift then applies their personal locks and the Master Lock is removed.
                        <br><strong>Verification Repeat:</strong> The incoming shift must <em>re-verify</em> the zero-energy state (Step 6) before beginning work. Never assume the previous shift did it correctly.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO protection must be continuous; there is never a gap where the machine is unlocked.</li><li>Incoming shifts must re-verify the zero-energy state before working.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Testing or Positioning of Machines',
                    'content': """
                        <p>In situations where lockout or tagout devices must be temporarily removed to test or position the machine (e.g., jogging a conveyor belt), a specific sequence must be followed (1910.147(f)(1)):
                        <br>1. Clear the machine of tools and materials.
                        <br>2. Remove employees from the machine area.
                        <br>3. Remove the lockout or tagout devices.
                        <br>4. Energize and proceed with testing or positioning.
                        <br>5. De-energize all systems and reapply energy control measures (Steps 1-6) to continue servicing.
                        <br>This "Temporary Removal" is highly dangerous. It requires the same level of vigilance as the initial shutdown. You cannot just "leave the lock off" because you might need to test it again in 10 minutes.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Temporary removal for testing requires clearing the area and notifying employees.</li><li>You must fully re-apply LOTO measures immediately after the test is complete.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Contractors and Outside Service Personnel',
                    'content': """
                        <p>When outside contractors perform servicing or maintenance, <strong>Mutual Information Exchange</strong> is required (1910.147(f)(2)).
                        <br><strong>Host Employer Responsibilities:</strong> Must inform the contractor of their LOTO procedures and any specific hazards of the machinery.
                        <br><strong>Contractor Responsibilities:</strong> Must inform the host employer of <em>their</em> LOTO procedures.
                        <br><strong>Harmonization:</strong> The host employer must ensure that their employees understand and comply with the restrictions and prohibitions of the contractor's LOTO program. For example, if the contractor uses a different color lock, the host employees must know what it means.
                        <br>When in doubt, the "Stricter" standard applies. If the contractor has a more rigorous procedure than the host, the host employees must respect it.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Host employers and contractors must exchange LOTO procedures before work begins.</li><li>Host employees must respect the contractor's locks and tags.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Periodic Inspections and Emergency Removal',
                    'content': """
                        <p><strong>Periodic Inspection:</strong> The employer must conduct a periodic inspection of the energy control procedure at least <strong>Annually</strong>. This audit must be performed by an authorized employee <em>other than</em> the one(s) utilizing the energy control procedure being inspected. It is designed to correct any deviations or inadequacies.
                        <br><strong>Emergency Lock Removal:</strong> If the authorized employee who applied the lock is not available to remove it (e.g., they went home sick), the employer may remove the device <em>only</em> if:
                        <br>1. Verification that the authorized employee is not at the facility.
                        <br>2. All reasonable efforts are made to contact the authorized employee.
                        <br>3. The authorized employee is informed <em>before</em> they resume work at that facility.
                        <br>This is a "Nuclear Option" and should be used only in absolute necessity, with sign-off from Plant Management.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO procedures must be audited annually by an independent authorized employee.</li><li>Emergency lock removal requires verifying the worker's absence and notifying them upon return.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Lockout/Tagout (LOTO) Upgraded to PLATINUM Standard.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
