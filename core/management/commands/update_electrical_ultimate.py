from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Electrical Safety to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Electrical Safety')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Physics of Electrical Hazards',
                    'content': """
                        <p>Electrical energy is a silent and instantaneous hazard. In 2026, workplace electrical safety is governed by OSHA 29 CFR 1910 Subpart S and the NFPA 70E standard. To understand the risk, we must understand the physics: <strong>Voltage</strong> is the pressure, <strong>Current (Amps)</strong> is the flow, and <strong>Resistance (Ohms)</strong> is the opposition to that flow. It is a common misconception that "high voltage" is the only killer. In reality, it is the <strong>Amperage</strong> that stops the human heart. As little as 50 to 100 milliamperes (mA) flowing through the chest can cause ventricular fibrillation and death in seconds. For context, a standard 15-amp office circuit carries enough current to kill over 150 people simultaneously.</p>
                        <p>The human body is an excellent conductor of electricity due to its high water and electrolyte content. When a person becomes part of an electrical circuit, they experience <strong>Ohmic Heating</strong>, where the internal tissues and organs are literally cooked by the passage of current. This often results in "Entrance and Exit" wounds, where the most significant damage is hidden internally. 2026 safety protocols emphasize that any individual who receives a significant electrical shock—even if they appear fine—must receive an immediate EKG, as cardiac arrhythmias can manifest hours after the initial contact. Awareness of these physical properties is the foundation of the "Zero Trust" electrical mindset.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Current (Amperage) kills; as little as 50-100mA can cause fatal heart failure.</li><li>Electrical injuries are often internal; an EKG is mandatory after any major shock.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Arc Flash and Blast Dynamics',
                    'content': """
                        <p>An <strong>Arc Flash</strong> is a massive release of energy caused by an electrical fault that travels through the air between conductors. In 2026, Arc Flash is recognized as one of the most violent events in the industrial environment. The temperature of an arc flash can reach <strong>35,000°F</strong>—hotter than the surface of the sun. This intense heat causes the surrounding air to expand rapidly, creating an <strong>Arc Blast</strong>—a pressure wave that can throw workers across rooms, collapse lungs, and turn copper components into "molten shrapnel." Most arc flash incidents occur while a worker is performing maintenance or "troubleshooting" on energized equipment.</p>
                        
                        <p>The 2026 NFPA 70E standard requires an <strong>Arc Flash Risk Assessment</strong> before any work begins on equipment operating at 50 volts or more. This assessment determines the "Flash Protection Boundary" and the "Incident Energy" level, which dictates the level of Flame-Resistant (FR) clothing required. You must understand that standard cotton or synthetic clothing is a liability in an arc flash; synthetic fabrics will melt into the skin, causing horrific, non-treatable burns. Engineering controls, such as "Arc-Resistant Switchgear" and "Remote Racking" systems, are the preferred 2026 methods for protecting workers by moving them outside the blast radius during high-risk operations.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Arc Flash temperatures can reach 35,000°F, vaporizing metal and causing pressure waves.</li><li>NFPA 70E requires a risk assessment for all equipment over 50 volts.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Grounding and GFCI Protection',
                    'content': """
                        <p>Grounding is a secondary path for electrical current to return safely to the earth in the event of a fault. In 2026, the <strong>Ground Fault Circuit Interrupter (GFCI)</strong> is the primary life-saving device in wet or outdoor environments. A GFCI does not monitor for "overloads" like a circuit breaker; instead, it monitors the balance of current between the "Hot" and "Neutral" wires. If it detects a leakage as small as <strong>5mA</strong>—indicating that the current is flowing through something else (like a human body)—it will trip and shut off the power in as little as 1/40th of a second. This speed is what prevents a shock from becoming a fatality.</p>
                        <p>The "Missing Ground Pin" is a frequent 2026 OSHA citation. If the third (round) pin is broken off an electrical plug, the equipment is no longer grounded. In the event of an internal short, the metal casing of the tool becomes "live," and the next person to touch it will become the path to ground. 2026 standards require <strong>Assured Equipment Grounding Conductor Programs</strong> in construction and industrial settings, which involve regular testing and visual inspections of all cords and tools. Never "bypass" a ground or use an adapter that eliminates the grounding path; these actions turn a safe tool into a lethal instrument.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>GFCIs trip at 5mA of leakage current, preventing fatal electrocution.</li><li>Never use a tool with a missing or damaged ground pin.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Lockout/Tagout (LOTO) Mastery',
                    'content': """
                        <p>Lockout/Tagout (LOTO) is the primary "Administrative Control" for preventing the accidental energization of equipment during maintenance. In 2026, OSHA 1910.147 mandates a strict 6-step sequence: 1. <strong>Preparation</strong> (Identifying all energy sources). 2. <strong>Shutdown</strong>. 3. <strong>Isolation</strong> (Turning off the disconnect). 4. <strong>Application of LOTO</strong> (Physical locks and tags). 5. <strong>Stored Energy Control</strong> (Bleeding capacitors or pressure). 6. <strong>Verification</strong>. The final step—Verification—is the most skipped and most critical; you must "Try" to start the machine to ensure it is truly in a "Zero Energy State."</p>
                        
                        <p>A 2026 LOTO standard is "One Person, One Lock, One Key." You must never allow someone else to remove your lock, and you must never "loan" your key to a supervisor. If you are working in a group, a <strong>Group Lockbox</strong> must be used, where the key to the main equipment lock is placed inside a box, and every individual worker attaches their own personal lock to that box. This ensures that the machine cannot be turned on until the very last worker has finished their task and removed their lock. This "Physical Guarantee" of safety is the only way to work inside a machine with 100% confidence.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Verification (the "Try" step) is mandatory to confirm a Zero Energy State.</li><li>Each worker must use their own unique lock and key; never share or bypass.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Electrical Safety Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
