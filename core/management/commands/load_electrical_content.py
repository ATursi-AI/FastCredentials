from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Loads 10 General Industry Electrical Safety Modules (Universal Audience)'

    def handle(self, *args, **kwargs):
        # 1. FIND THE COURSE
        try:
            course = Course.objects.get(title="Electrical Safety")
            self.stdout.write(self.style.SUCCESS(f"Found Course: '{course.title}'"))
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR("Error: Course 'Electrical Safety' not found."))
            return

        # 2. CLEAR OLD CONTENT
        Lesson.objects.filter(course=course).delete()
        self.stdout.write("Old lessons cleared.")

        # 3. DEFINE THE 10 MODULES
        lessons = [
            {
                "title": "Module 1: What's New in 2026 - Lithium & Cords",
                "order": 1,
                "content": """
                <h3>The 2026 Focus: Batteries & Power Strips</h3>
                <p>As we enter 2026, the biggest change in electrical safety isn't just about wall outlets—it's about what we plug into them. OSHA and fire marshals have issued new warnings regarding <strong>Lithium-Ion Batteries</strong>. From personal cell phones to custodial floor scrubbers and "Workstations on Wheels," these batteries pose a significant fire risk if damaged or charged improperly. 2026 guidance requires that any battery showing signs of swelling, overheating, or physical damage be removed from service immediately. Never leave charging devices on soft surfaces like couches or piles of paper where heat cannot escape.</p>
                
                <p>There is also renewed enforcement on <strong>Daisy-Chaining</strong> (plugging a power strip into another power strip). This is now a "Top 5" citation for schools, offices, and hospitals alike. Whether you are a teacher daisy-chaining cords for a projector or a janitor extending a vacuum cord, this practice creates excessive resistance and heat, leading to fires.</p>

                <p><strong>Extension Cord "Sunset" Rules:</strong> New guidelines emphasize that extension cords have an "expiration date" of use. They are permitted for <em>temporary</em> tasks only (e.g., drilling a hole, vacuuming a hallway). They generally cannot be used as a permanent solution for more than 90 days (or 24 hours in some healthcare settings). If you need a permanent outlet, one must be installed.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Lithium Batteries:</strong> Swollen or hot batteries are fire hazards; remove them from service.</li>
                        <li><strong>Daisy-Chaining:</strong> Never plug a power strip into another power strip.</li>
                        <li><strong>Extension Cords:</strong> For temporary use only, never permanent.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 2: How Electricity Works (The Basics)",
                "order": 2,
                "content": """
                <h3>The Water Analogy</h3>
                <p>Electricity can be invisible and silent, making it dangerous. To understand it, think of water flowing through a hose:</p>
                <ul>
                    <li><strong>Voltage (Volts):</strong> This is the <em>pressure</em> pushing the water. High voltage means high pressure.</li>
                    <li><strong>Current (Amps):</strong> This is the <em>volume</em> of water flowing. This is what actually hurts you.</li>
                    <li><strong>Resistance (Ohms):</strong> This is the size of the hose. A narrow hose (high resistance) restricts flow; a wide hose (low resistance) lets it rush through.</li>
                </ul>

                <p><strong>The Human Body:</strong> Your body is basically a bag of saltwater, which makes you a great conductor (like a wide hose). If you touch a live wire, you become part of the circuit. The electricity flows through you to the ground. If your skin is dry, you have some resistance. If your skin is wet (sweat, rain, or spilled water), your resistance drops to almost zero, allowing a massive amount of current to flow through your organs.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Amps (Current):</strong> This is the factor that causes injury or death.</li>
                        <li><strong>Conductors:</strong> Water and metal conduct electricity. Your body is mostly water.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 3: The Fatal Shock",
                "order": 3,
                "content": """
                <h3>It Takes Less Than You Think</h3>
                <p>Many people think it takes massive high-voltage lines to kill. In reality, standard 110-volt wall outlets are the most common cause of electrocution. It takes a tiny amount of current to disrupt your heart's rhythm.</p>

                <p><strong>The Danger Scale:</strong></p>
                <ul>
                    <li><strong>1 Milliamp (mA):</strong> A faint tingle.</li>
                    <li><strong>5 mA:</strong> Slight shock, not painful, but disturbing.</li>
                    <li><strong>10-20 mA:</strong> "The Let-Go Threshold." Your muscles contract violently, and you <em>cannot let go</em> of the wire. You are trapped.</li>
                    <li><strong>50-100 mA:</strong> Ventricular Fibrillation. Your heart stops pumping effectively. Death occurs in minutes without CPR.</li>
                </ul>

                <p>For context, a standard 100-watt lightbulb draws about 850 milliamps. That is 8 times the amount needed to kill a human being. Respect every outlet.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Let-Go Threshold:</strong> At ~10mA, muscles freeze, and you cannot let go of the shocking object.</li>
                        <li><strong>Lethality:</strong> Household current is more than enough to be fatal.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 4: Grounding & The Third Prong",
                "order": 4,
                "content": """
                <h3>Your Safety Valve</h3>
                <p>Have you ever seen a plug with three prongs? That round bottom prong is the "Ground." It is the most important safety feature on the device. If a wire breaks inside a metal vacuum cleaner or coffee pot, the electricity might touch the metal casing. Without a ground, the next person to touch that machine gets shocked.</p>

                <p>With a ground prong, that stray electricity is instantly sent deep into the earth, tripping the circuit breaker and shutting off the power before anyone gets hurt.</p>

                <p><strong>Never</strong> break off the third prong to fit a 3-prong plug into an old 2-prong outlet. <strong>Never</strong> use a "Cheater Plug" (grey adapter) to bypass this safety feature. If you find a tool or appliance with a missing ground prong, tag it "Do Not Use" and report it to maintenance immediately.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Ground Pin:</strong> Directs dangerous stray electricity to the earth.</li>
                        <li><strong>Rule:</strong> Never use a plug with a broken or missing third prong.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 5: Cord Safety Basics",
                "order": 5,
                "content": """
                <h3>Inspect Before You Connect</h3>
                <p>Power cords are the weak link in electrical safety. They get stepped on, rolled over by carts, and pinched in doors. Before you plug in any device—whether it's a floor buffer, a laptop charger, or a toaster—look at the cord.</p>

                <ul>
                    <li><strong>Fraying:</strong> Are the inner wires exposed?</li>
                    <li><strong>Cracks:</strong> Is the insulation brittle or broken?</li>
                    <li><strong>Tape:</strong> Has someone tried to fix it with electrical tape?</li>
                </ul>

                <p><strong>The "No Tape" Rule:</strong> Taping a damaged cord is prohibited in workplaces. Tape hides the damage and does not restore the cord's insulation rating. Damaged cords must be replaced, not repaired.</p>

                <p><strong>Unplugging:</strong> Always pull by the heavy rubber <em>plug</em>, never yank the cord itself. Yanking breaks the internal wires, creating a hidden fire hazard.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Inspection:</strong> Check for frays and cracks before every use.</li>
                        <li><strong>No Tape:</strong> Never use a cord wrapped in electrical tape.</li>
                        <li><strong>Pull the Plug:</strong> Never yank the cord to unplug a device.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 6: Power Strips & Overloading",
                "order": 6,
                "content": """
                <h3>The Daisy-Chain Danger</h3>
                <p>Power strips are convenient, but they are easy to abuse. The most common violation in schools and offices is <strong>Daisy-Chaining</strong>: plugging a power strip into another power strip or extension cord to reach a far wall.</p>

                <p>Power strips are not designed to handle the combined load of another strip. This creates a "bottleneck" of current that generates intense heat, often melting the plastic housing and starting a fire. Wall outlets are designed for a specific limit (usually 15 or 20 amps).</p>

                <p><strong>Space Heaters:</strong> Never plug a high-draw appliance like a space heater, microwave, or coffee maker into a power strip. These devices draw massive amounts of power and can easily melt a standard plastic strip. Plug them directly into the wall.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>No Daisy-Chaining:</strong> One power strip per wall outlet. Never series-connect them.</li>
                        <li><strong>High Power Devices:</strong> Heaters and kitchen appliances must go directly into the wall.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 7: Water, Wet Hands & GFCIs",
                "order": 7,
                "content": """
                <h3>Mixing Water and Watts</h3>
                <p>Water lowers resistance. If you touch a switch with wet hands, the current can jump to your skin much easier than if you were dry. This is why bathrooms, kitchens, and janitorial closets are high-risk zones.</p>

                <p><strong>GFCI (Ground Fault Circuit Interrupter):</strong> You've seen these outlets—they have the "Test" and "Reset" buttons in the middle. They monitor the electricity leaving and returning. If even a tiny amount "leaks" (like into a sink or a person), the GFCI snaps the power off in 1/40th of a second, faster than a heartbeat.</p>

                <p>If you are working with water (mopping, washing dishes), ensure you are plugged into a GFCI outlet. If a GFCI trips, do not just reset it. It did its job. Check the device for water damage or faults before trying again.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Wet Hands:</strong> Dry your hands completely before touching plugs or switches.</li>
                        <li><strong>GFCI:</strong> Mandatory safety outlets for any wet area (kitchens, bathrooms).</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 8: Lockout / Tagout (LOTO) for General Staff",
                "order": 8,
                "content": """
                <h3>The Red Lock Means STOP</h3>
                <p>You may see a breaker box, a machine, or a switch with a special <strong>Red Lock</strong> and a tag on it. This is part of the <strong>Lockout / Tagout (LOTO)</strong> safety procedure.</p>

                <p>It means a qualified electrician or mechanic is working on that machine, possibly with their hands inside the gears or wires. They have physically locked the power "OFF" so no one can accidentally turn it on.</p>

                <p><strong>Your Rule:</strong> If you see a lock and tag, <strong>stay away</strong>. Never attempt to bypass it, cut it, or turn the machine on. Even if the machine looks fine, turning it on could kill the person working on the other side of the wall. Only the person who put the lock on is allowed to take it off.</p>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Red Lock/Tag:</strong> Do not touch. Do not attempt to turn on.</li>
                        <li><strong>Life Safety:</strong> LOTO protects the life of the worker fixing the equipment.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 9: Electrical Fires",
                "order": 9,
                "content": """
                <h3>Class C Fires</h3>
                <p>Electrical fires are different from wood or paper fires. They are <strong>Class C</strong> fires, meaning the fuel source is energized.</p>

                <p><strong>NEVER use water</strong> on an electrical fire. Water conducts electricity. If you throw a bucket of water on a burning computer or panel, the electricity will travel up the water stream and electrocute you instantly.</p>

                <p><strong>Steps to take:</strong></p>
                <ol>
                    <li><strong>Unplug/Disconnect:</strong> If it is safe, pull the plug or flip the breaker. Once power is cut, it becomes a normal fire.</li>
                    <li><strong>Extinguish:</strong> Use a fire extinguisher rated <strong>C</strong> (usually CO2 or Dry Chemical). Most general extinguishers are rated "ABC" and are safe to use.</li>
                    <li><strong>Evacuate:</strong> Electrical fires produce toxic plastic smoke. Get out if you can't control it immediately.</li>
                </ol>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Water:</strong> NEVER use water on an electrical fire.</li>
                        <li><strong>Class C:</strong> The classification for energized electrical fires.</li>
                    </ul>
                </div>
                """
            },
            {
                "title": "Module 10: Emergency Response",
                "order": 10,
                "content": """
                <h3>Don't Become Victim #2</h3>
                <p>If you see someone being shocked (they may be frozen, shaking, or unable to let go of a wire), your instinct will be to grab them and pull them away. <strong>DO NOT TOUCH THEM.</strong></p>

                <p>If you touch them while they are electrified, the current will flow through them and into you. You will become part of the circuit and freeze alongside them.</p>

                <p><strong>The Correct Action:</strong></p>
                <ol>
                    <li><strong>Cut the Power:</strong> Unplug the device or hit the emergency shutoff button immediately.</li>
                    <li><strong>Push Away (If power can't be cut):</strong> Use a <strong>non-conductive object</strong> like a dry wooden broom handle, a plastic bin, or a dry belt to push the person away from the source.</li>
                    <li><strong>Call 911:</strong> Once they are free, check for breathing. Electrical shock often stops the heart. Begin CPR if you are trained.</li>
                </ol>

                <div class="alert alert-info mt-4">
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li><strong>Do Not Touch:</strong> You will be shocked if you touch an energized victim.</li>
                        <li><strong>First Move:</strong> Cut the power source immediately.</li>
                    </ul>
                </div>
                """
            }
        ]

        # 4. INSERT INTO DATABASE
        for lesson_data in lessons:
            Lesson.objects.create(
                course=course,
                title=lesson_data['title'],
                order=lesson_data['order'],
                content=lesson_data['content']
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(lessons)} universal modules for {course.title}"))
