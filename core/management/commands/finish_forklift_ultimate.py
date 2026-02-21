from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Forklift Safety with Modules 5-12 at World-Class Density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Forklift Safety (Theory)')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Traveling and Maneuvering',
                    'content': """
                        <p>Traveling safely in a forklift requires a different mindset than driving a car. In 2026, the standard for warehouse navigation is <strong>Pedestrian Primacy</strong>. A forklift can weigh three times as much as a car and cannot stop on a dime. When traveling, the forks must be kept 4 to 6 inches off the ground, tilted back, and the operator must always look in the direction of travel. If a load is so large that it blocks your forward vision, the 2026 OSHA requirement is absolute: <strong>You must travel in reverse</strong>. Driving forward with a blocked view is a leading cause of warehouse fatalities.</p>
                        <p>Maneuvering involves managing the "Rear-End Swing." Because forklifts steer from the rear, the back of the truck swings out wide during a turn. Operators must maintain a "Safe Cushion" from racks, walls, and especially pedestrians. In 2026, we utilize the <strong>"Stop, Look, Listen"</strong> protocol at all intersections and "blind spots." This involves coming to a complete stop, sounding the horn, and checking overhead mirrors. Furthermore, operators must never "turn on a grade" (ramp or incline), as this immediately shifts the Center of Gravity outside the Stability Triangle, resulting in a lateral tip-over.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>If the load blocks your forward view, you must travel in reverse.</li><li>Be aware of "Rear-End Swing" and always sound the horn at intersections.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: 2026 Battery Safety and Lithium-Ion Charging',
                    'content': """
                        <p>The 2026 warehouse is rapidly transitioning from lead-acid to <strong>Lithium-Ion (Li-ion) battery systems</strong>. Li-ion technology allows for "Opportunity Charging"—plugging the truck in during short breaks or lunch periods without damaging the battery's lifespan. However, this introduces new fire risks. Li-ion batteries are susceptible to <strong>Thermal Runaway</strong> if they are physically damaged or overcharged. If a battery is hissing, swollen, or emitting a sweet smell, it is a medical and fire emergency. Isolate the truck and notify the fire department immediately, as these fires produce their own oxygen and are extremely difficult to extinguish.</p>
                        <p>For facilities still using lead-acid batteries, the hazards are chemical. These batteries produce <strong>Hydrogen Gas</strong> during charging, which is highly explosive. Charging areas must be well-ventilated, and "No Smoking" signs must be strictly enforced. When handling battery acid (electrolyte), you must wear specific PPE: acid-resistant gloves, a face shield, and a rubber apron. If acid splashes on your skin or eyes, you must use an emergency eyewash station for at least 15 minutes. In 2026, the "Battery Wash Station" is also a critical OSHA requirement to prevent the buildup of corrosive "white powder" (lead sulfate) on the battery casing.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Li-ion batteries allow for "Opportunity Charging" but can enter "Thermal Runaway" if damaged.</li><li>Lead-acid charging produces explosive hydrogen gas; proper ventilation is mandatory.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: LPG and Diesel Fueling Physics',
                    'content': """
                        <p>Internal Combustion (IC) forklifts typically run on <strong>Liquid Petroleum Gas (LPG)</strong> or Diesel. LPG is stored in pressurized cylinders as a liquid but turns into a gas when released. In 2026, the primary risk during LPG tank replacement is "Cold Burns" (frostbite). If LPG touches your skin, it will instantly freeze the tissue. You must wear leather or insulated gloves and eye protection when changing tanks. Before disconnecting, always close the tank valve and allow the engine to "run out" the remaining fuel in the lines. This ensures the coupling is not under pressure when you release it.</p>
                        
                        <p>Proper tank positioning is a non-negotiable safety step. LPG tanks have a "Positioning Pin" hole that ensures the internal "liquid dip tube" is facing the bottom of the tank. If the tank is mounted incorrectly, the engine may draw vapor instead of liquid, causing it to stall or run poorly. Furthermore, you must inspect the tank's O-ring for cracks. If you smell "rotten eggs," that is the odorant (mercaptan) added to the gas to warn you of a leak. Immediately move the truck to an outdoor area and close the valve. Never attempt to "find a leak" with a flame or by hand; use a soap-and-water solution to look for bubbles.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>LPG causes "Cold Burns"; wear gloves and eye protection when changing tanks.</li><li>Ensure the tank positioning pin is correctly seated to allow proper fuel flow.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Pedestrian Safety: Blue Lights and Red Zones',
                    'content': """
                        <p>In 2026, forklift-pedestrian accidents are mitigated by <strong>Active Visual Warning Systems</strong>. The most common is the "Blue Spotlight," which projects a bright blue dot on the floor 10 to 15 feet in front of or behind the moving forklift. This gives pedestrians a visual cue that a truck is approaching an intersection before they can see it. Additionally, many trucks now feature "Red Zone" LED strips that project a red boundary on the floor around the sides of the truck, marking the "Danger Zone" where the rear-end swing occurs. As an operator, you must ensure these lights are functional during your pre-shift inspection.</p>
                        <p>However, technology is not a substitute for <strong>Eye Contact</strong>. In a world-class safety culture, a pedestrian must never assume the operator sees them. Pedestrians should use hand signals to "wave" the forklift through, and the operator should acknowledge with a nod or a horn tap. If a pedestrian enters your "Red Zone," you must <strong>Stop the Truck Immediately</strong>. In 2026, many warehouses are implementing AI-based "Person Detection" cameras that will automatically slow or stop the forklift if a human is detected in its path. Even with these sensors, the operator remains 100% responsible for the safety of those around them.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Blue spotlights and Red Zone LEDs provide visual warnings to pedestrians.</li><li>Always maintain eye contact with pedestrians; stop immediately if they enter your safety zone.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Ramps, Inclines, and the "Load Up-Grade" Rule',
                    'content': """
                        <p>Driving on a ramp or incline is one of the most dangerous forklift maneuvers due to the shift in the Center of Gravity. In 2026, the rule of thumb is <strong>"Load Up-Grade."</strong> If you are carrying a load, the load must always be on the "up" side of the ramp. This means you drive forward when going up a ramp and drive in reverse when going down. This orientation ensures that the weight of the load is pushing into the forks and keeping the Center of Gravity centered over the drive axle. Traveling "Load Down-Grade" can cause the load to slide off the forks or, worse, tip the truck forward.</p>
                        
                        <p>When traveling <strong>unloaded</strong> on a ramp, the opposite is true: the "Counterweight" (the heavy back of the truck) should be on the "up" side. This means you drive in reverse when going up and forward when going down. Most importantly, <strong>Never Turn on a Ramp</strong>. Turning on an incline causes the Center of Gravity to move laterally toward the edge of the Stability Triangle. Even a small turn on a 10-degree slope can be enough to flip a forklift. If you must use a ramp, keep your speed low and your forks as low to the ground as possible to maintain a low Center of Gravity.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Load must always be on the "up" side of the ramp (drive up, reverse down).</li><li>Never turn the forklift on a ramp or incline; this causes immediate tip-overs.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Attachments and Data Plate Deratement',
                    'content': """
                        <p>Attachments—such as side-shifters, paper-roll clamps, or man-baskets—completely change the physics of the forklift. In 2026, OSHA requires that a forklift have a <strong>Data Plate</strong> that specifically lists the capacity of the truck <em>with that specific attachment</em>. Adding an attachment typically reduces the lifting capacity for two reasons: 1. The attachment itself has weight that must be subtracted from the total capacity. 2. The attachment usually moves the "Load Center" further away from the front wheels (the fulcrum), which reduces the truck's stability.</p>
                        <p>Operating a forklift with an unapproved or "homemade" attachment is a major OSHA violation. If you add an attachment, you must receive written approval from the forklift manufacturer, and a new data plate must be installed. In 2026, operators must also be aware of <strong>"Side-Shifting Physics."</strong> While a side-shifter is useful for aligning a load, shifting a heavy load to the extreme left or right moves the Center of Gravity toward the edge of the Stability Triangle. You should only use the side-shifter when the load is low to the ground; side-shifting a load at maximum lift height is a high-risk move that can cause a lateral tip-over.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Attachments reduce the total lift capacity and change the load center.</li><li>You must have a specific data plate for every attachment used on the truck.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Loading Docks, Trailers, and "Dock Walk"',
                    'content': """
                        <p>The loading dock is the most high-pressure and dangerous area of the warehouse. In 2026, the primary threat is <strong>"Trailer Creep" or "Early Departure."</strong> This occurs when the movement of the forklift in and out of the trailer causes the trailer to slowly move away from the dock, creating a gap. To prevent this, 2026 standards require <strong>Mechanical Dock Restraints</strong> (hook systems) or, at minimum, wheel chocks on both sides of the trailer. You must never enter a trailer until you have verified that the "Green Light" is on, signaling that the trailer is locked to the building.</p>
                        <p>A 2026 safety protocol is the <strong>"Nose Jack" Requirement</strong>. If you are loading an "un-coupled" trailer (one not attached to a tractor), the weight of the forklift entering the front of the trailer can cause the trailer to tip forward or "nose-dive." A nose jack must be placed under the front of the trailer to provide stability. Before entering, you must also inspect the trailer floor for "soft spots" or holes. In 2026, many trailers are being built with lighter materials that may not support the weight of a heavy electric forklift. If the floor looks suspicious, do not enter.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Trailers must be locked to the dock or chocked before entry.</li><li>Use a "Nose Jack" for un-coupled trailers to prevent them from tipping forward.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Safety Culture and AI Sensors',
                    'content': """
                        <p>The final module focuses on the <strong>Psychology of Operation</strong>. A world-class forklift operator understands that "Safety is not what you know, it\'s what you do when no one is watching." In 2026, we are seeing the integration of <strong>AI-Driven Safety Sensors</strong> that can automatically limit a truck\'s speed in "high-traffic zones" or shut down the motor if the operator is not wearing their seatbelt. While these tools are life-saving, they can also lead to "Complacency." An operator must never rely on a sensor to do the job of a safe driver.</p>
                        <p>We conclude with the <strong>"Zero Tolerance" for Tip-Overs</strong>. If your forklift begins to tip, the 2026 survival protocol is: <strong>Do Not Jump</strong>. Most forklift fatalities occur when an operator tries to jump clear and is crushed by the overhead guard (the "mousetrap" effect). Instead, stay in the seat, grip the steering wheel firmly, brace your feet, and lean *away* from the direction of the fall. Your seatbelt is your primary life-saving device in a tip-over. By maintaining your certification and staying vigilant, you are a professional guardian of the warehouse. Stay focused, stay buckled, and stay safe.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>AI sensors are a backup, not a replacement for a vigilant operator.</li><li>In a tip-over: Stay in the seat, brace your feet, and lean away from the fall.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Forklift Safety is now World-Class.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
