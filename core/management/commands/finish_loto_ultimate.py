from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades LOTO to 12 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Lockout/Tagout (LOTO)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Fatal Stakes of Hazardous Energy',
                    'content': """
                        <p>Lockout/Tagout (LOTO) is the physical practice of ensuring that a machine is totally "Zero Energy" before service or maintenance begins. In 2026, LOTO failures remain one of the top 10 causes of workplace fatalities. "Hazardous Energy" isn't just electricity; it includes <strong>Mechanical, Hydraulic, Pneumatic, Chemical, Thermal, and Gravitational</strong> forces. If a machine restarts unexpectedly while a worker is inside, the result is almost always catastrophic. This module establishes the absolute requirement: if you are performing maintenance where the startup of a machine could cause injury, you MUST apply LOTO.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO prevents the "unexpected startup" of machinery during maintenance.</li><li>Hazardous energy includes electricity, pressure, heat, and gravity.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Authorized vs. Affected Personnel',
                    'content': """
                        <p>OSHA distinguishes between two groups. 1. <strong>Authorized Personnel</strong>: These are the trained workers who are permitted to apply the locks and perform the maintenance. They are responsible for the entire LOTO procedure. 2. <strong>Affected Personnel</strong>: These are employees whose jobs require them to operate the machine or work in the area where LOTO is being applied. In 2026, an "Affected" worker is strictly prohibited from touching a lock or attempting to restart a machine. If you aren't the one who put the lock on, you are NEVER the one to take it off.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Only "Authorized" employees can apply or remove locks.</li><li>"Affected" employees must stay clear and never attempt to bypass a LOTO device.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: The 6 Steps of a Standard Lockout',
                    'content': """
                        <p>In 2026, the <strong>Standardized 6-Step Sequence</strong> is the only way to ensure safety: 1. <strong>Preparation</strong> (Identify the energy source). 2. <strong>Shutdown</strong> (Turn the machine off). 3. <strong>Isolation</strong> (Pull the plug or flip the breaker). 4. <strong>Application</strong> (Apply your lock and tag). 5. <strong>Stored Energy Control</strong> (Bleed the pressure, ground the charge). 6. <strong>Verification</strong> (The "Try" step). Skipping even one of these steps is a terminable offense in high-safety 2026 facilities.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Following the exact 6-step sequence is mandatory for every lockout.</li><li>Preparation and Verification are the most critical "bookend" steps.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: "Try Before You Trust": The Verification Step',
                    'content': """
                        <p>The most dangerous moment in LOTO is assuming the machine is dead because you flipped a switch. Step 6, <strong>Verification</strong>, requires you to physically attempt to start the machine after the locks are applied. This is often called the "Try" step. You must verify that the machine cannot be restarted from the local control panel, the remote start, or any other activation point. If the machine moves, even slightly, your isolation has failed. You must never begin work until you have "Tried" the machine and proven it is at Zero Energy.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Verification is the final proof that the machine is actually at Zero Energy.</li><li>Always "Try" to start the machine after applying locks to ensure isolation.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Stored Energy: The Hidden Killer',
                    'content': """
                        <p>Many accidents occur because of <strong>Residual or Stored Energy</strong>. After a machine is isolated from its power source, energy can still be trapped in capacitors (electricity), springs (tension), or tanks (pressure). In 2026, we also focus on <strong>Gravitational Energy</strong>—if a heavy press is held up by a hydraulic ram, you must physically "block" or "pin" the press so it cannot fall if the hydraulic line fails. You must "Bleed, Block, and Vent" all stored energy before you are safe to work.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Stored energy remains in a machine even after the main power is cut.</li><li>Use blocks, pins, and bleed valves to neutralize residual energy.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Hardware Standards: Durable and Singular',
                    'content': """
                        <p>LOTO hardware (locks and tags) must meet four OSHA criteria: 1. <strong>Durable</strong> (must withstand the environment). 2. <strong>Standardized</strong> (must be the same color/shape throughout the plant). 3. <strong>Substantial</strong> (cannot be removed without excessive force). 4. <strong>Identifiable</strong> (must show the name of the authorized person). In 2026, a LOTO lock must NEVER be used for any other purpose, such as locking a toolbox or a locker. The presence of a LOTO lock must signal one thing only: Life-Saving Isolation.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO locks must be unique and identifiable to the individual authorized worker.</li><li>Never use a LOTO lock for a non-safety purpose (like a locker).</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: The Role of the Tag',
                    'content': """
                        <p>A tag is not a physical barrier; it is a communication tool. In 2026, a tag must be attached to every lock and must clearly state "DO NOT OPERATE." It must also include the <strong>Authorized Person\'s Name</strong>, their department, and the date the LOTO was applied. Tags are designed to withstand 50 lbs of pull-force to ensure they aren't accidentally knocked off. While some situations allow for "Tagout Only," this is extremely rare in 2026 and requires additional safety measures; "Lockout" is always the preferred and mandatory standard when a lock can be applied.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Tags provide critical communication about who is working on the machine.</li><li>"Lockout" is the mandatory standard; "Tagout Only" is rarely permitted.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Group Lockout and Multi-Lock Hasps',
                    'content': """
                        <p>When multiple people work on a single machine, a <strong>Multi-Lock Hasp</strong> must be used. In 2026, the rule is simple: <strong>"One Person, One Lock, One Key."</strong> Every worker must apply their <em>own</em> personal lock to the hasp. The machine cannot be restarted until the very last person has finished their work and removed their personal lock. You must never rely on a coworker\'s lock to protect you. If there are 5 people working, there must be 5 locks on the machine.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Every worker must apply their own personal lock to a hasp.</li><li>The machine is only safe when every single worker\'s lock is in place.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Shift Changes and Long-Term Lockouts',
                    'content': """
                        <p>Shift changes are high-risk periods for LOTO errors. If work continues into a second shift, the <strong>"Live Hand-Off"</strong> is required. The incoming authorized person applies their lock <em>before</em> the outgoing person removes theirs. If a lockout remains on a machine for multiple days, it is a "Long-Term Lockout." In 2026, these must be audited daily by supervisors to ensure the machine remains isolated and that the tags are still legible. Consistency is the only way to prevent a catastrophic "communication gap" between crews.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>During shift changes, the incoming worker must apply their lock before the outgoing worker removes theirs.</li><li>Long-term lockouts require daily supervisor audits.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Special Situations: Cord-and-Plug Equipment',
                    'content': """
                        <p>Equipment that is powered by a simple <strong>Cord and Plug</strong> (like a portable drill or a small conveyor) is exempt from traditional LOTO <em>only if</em> the plug is under the <strong>Exclusive Control</strong> of the person performing the work. This means the person must have the plug within their line of sight or within their reach at all times. If you have to walk away from the plug, even for a minute, you must apply a "Plug Lockout" device to ensure no one else can plug it in while your hands are in the machine.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cord-and-plug items are only exempt if the plug is in your constant control.</li><li>If you leave the equipment, the plug must be locked out.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Emergency Lock Removal',
                    'content': """
                        <p>What happens if a worker leaves for the day but forgets their lock on the machine? In 2026, <strong>Emergency Lock Removal</strong> is a high-level administrative process. It can only be performed by a supervisor after: 1. Verifying the worker is not in the facility. 2. Attempting to contact the worker. 3. Verifying the machine is safe to restart. 4. Ensuring the worker is notified *immediately* upon their return to work. Cutting a lock off is a last resort and requires documented authorization to prevent a life-threatening mistake.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Only supervisors can remove a forgotten lock, and only after a strict verification process.</li><li>The worker must be notified before they resume work that their lock was removed.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 LOTO Audit Culture',
                    'content': """
                        <p>We conclude with the <strong>Annual Periodic Inspection</strong>. OSHA requires that LOTO procedures be audited at least once a year to ensure they are being followed correctly. In 2026, world-class facilities use "Digital Twin" models to simulate lockouts before they happen. However, safety ultimately rests on your <strong>Surgical Conscience</strong>. Never take a shortcut. Never assume a machine is off. And never, under any circumstances, allow anyone else to remove your lock. By mastering LOTO, you have gained the ultimate power in safety: the power to prevent the unexpected. You are now a certified guardian of Zero Energy.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LOTO procedures must be audited annually to ensure ongoing compliance.</li><li>Shortcuts in LOTO are the leading cause of preventable industrial deaths.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)

            # --- EXAM (15 QUESTIONS) ---
            qs = [
                ('What is the primary goal of Lockout/Tagout (LOTO)?', ['To save electricity', 'To prevent the unexpected startup of machinery during maintenance', 'To keep unauthorized people away from the office', 'To speed up repairs'], 2),
                ('Who is an "Authorized Person" in a LOTO program?', ['Anyone who works in the building', 'A worker trained and permitted to apply locks and perform maintenance', 'The CEO only', 'The janitorial staff'], 2),
                ('Which energy source is NOT covered by LOTO?', ['Electrical', 'Gravitational', 'Hydraulic', 'All of these ARE covered'], 4),
                ('What is the final step (Step 6) of a standard lockout procedure?', ['Applying the tag', 'Verifying (The "Try" step) to ensure Zero Energy', 'Taking a break', 'Turning on the power'], 2),
                ('What should an "Affected Employee" do when they see a LOTO lock?', ['Try to remove it', 'Stay clear and never attempt to restart the machine', 'Call the maintenance worker', 'Ignore it'], 2),
                ('Why must you "Bleed or Block" stored energy?', ['To make the machine lighter', 'Because residual energy can still cause movement or injury after power is cut', 'To save time', 'OSHA doesn\'t require this'], 2),
                ('What is the rule for multi-person lockouts?', ['One lock for the whole group', 'One person, one lock, one key', 'The supervisor holds all the keys', 'Locks are not required for groups'], 2),
                ('How often must LOTO procedures be audited by a supervisor?', ['Every 5 years', 'At least once a year (annually)', 'Every month', 'Only after an accident'], 2),
                ('When can a supervisor remove an employee\'s lock?', ['Anytime they want', 'Only in an emergency after following a strict verification and notification process', 'If the employee is at lunch', 'Never'], 2),
                ('What must a LOTO tag clearly state?', ['"Fixing it soon"', '"Do Not Operate"', '"Property of Maintenance"', '"Machine is Broken"'], 2),
                ('Which is a requirement for LOTO locks?', ['They must be easy to pick', 'They must be standardized and identifiable to the individual worker', 'They must be blue', 'They must be made of plastic'], 2),
                ('What is "Verification" in LOTO?', ['Signing a paper', 'Physically trying to start the machine to prove it won\'t move', 'Asking a coworker if it\'s off', 'Checking the clock'], 2),
                ('Does cord-and-plug equipment (like a fan) always require LOTO?', ['Yes', 'No, only if the plug is NOT in the exclusive control of the worker', 'Only if it\'s 220V', 'Only in warehouses'], 2),
                ('If you work across multiple shifts, when do you remove your lock?', ['At the end of your shift, after the next worker has applied theirs', 'Whenever you feel like it', 'You leave it on and take the key home', 'You give your key to the next shift'], 1),
                ('What should you do if a machine moves during the "Try" step?', ['Start working anyway', 'Identify and isolate the remaining energy source before proceeding', 'Kick the machine', 'Turn the power back on'], 2)
            ]

            for text, options, correct in qs:
                Question.objects.create(
                    course=course,
                    text=text,
                    option_1=options[0],
                    option_2=options[1],
                    option_3=options[2],
                    option_4=options[3],
                    correct_option=correct
                )

            self.stdout.write(self.style.SUCCESS('SUCCESS: LOTO is now World-Class (22/24 Complete).'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
