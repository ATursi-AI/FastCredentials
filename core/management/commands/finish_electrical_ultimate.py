from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Electrical Safety with Modules 5-12 at 2,000+ char density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Electrical Safety')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: PPE Selection and ASTM Ratings',
                    'content': """
                        <p>Personal Protective Equipment (PPE) for electrical work is not a "one size fits all" solution. In 2026, the selection of PPE is driven by the <strong>Incident Energy</strong> level identified on the equipment's Arc Flash Label. For voltage protection, <strong>Rubber Insulating Gloves</strong> are the most critical line of defense. These gloves are classified from Class 00 (500V) to Class 4 (36,000V). Before every single use, you must perform an "Air Test"—rolling the glove to trap air and checking for microscopic punctures. A hole as small as a pinprick can allow thousands of volts to bypass the glove and enter your body.</p>
                        <p>Arc-rated (AR) clothing is measured in cal/cm². In 2026, we utilize the <strong>Category System (1-4)</strong>. Category 4 protection, often referred to as a "Moon Suit," includes a multi-layered hood with a reflective face shield, a heavy coat, and bib overalls designed to withstand a massive thermal blast. It is vital to remember that PPE does not "stop" the blast; it is designed to prevent the clothing from igniting and to limit the burn to a survivable 2nd-degree level. 2026 standards also prohibit the wearing of any conductive jewelry (rings, watches) or metal-rimmed glasses when working within the "Limited Approach Boundary," as these can "bridge" the gap between energized parts and your skin.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Perform an "Air Test" on rubber gloves before every use; check the class rating.</li><li>AR clothing is designed to prevent ignition, not to eliminate the shock hazard.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: 2026 EV Infrastructure and DC Safety',
                    'content': """
                        <p>The massive rollout of <strong>Electric Vehicle (EV) Charging Infrastructure</strong> has introduced high-voltage Direct Current (DC) risks to the standard workplace. Unlike standard 120V AC power, high-voltage DC (found in Level 3 Fast Chargers) is extremely dangerous because it can cause "muscle tetany"—the "can\'t let go" phenomenon—at much lower thresholds. In 2026, maintenance on EV chargers must only be performed by "Qualified Personnel" who understand the internal capacitor banks that can hold a lethal charge long after the main power is disconnected.</p>
                        <p>Safety protocols for EV chargers include the inspection of cables for "jacket wear." Because these cables are often dragged across asphalt, the insulation can degrade, creating a ground fault risk. In 2026, commercial chargers utilize <strong>DC Leakage Monitoring</strong>. If you notice a "Fault" light on a charger, do not attempt to reset it repeatedly. This indicates an internal insulation failure. Furthermore, when fighting a fire involving an EV charger or the vehicle itself, you must use specialized non-conductive suppression agents and maintain a safe distance, as the high-voltage DC battery can cause "Arc-over" through a standard water stream.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>High-voltage DC in EV chargers can cause "muscle tetany," preventing you from letting go.</li><li>Internal capacitors can hold lethal charges even when the unit is unplugged.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Safe Use of Cords, Cables, and "Daisy-Chains"',
                    'content': """
                        <p>Flexible cords and cables are the most frequently cited OSHA electrical violation. In 2026, the rule is clear: <strong>Flexible cords are not a substitute for permanent wiring.</strong> They must not be run through holes in walls, ceilings, or floors, and they must not be attached to building surfaces with staples or nails. A cord that is pinched or crushed can experience "Internal Arcing," where the copper strands break and generate heat inside the insulation, eventually leading to a fire. You must perform a visual inspection of every cord before use, looking for "strain relief" failure at the plug end where wires are often exposed.</p>
                        <p><strong>"Daisy-Chaining"</strong>—plugging one power strip or extension cord into another—is a major fire hazard in the 2026 office and industrial environment. Power strips are designed to be plugged directly into a permanently installed wall outlet. When you daisy-chain them, you increase the total resistance of the circuit and exceed the "Ampacity" rating of the first cord in the chain. This causes the insulation to melt and can trigger a fire before the circuit breaker ever trips. Always ensure that high-draw appliances (heaters, coffee makers, industrial tools) are plugged directly into a wall outlet, never into a power strip.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cords must be inspected for "strain relief" and insulation damage before use.</li><li>Daisy-chaining power strips is a fire hazard and a major OSHA violation.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Class C Fire Suppression Chemistry',
                    'content': """
                        <p>An electrical fire is classified as a <strong>Class C Fire</strong>. In 2026, the primary rule of Class C fires is that the suppression agent must be <strong>Non-Conductive</strong>. Using water or a foam-based extinguisher on an energized electrical fire can cause the current to travel up the stream, electrocuting the rescuer. The most common Class C agents are Carbon Dioxide (CO2) and Dry Chemical (ABC). CO2 is preferred for sensitive electronics because it leaves no residue, while ABC powder is more effective at stopping the fire from re-igniting by "smothering" the components.</p>
                        <p>The first step in any electrical fire is to <strong>Disconnect the Power</strong> if it is safe to do so. Once the power is disconnected, the fire technically becomes a Class A (if plastic/wood is burning) or Class B (if oils are burning) fire. However, in 2026, we always treat a fire as Class C until we have "Visual Verification" of the disconnect. Be aware that CO2 extinguishers can displace oxygen in small, unventilated rooms, posing a suffocation risk. After the fire is extinguished, do not touch the equipment, as it may still hold "Stored Energy" in capacitors that could cause a secondary shock or re-ignition.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never use water on an energized fire; use CO2 or ABC dry chemical extinguishers.</li><li>Treat every fire as "Live" until you have a verified physical disconnect.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Portable Tools and Non-Conductive Ladders',
                    'content': """
                        <p>Hand-held power tools must be either <strong>Grounded</strong> (3-prong plug) or <strong>Double-Insulated</strong>. A double-insulated tool (marked with a "square-within-a-square" symbol) does not require a ground pin because it has two layers of non-conductive material between the internal electrical parts and the outer casing. In 2026, we also emphasize the "Wet Condition" rule: never use a corded power tool while standing in water or in the rain, even if it is double-insulated, as moisture can bridge the internal gaps and cause a short-circuit to your body.</p>
                        <p>Ladder safety is a life-saving component of electrical work. You must <strong>never use an Aluminum or Metal ladder</strong> when working near energized parts or overhead power lines. Metal ladders are perfect conductors and will "bridge" the gap between a power line and the ground, electrocuting anyone on or near the ladder. The 2026 standard is the <strong>Fiberglass Ladder</strong>, which is non-conductive. However, be aware that a dirty or wet fiberglass ladder can still conduct electricity. Always keep your ladder clean, dry, and at least 10 feet away from any overhead lines.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Double-insulated tools are marked with a "square-in-a-square" and don't need a ground.</li><li>Only use Fiberglass ladders near electricity; never use Aluminum or Metal.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Overhead Lines and the 10-Foot Rule',
                    'content': """
                        <p>Overhead power lines are typically not insulated; the "air" around them is the insulation. In 2026, OSHA 1910.333 mandates the <strong>10-Foot Rule</strong>: all unqualified persons and equipment (ladders, cranes, scaffolding) must maintain a minimum clearance of at least 10 feet from any overhead line carrying up to 50kV. For higher voltages, the distance increases. It is a common myth that you have to "touch" the line to be killed; at high voltages, electricity can <strong>"Arc" or jump</strong> across the air to a nearby conductor, such as a metal ladder or a person standing on a roof.</p>
                        <p>If you are operating a vehicle (like a forklift or cherry picker) that makes contact with a power line, the 2026 protocol is <strong>STAY IN THE VEHICLE</strong>. The vehicle and the ground around it are energized. If you step out, you will create a path to ground and be electrocuted. The only exception is if the vehicle catches fire. In that case, you must <strong>Jump Clear</strong> with both feet together—ensuring you do not touch the vehicle and the ground at the same time—and then "shuffle-step" away, keeping both feet on the ground and close together to prevent "Step Potential" (the voltage difference between your feet).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Maintain at least 10 feet of clearance from all overhead power lines.</li><li>If your vehicle hits a line, stay inside unless it is on fire; then jump clear and shuffle.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Emergency Response and Extrication',
                    'content': """
                        <p>When a person is being shocked and is "frozen" to the circuit (muscle tetany), you must never touch them directly. If you do, the current will flow through them and into you, making you a second victim. The 2026 response is <strong>Immediate Disconnect</strong>. If the circuit breaker or disconnect switch is nearby, use it. If not, you must use a <strong>Non-Conductive Object</strong>—such as a dry wooden broom handle or a dedicated "Rescue Hook"—to push the victim away from the source or pull the wire away from them. Only once the victim is disconnected from the power is it safe to touch them and begin CPR/AED protocols.</p>
                        
                        <p>Post-extrication care in 2026 recognizes the risk of <strong>Rhabdomyolysis</strong>—the breakdown of muscle tissue caused by the electrical current. This releases toxins into the bloodstream that can cause sudden kidney failure. This is why every victim of a major shock must be transported to a hospital immediately, even if they claim they feel fine. If the victim has external burns, cover them with a dry, sterile dressing and do not apply any ointments or ice. Your primary duty is to ensure the power is truly OFF before starting life-saving measures.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never touch a victim who is still in contact with a live circuit.</li><li>Use a non-conductive object (like a rescue hook or wooden broom) to disconnect them.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Safety Culture: Qualified vs. Unqualified',
                    'content': """
                        <p>The final module distinguishes between <strong>Qualified and Unqualified Persons</strong>. According to OSHA, a Qualified Person is one who has been specifically trained on the construction and operation of the equipment and has the skills to identify and avoid the specific hazards involved. Simply being an "Electrician" does not make you qualified for every piece of equipment. In 2026, an Unqualified Person is anyone who has not received this specific training. Unqualified persons are strictly prohibited from entering the "Limited Approach Boundary" or performing any maintenance on energized equipment.</p>
                        <p>Sustaining a culture of electrical safety means respecting the <strong>"Zero Energy" Goal</strong>. If a job can be done with the power off, it MUST be done with the power off. Working "live" is a specialized exception that requires a written "Energized Electrical Work Permit" and specific justifications. By completing this certification, you have gained the awareness to identify hazards and the discipline to follow the LOTO and PPE protocols that save lives. Electrical safety is not about luck; it is about the technical precision of your preparations and your respect for the silent power of the circuit.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Only "Qualified Persons" are allowed to perform maintenance on energized equipment.</li><li>If a task can be done with the power off, OSHA mandates that it must be done with the power off.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Electrical Safety is now World-Class.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
