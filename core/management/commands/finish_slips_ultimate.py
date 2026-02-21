from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Slips, Trips, and Falls to 12 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Slips, Trips, and Falls')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Physics of the Fall',
                    'content': """
                        <p>In 2026, <strong>Slips, Trips, and Falls</strong> remain the #1 cause of lost workdays across all industries. To prevent them, we must understand the physics. A <strong>Slip</strong> occurs when there is too little friction (traction) between your footwear and the walking surface. A <strong>Trip</strong> occurs when your foot hits an object, causing you to lose balance. A <strong>Fall</strong> happens when you move too far from your center of gravity. This module establishes the "Zero-Fall" mindset: most of these accidents are 100% preventable through environmental control and situational awareness.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Slips are caused by low friction; Trips are caused by unexpected obstacles.</li><li>Maintaining your center of gravity is the physical key to balance.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The COF: Understanding Traction',
                    'content': """
                        <p>The <strong>Coefficient of Friction (COF)</strong> is the measurement of "slip resistance." In 2026, OSHA-compliant surfaces typically require a COF of 0.5 or higher. Contaminants like water, grease, oil, and even dust act as "lubricants" that slash the COF, turning a safe floor into a skating rink. You must be aware of "Transition Hazards"—moving from a high-traction surface (carpet) to a low-traction surface (wet tile). Your choice of footwear is your primary personal engineering control against COF failure.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A higher COF means better traction and fewer slips.</li><li>Contaminants like oil or dust are the primary causes of COF loss.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Housekeeping: The First Line of Defense',
                    'content': """
                        <p>In 2026, "Good Housekeeping" is a legal safety requirement. Over 50% of workplace falls are caused by poor housekeeping. This includes cluttered aisles, loose cords (the #1 trip hazard in offices), and uncleaned spills. The 2026 rule is <strong>"See it, Own it"</strong>: if you see a spill or a trip hazard, you are responsible for either cleaning it immediately, marking it with a "Wet Floor" sign, or reporting it. Leaving a hazard for "someone else" is a direct contribution to a future injury.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Housekeeping is the most effective way to prevent trips and falls.</li><li>"See it, Own it" means every employee is responsible for hazard control.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Stairs and Ladders: Vertical Safety',
                    'content': """
                        <p>Falls from heights are the most lethal. In 2026, we mandate the <strong>"Three Points of Contact"</strong> rule for all ladder and stair use: two hands and one foot, or two feet and one hand must be on the ladder at all times. Never carry heavy loads up a ladder; use a hoist or a "tool belt" instead. For stairs, handrails are not optional—they are life-saving devices. Most stair falls occur on the top or bottom three steps because people begin to "look away" before the transition is complete.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Always maintain Three Points of Contact on ladders.</li><li>Use handrails on every staircase, every time.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Lighting and Visual Contrast',
                    'content': """
                        <p>You cannot avoid what you cannot see. In 2026, <strong>Inadequate Lighting</strong> is recognized as a major contributor to falls, especially in warehouses and parking lots. We also focus on "Visual Contrast"—using high-visibility tape or paint on the edges of steps and "curb cuts" to help the brain distinguish changes in elevation. In a 2026 workspace, any change in floor level greater than 1/4 inch must be beveled or marked to prevent "Micro-Trips."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Proper lighting is essential for identifying floor-level hazards.</li><li>Use visual contrast (yellow tape) to mark changes in elevation.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Human Factors: Distraction and Fatigue',
                    'content': """
                        <p>The "Human Factor" is the most common cause of falls in the digital age. <strong>Distracted Walking</strong> (using a phone while moving) is the 2026 equivalent of driving while intoxicated. When your eyes are on a screen, your brain loses "Proprioception"—the ability to sense your body's position in space. Fatigue also slows your reaction time; a tired worker is 3x more likely to slip on a wet patch that an alert worker would have easily avoided. Eyes on path, mind on task.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Distracted walking is a major 2026 safety risk; keep phones away while moving.</li><li>Fatigue significantly increases the risk of balance-related accidents.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Walking-Working Surfaces: OSHA 1910',
                    'content': """
                        <p>OSHA 29 CFR 1910 Subpart D governs all <strong>Walking-Working Surfaces</strong>. In 2026, employers are required to inspect surfaces regularly and keep them in a "clean, orderly, and sanitary condition." Floors must be kept dry whenever possible. If the floor is naturally wet (like in a car wash or food prep area), non-slip mats and proper drainage are mandatory. You have a right to work on a surface that is free from "recognized hazards" like holes, loose boards, or protruding nails.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Employers must inspect and maintain all walking surfaces for safety.</li><li>Non-slip mats are required in areas where wet floors are unavoidable.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Footwear as PPE',
                    'content': """
                        <p>In many industries, shoes are considered <strong>Personal Protective Equipment (PPE)</strong>. For 2026, we require slip-resistant outsoles with "Siped" patterns that channel water away from the contact point, similar to car tires. Worn-out treads are a major hazard; once the "circle" or "tread pattern" is smooth, the shoe is no longer providing protection. Your footwear must be appropriate for the specific contaminant in your environment (e.g., oil-resistant vs. water-resistant soles).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Inspect shoe treads regularly; smooth soles provide zero traction on wet floors.</li><li>Use siped or specialized soles to channel liquids away from the foot.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Weather-Related Hazards',
                    'content': """
                        <p>External conditions impact internal safety. In 2026, <strong>"Tracking"</strong>—snow, ice, and rain brought in on shoes—is a leading cause of lobby falls. Entrance mats should be at least 10 to 12 feet long to allow for "Step-Off" drying of soles. Outside, "Black Ice" is the invisible killer. In 2026, we use the "Penguin Walk" for icy surfaces: point your toes out slightly, keep your knees loose, and take short, shuffling steps to keep your center of gravity directly over your feet.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Entrance mats must be long enough to dry shoes completely.</li><li>Use the "Penguin Walk" (short, shuffling steps) on icy or slippery external surfaces.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Fall Protection: The 4-Foot Rule',
                    'content': """
                        <p>In 2026 general industry, OSHA requires <strong>Fall Protection</strong> for any height over <strong>4 feet</strong>. This can include guardrails, safety nets, or Personal Fall Arrest Systems (PFAS) like harnesses and lanyards. If you are working on an elevated platform, "unprotected edges" are a death trap. You must never bypass a guardrail or "lean out" past the safety boundary. Fall protection is not a suggestion; it is the barrier between a minor slip and a fatal vertical drop.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Fall protection is mandatory for heights of 4 feet or more in general industry.</li><li>Never lean over or bypass guardrails on elevated platforms.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Reporting and "Near-Miss" Analysis',
                    'content': """
                        <p>A 2026 world-class safety culture treats a <strong>Near-Miss</strong> as an actual injury. If you trip but catch yourself, you have just discovered a "latent hazard." If you don't report it, the next person will fall. Reporting allows for "Root Cause Analysis": Is the floor too slippery? Is the light bulb out? Is the rug bunching up? By reporting near-misses, you help the organization fix the environment before a life-altering injury occurs. Data-driven safety is the only way to reach "Zero-Fall" status.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Report all near-misses to identify hazards before an injury occurs.</li><li>"Root Cause Analysis" helps fix the environment, not just the symptom.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Balance Mastery',
                    'content': """
                        <p>We conclude with <strong>Personal Responsibility</strong>. Balance is a skill that must be practiced. In 2026, we encourage "Dynamic Stability"—staying fit, maintaining core strength, and being mindful of your environment. You are the captain of your own movement. By keeping your workspace clean, wearing the right shoes, and maintaining three points of contact, you eliminate the risk of the most common injury in the world. Stay alert, stay balanced, and stay safe. You are now a certified master of Slips, Trips, and Falls prevention.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Core strength and physical fitness are natural defenses against falls.</li><li>Situational awareness is your most powerful tool for staying upright.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)

            # --- EXAM (15 QUESTIONS) ---
            qs = [
                ('What is the #1 cause of lost workdays in most industries?', ['Stress', 'Slips, Trips, and Falls', 'Flu', 'Car accidents'], 2),
                ('What causes a "Slip"?', ['Hitting an object with your foot', 'Too little friction between footwear and floor', 'Looking at your phone', 'Being too tall'], 2),
                ('What is the "COF" in floor safety?', ['Center of Fall', 'Coefficient of Friction', 'Circle of Force', 'Carry on Firmly'], 2),
                ('What is the "See it, Own it" rule?', ['If you see a hazard, you are responsible for fixing or reporting it', 'If you see a spill, you should walk around it', 'Only managers own safety', 'You only own what you buy'], 1),
                ('What is the "Three Points of Contact" rule?', ['Three people must watch you climb', 'Two hands and one foot (or vice-versa) on a ladder at all times', 'Touching the floor with three fingers', 'Always wear three layers of clothes'], 2),
                ('Most stair falls occur on which steps?', ['The middle steps', 'The top or bottom three steps', 'The first step only', 'Only on spiral stairs'], 2),
                ('How much of an elevation change requires a bevel or marking to prevent trips?', ['1 inch', '1/4 inch or more', '5 inches', 'Any change is fine'], 2),
                ('What is "Distracted Walking" in 2026?', ['Walking while tired', 'Using a mobile device while moving', 'Walking in the rain', 'Talking to a coworker'], 2),
                ('In 2026, what is the OSHA fall protection height for general industry?', ['10 feet', '4 feet', '20 feet', 'Only on rooftops'], 2),
                ('How should you walk on an icy surface (The Penguin Walk)?', ['Running fast', 'Short, shuffling steps with toes pointed out', 'Lifting feet high', 'Backward'], 2),
                ('Why is a "Near-Miss" report important?', ['To get people in trouble', 'To identify and fix a hazard before someone actually gets hurt', 'To fill out paperwork', 'It isn\'t important'], 2),
                ('Where should you look for "First-Aid" for a chemical slip injury?', ['Section 1 of the SDS', 'Section 4 of the SDS', 'The HR manual', 'The news'], 2),
                ('What is "Visual Contrast" used for?', ['To make the floor look pretty', 'To help the brain distinguish changes in floor level or elevation', 'To save on lighting costs', 'To hide dirt'], 2),
                ('How long should an entrance mat be to properly dry shoes?', ['2 feet', '10 to 12 feet', '5 feet', 'No mat is needed'], 2),
                ('If you cannot carry a load and maintain 3 points of contact on a ladder, what should you do?', ['Carry it in your teeth', 'Use a hoist, rope, or tool belt to lift the items', 'Have someone throw it to you', 'Run up the ladder'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Slips, Trips, and Falls is World-Class (23/24 Complete).'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
