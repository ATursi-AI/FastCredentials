from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades Slips/Trips/Falls to Platinum Standard (High Density)'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Slips, Trips, and Falls')
            # We keep the questions, only rewriting the lesson content for density.
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Physics of Equilibrium and Tribology',
                    'content': """
                        <p>To prevent falls, we must understand the science of <strong>Tribology</strong>—the study of friction, lubrication, and wear. A slip occurs when the <strong>Required Coefficient of Friction (RCOF)</strong> (the friction needed to keep your foot planted during a stride) exceeds the <strong>Available Coefficient of Friction (ACOF)</strong> (the actual friction provided by the floor/shoe interface).
                        <br><strong>The Gait Cycle:</strong>
                        <br>1. <strong>Heel Strike:</strong> The most dangerous moment. Your heel hits the floor at an angle, creating a forward force. If the floor is slippery, your heel slides forward (the "Slip").
                        <br>2. <strong>Mid-Stance:</strong> Your weight is fully over the foot. The risk here is low unless the surface collapses.
                        <br>3. <strong>Toe-Off:</strong> You push off to step forward. If friction is low, your foot slips backward.
                        <br>Most slips occur at <strong>Heel Strike</strong>. Factors like stride length, walking speed, and load carrying all increase the RCOF. The "Platinum" standard is to reduce the RCOF by adopting a "Safety Walk"—shorter strides, slower pace, and keeping the center of gravity directly over the feet.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Most slips occur at "Heel Strike" when the forward force exceeds available friction.</li><li>Shortening your stride reduces the required friction (RCOF), making a slip less likely.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Coefficient of Friction (COF) and Floor Standards',
                    'content': """
                        <p>The <strong>Static Coefficient of Friction (SCOF)</strong> is the force required to start an object moving. The <strong>Dynamic Coefficient of Friction (DCOF)</strong> is the force required to keep it moving. For decades, a SCOF of <strong>0.5</strong> was the OSHA guideline for a safe walkway. However, the 2026 ANSI/NFSI B101.3 standard focuses on DCOF, requiring a minimum of <strong>0.42</strong> for wet, level floors.
                        <br><strong>Surface Roughness:</strong> Micro-roughness (measured in micrometers) creates the "teeth" that grip the shoe sole. Over time, aggressive cleaning pads or high traffic can "polish" a floor, reducing its DCOF below safe levels.
                        <br><strong>The Hydrodynamic Squeeze Film:</strong> When a liquid (water, oil) gets trapped between the shoe and floor, it prevents contact. If the shoe tread cannot channel this liquid away (like a car tire hydroplaning), friction drops to near zero. This is why smooth-soled shoes are lethal on wet floors.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A DCOF of 0.42 is the modern safety standard for wet, level floors.</li><li>"Polishing" from foot traffic can dangerously lower a floor's slip resistance over time.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: The Hierarchy of Controls for Fall Hazards',
                    'content': """
                        <p>OSHA requires employers to protect employees from fall hazards using the <strong>Hierarchy of Controls</strong>. This is a prioritized list of strategies:
                        <br><strong>1. Elimination (Most Effective):</strong> Removing the hazard entirely. (e.g., Moving a high storage shelf to ground level so ladders aren't needed).
                        <br><strong>2. Substitution:</strong> Replacing the hazard. (e.g., Replacing a slippery tile floor with high-traction rubber matting).
                        <br><strong>3. Engineering Controls:</strong> Isolating people from the hazard. (e.g., Installing guardrails, handrails, or covers over floor holes).
                        <br><strong>4. Administrative Controls:</strong> Changing the way people work. (e.g., Implementing a "Clean-as-you-go" policy, requiring "Wet Floor" signs).
                        <br><strong>5. PPE (Least Effective):</strong> Protective equipment. (e.g., Slip-resistant footwear, fall arrest harnesses).
                        <br>You must always attempt the higher-level controls first. Relying solely on "Watch your step" (Administrative) or "Wear better shoes" (PPE) is a failure of safety management.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Elimination (removing the hazard) is the most effective control.</li><li>PPE (shoes/harnesses) is the last line of defense, used only when other controls fail.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: OSHA 1910 Subpart D: Walking-Working Surfaces',
                    'content': """
                        <p><strong>29 CFR 1910 Subpart D</strong> governs all general industry walking-working surfaces. The employer must ensure:
                        <br><strong>1. Surface Conditions:</strong> All places of employment must be kept clean, orderly, and sanitary. Workroom floors must be maintained in a clean and, to the extent feasible, dry condition.
                        <br><strong>2. Load Ratings:</strong> Employees must not exceed the load rating of any floor or roof.
                        <br><strong>3. Access and Egress:</strong> Safe means of access and egress must be provided and maintained.
                        <br><strong>4. Inspection:</strong> Walking-working surfaces must be inspected regularly and as necessary. If a hazard is identified, it must be corrected or repaired before an employee uses the surface again. If repair cannot be made immediately, the hazard must be guarded or barricaded.
                        <br>This standard eliminates the "We'll get to it later" excuse. If a tile is loose or a carpet is torn, it is an immediate violation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Floors must be kept dry; if wet processes are used, drainage and dry standing places (mats) are required.</li><li>Identified hazards must be repaired immediately or guarded until repair is possible.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Housekeeping and Contaminant Control',
                    'content': """
                        <p>Poor housekeeping causes over 50% of trip accidents. The 2026 standard is <strong>"Continuous Housekeeping."</strong>
                        <br><strong>Trip Hazards:</strong>
                        <br>- <strong>Cables/Cords:</strong> Must be taped down, run through bridges, or routed along walls.
                        <br>- <strong>Debris:</strong> Pallet fragments, packing straps, and tools must be cleared immediately.
                        <br>- <strong>Rug Bunching:</strong> Entry mats must have beveled edges and rubber backing to prevent curling or sliding.
                        <br><strong>Spill Containment:</strong>
                        <br>- <strong>The 3-Zone Strategy:</strong> 1. Mark the hazard (Wet Floor Sign). 2. Isolate the hazard (Cones/Barricade). 3. Clean the hazard (Absorbents/Mop).
                        <br>- <strong>Transition Zones:</strong> Areas where flooring changes (e.g., tile to carpet) are high-risk. Ensure the transition strip is flush (less than 1/4 inch vertical change) and visually distinct.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cords and cables are the #1 office trip hazard; use bridges or wall routing.</li><li>Mats must be flat and backed with rubber; curled edges are a major trip risk.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Stairways and Ramps (ANSI A1264.1)',
                    'content': """
                        <p>Stair safety relies on consistent geometry. <strong>ANSI A1264.1</strong> dictates:
                        <br><strong>1. Uniformity:</strong> Riser height and tread depth must be uniform within a flight of stairs. A variation of just <strong>1/4 inch</strong> disrupts the brain's "proprioceptive map," leading to a trip.
                        <br><strong>2. Tread Depth:</strong> Must be sufficient to support the ball of the foot (typically min. 11 inches).
                        <br><strong>3. Nosings:</strong> The leading edge of the stair tread (nosing) should be distinguishable (e.g., yellow high-contrast tape) and non-slip.
                        <br><strong>4. Handrails:</strong> Must be provided on both sides if possible, capable of withstanding 200 lbs of force. The "Power Grip" (wrapping fingers fully around the rail) is required, not just a "Pinch Grip."
                        <br><strong>Ramps:</strong> Slope should not exceed 1:12 (4.8 degrees). Ramps require significantly higher friction surfaces than level floors.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Stair riser height must not vary by more than 1/4 inch.</li><li>Use the "Power Grip" on handrails; touch-contact is not enough to arrest a fall.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Ladder Safety: The 4:1 Rule and 3 Points of Contact',
                    'content': """
                        <p>Ladders are tools, not workspaces.
                        <br><strong>The 4:1 Rule:</strong> For every 4 feet of height, the base of the extension ladder should be 1 foot away from the wall. (e.g., A 20ft ladder needs a 5ft base). This ensures the optimal 75.5-degree angle.
                        <br><strong>The 3 Points of Contact Rule:</strong> At all times, you must have either two hands and one foot, or two feet and one hand, in contact with the ladder.
                        <br>- <strong>The "Belt Buckle" Rule:</strong> Keep your belt buckle (center of gravity) between the side rails. Leaning out ("Overreaching") shifts your COG outside the base of support, causing the ladder to tip sideways.
                        <br>- <strong>Tie-Off:</strong> Whenever possible, secure the top of the ladder to the structure to prevent sliding.
                        <br>- <strong>Extension:</strong> The ladder must extend <strong>3 feet</strong> above the landing surface to provide a handhold for transition.</p>
                        [Image illustrating the 4-to-1 rule for ladder placement]
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Extension ladders must be set at a 4:1 ratio (75 degrees).</li><li>The ladder must extend 3 feet past the roofline for safe access/egress.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Illumination and Visual Contrast',
                    'content': """
                        <p><strong>Illumination:</strong> ANSI standards recommend minimum lighting levels (measured in foot-candles or lux) for different areas: 5 fc for hallways, 10 fc for stairs, 50 fc for detailed work.
                        <br><strong>Shadows and Glare:</strong> Shadows can hide obstacles; glare can blind a worker to a change in elevation. Lighting must be diffuse and uniform.
                        <br><strong>Visual Contrast:</strong> The human eye detects hazards by contrast.
                        <br>- <strong>Curb Cuts:</strong> Must be painted yellow to distinguish the slope from the flat road.
                        <br>- <strong>Step Edges:</strong> Must have high-contrast stripping.
                        <br>- <strong>Floor Openings:</strong> Must be guarded or covered with a cover marked "HOLE" or "COVER" in high-visibility paint.
                        <br>In 2026, "Photoluminescent" (Glow-in-the-dark) markings on stair nosings and handrails are standard for emergency egress.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Minimum lighting levels (5-10 foot-candles) are required for walkways and stairs.</li><li>High-contrast markings (yellow) are essential for identifying changes in elevation.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Footwear Selection and Maintenance',
                    'content': """
                        <p>Footwear is a critical component of the friction equation.
                        <br><strong>Tread Pattern:</strong> The pattern must be designed for the specific contaminant.
                        <br>- <strong>Water/Liquid:</strong> Requires wide channels ("sipes") to evacuate liquid and prevent hydroplaning.
                        <br>- <strong>Grease/Oil:</strong> Requires a tighter, more geometric pattern to bite through the film.
                        <br>- <strong>Outdoor/Mud:</strong> Requires deep lugs (cleats) for soft-surface traction.
                        <br><strong>Material:</strong> The outsole rubber must be compatible. "Oil-Resistant" soles won't dissolve in petroleum products.
                        <br><strong>Wear Indicator:</strong> Inspect the tread weekly. Once the tread depth is worn down (smooth spots), the shoe has lost 90% of its wet-traction capability. Employers should mandate "Slip-Resistant" (SR) rated footwear for hospitality and industrial roles.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Shoe tread acts like a car tire; it must channel liquid away to maintain contact.</li><li>Smooth soles on wet floors create a "hydrodynamic film" with near-zero friction.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Fall Protection: The 4-Foot Trigger',
                    'content': """
                        <p>In General Industry (1910), OSHA requires fall protection for any worker exposed to a fall of <strong>4 feet or more</strong> to a lower level. (Note: Construction is 6 feet).
                        <br><strong>The 3 Options:</strong>
                        <br><strong>1. Guardrails:</strong> Top rail at 42 inches (+/- 3 inches), Midrail at 21 inches, Toe-board to prevent falling objects. Must withstand 200 lbs of force.
                        <br><strong>2. Safety Nets:</strong> Installed beneath the work area.
                        <br><strong>3. Personal Fall Arrest System (PFAS):</strong> A harness, lanyard, and anchor point.
                        <br><strong>Holes:</strong> Any floor hole (including skylights) into which a person can accidentally walk must be guarded by a standard railing and toe-board or a floor hole cover.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>General Industry trigger height is 4 feet. (Construction is 6 feet).</li><li>Guardrails must have a top rail, midrail, and toe-board.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Personal Fall Arrest Systems (PFAS): The ABCD Model',
                    'content': """
                        <p>When using a PFAS, you must understand the <strong>ABCD</strong> components:
                        <br><strong>A - Anchorage:</strong> The secure point of attachment. It must be capable of supporting <strong>5,000 lbs</strong> per worker attached. (Never anchor to a conduit or PVC pipe).
                        <br><strong>B - Body Wear:</strong> The Full Body Harness. Body belts are <em>prohibited</em> for fall arrest as they cause internal organ damage. The D-ring must be located in the center of the back between the shoulder blades.
                        <br><strong>C - Connector:</strong> The device linking the harness to the anchor (Lanyard or Self-Retracting Lifeline). It must have double-locking snap hooks.
                        <br><strong>D - Deceleration Device:</strong> The shock absorber. It limits the arresting force on the body to under 1,800 lbs.
                        <br><strong>Rescue Plan:</strong> You must have a plan to rescue a suspended worker within <strong>15 minutes</strong> to prevent "Suspension Trauma" (blood pooling in legs leading to cardiac arrest).</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Anchors must support 5,000 lbs per person.</li><li>Suspension trauma can kill in under 30 minutes; a rapid rescue plan is mandatory.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Human Factors and Cultural Safety',
                    'content': """
                        <p>Even with the best equipment, falls happen due to human error.
                        <br><strong>Psychological Factors:</strong>
                        <br>- <strong>"Hurry Sickness":</strong> Rushing increases gait speed, reducing friction and attention.
                        <br>- <strong>Distraction:</strong> Texting while walking ("Distracted Walking") creates "Inattentional Blindness" to hazards.
                        <br>- <strong>Fatigue:</strong> Reduces reaction time and core stability.
                        <br><strong>Cultural Safety:</strong> We must move from "Compliance" to "Commitment." A Platinum safety culture encourages reporting near-misses. "I almost slipped there" is a gift—it tells you where the next accident will happen. Fix the rug, dry the floor, change the lightbulb. Safety is active, not passive.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>"Hurry Sickness" and Distraction are the leading behavioral causes of falls.</li><li>Report every near-miss to identify and fix latent hazards before they cause injury.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Slips, Trips, and Falls Upgraded to PLATINUM Standard.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
