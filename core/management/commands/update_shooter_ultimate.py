from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Active Shooter Preparedness to 10 Deep-Dive Tactical Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Active Shooter Preparedness')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Evolution of the Active Threat',
                    'content': """
                        <p>The term "Active Shooter" has evolved into a broader "Active Threat" landscape. In 2026, tactical analysis of mass casualty events shows that the average duration of these incidents is between 5 and 10 minutes—often ending before law enforcement arrives on the scene. This reality places the burden of initial survival entirely on the individuals present during the first moments of the attack. Understanding the "Active Shooter" definition—an individual actively engaged in killing or attempting to kill people in a confined and populated area—is critical because it dictates a response that is fundamentally different from a robbery or a hostage situation. In an active threat, the primary objective of the attacker is mass casualties, not negotiation or theft.</p>
                        <p>The 2026 survival paradigm is built on the <strong>OODA Loop</strong> (Observe, Orient, Decide, Act), a tactical decision-making framework developed by military strategist John Boyd. When an attack begins, the attacker is already in the "Act" phase, while the victims are usually in a state of "Normalcy Bias," where the brain tries to rationalize gunshots as fireworks or construction noise. To survive, you must break this bias immediately. The faster you can orient yourself to the reality of the threat, the faster you can move into an action that saves your life. Seconds are the currency of survival in these environments; a head start of just 15 seconds can be the difference between being in the "kill zone" and being behind a locked door.</p>
                        <p>This course utilizes the <strong>FBI and DHS-endorsed "Run, Hide, Fight"</strong> model, but with significantly more tactical depth than standard corporate training. We will move beyond the basics to explore the "why" behind these actions. Why does "Running" fail in certain architectural layouts? Why is "Hiding" ineffective without "Hardening"? How do you "Fight" an armed attacker as a group of unarmed civilians? By the end of this curriculum, you will have a mental "Crisis Blueprint" that allows you to bypass the paralyzing effects of fear and move directly into a survival-oriented state of mind.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Active threats typically last 5-10 minutes; you are the first responder.</li><li>The OODA Loop helps you break through normalcy bias and act faster.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: RUN: The Physics of Evacuation',
                    'content': """
                        <p>Evacuation (Running) is always your primary and most effective survival option, provided there is an accessible escape path. However, in 2026, tactical "Running" is defined as a <strong>purposeful movement toward cover</strong>, not a blind panic. When you choose to run, you must leave all non-essential belongings behind. Trying to grab a laptop or a bag wastes precious seconds and encumbers your movement. If you are in a group, encourage others to come with you, but do not wait for them if they are paralyzed by shock or insist on staying. Your survival depends on your individual movement.</p>
                        <p>Strategic evacuation involves understanding <strong>Linear vs. Non-Linear Movement</strong>. If you are in a long hallway, do not run down the center; stay close to the walls and look for "lateral" escapes—side doors, windows, or stairwells. If you are outside and being fired upon, move in a way that puts physical obstacles (cars, brick walls, trees) between you and the threat. Understand the difference between <strong>Concealment</strong> (something that hides you, like a bush) and <strong>Cover</strong> (something that stops a bullet, like an engine block or a concrete planter). Always move toward cover.</p>
                        <p>Once you have successfully evacuated the immediate danger zone, you must prevent others from entering the area. This is a critical community responsibility. As you reach a safe perimeter, do not stop; continue moving until you are significantly far away from the building. Do not huddle in large groups in the parking lot, as these can become secondary targets. Only when you are at a safe distance should you call 911. Be prepared to provide the "Five Critical Facts": Your location, the shooter’s location, number of shooters, physical description/weapons, and an estimate of victims.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Evacuate immediately and leave belongings; do not wait for others.</li><li>Understand the difference between Cover (stops bullets) and Concealment (only hides you).</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: HIDE: Hardening the Environment',
                    'content': """
                        <p>If evacuation is not possible, your objective shifts from movement to <strong>Hardening</strong>. Hiding is not merely sitting under a desk; it is the process of turning a soft target (an office or classroom) into a hard target that the attacker will likely bypass in favor of easier targets. The first step is to lock the door. In 2026, many attackers will test a door handle and, if it is locked, move on to the next room to maintain their momentum. However, a lock is only the first layer of defense. You must immediately begin <strong>Barricading</strong>.</p>
                        
                        <p>Effective barricading requires a tactical understanding of door mechanics. If the door opens <strong>inward</strong>, you should stack the heaviest furniture available (desks, filing cabinets, tables) against it. The goal is to create a physical mass that is difficult to push through. If the door opens <strong>outward</strong>, furniture is ineffective. In this case, you must secure the door handle to a fixed object (like a heavy table or a floor-mounted bracket) using a belt, a power cord, or a dedicated door-securing device. If no tether is available, a simple door wedge driven hard under the door can provide significant resistance.</p>
                        <p>Once the door is secured, you must "silence" the room. This means <strong>turning off the lights</strong>, closing any blinds or curtains, and silencing all cell phones—including vibration mode. A vibrating phone in a quiet room can alert an attacker to your presence. Move away from the door and any windows; stay low to the floor and spread out. Do not huddle in a single corner, as this makes it easier for a shooter to hit multiple people if they fire through the door. Maintain absolute silence and prepare for the possibility that the attacker may try to lure you out by pretending to be the police or an injured victim.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Lock and barricade doors; inward-opening doors need mass, outward-opening need tethers.</li><li>Silence phones completely (no vibrate) and stay away from doors/windows.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: FIGHT: The Tactics of Countering',
                    'content': """
                        <p>Fighting is your absolute last resort, to be used only when your life is in imminent danger and all other options have failed. In 2026, the mindset has shifted from "Fighting" to <strong>"Countering."</strong> This is not a fair fight; it is an aggressive, coordinated attempt to disrupt and incapacitate the attacker. If you are in a room with others, you must commit to a team-based defense. A single attacker, even one with a firearm, can be overwhelmed by a group of people acting with total aggression and speed. Decisiveness is your greatest weapon.</p>
                        <p>Tactical countering involves <strong>Distraction and Disruption</strong>. The human brain can only focus on one thing at a time. By throwing items (books, staplers, fire extinguishers) at the attacker’s face as they enter the room, you force them to flinch or blink, disrupting their "OODA Loop" and preventing them from aiming effectively. While they are distracted, "low-and-high" tackles should be initiated. One person targets the weapon, while others target the attacker’s limbs and head. Use your body weight to take them to the ground and do not stop until they are completely neutralized and the weapon is secured.</p>
                        <p>Improvised weapons are everywhere. A fire extinguisher can be sprayed to blind and choke the attacker before being used as a blunt instrument. A pair of scissors, a heavy trophy, or even a chair can be used to cause significant injury. When you commit to the fight, you must do so with <strong>absolute aggression</strong>. Do not hesitate. Yell loudly to disorient the shooter and provide yourself with a boost of adrenaline. This is a life-or-death struggle, and your only goal is to stop the attacker from hurting anyone else. Once the weapon is secured, place it in a trash can or away from you so arriving police do not mistake you for the shooter.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Countering is about total aggression and disrupting the attacker\'s focus.</li><li>Use improvised weapons and coordinate with others for a "low-and-high" attack.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Situational Awareness and Pre-Attack Indicators',
                    'content': """
                        <p>Situational Awareness is the practice of consciously observing your environment to identify potential threats before they materialize. In 2026, we utilize the "baseline" method: when you enter a space, quickly establish what is "normal" for that environment. What is the noise level? How are people behaving? Once the baseline is established, you look for <strong>Anomalies</strong>—individuals who are dressed inappropriately for the weather (e.g., a heavy coat in summer), people showing signs of extreme agitation, or individuals lingering in secure areas. Awareness is not paranoia; it is the skill of not being surprised.</p>
                        <p>Most active threats are not spontaneous; they are preceded by <strong>Pre-Attack Indicators</strong> or "Leakage." Leakage is the communication of intent to harm a third party, often through social media posts, diary entries, or verbal threats. Other red flags include a sudden, intense fascination with past mass shootings, the "stockpiling" of weapons, or a withdrawal from social groups combined with expressions of hopelessness or extreme anger. In the workplace, these indicators often follow a "grievance" such as a termination or a perceived injustice. Recognizing these signs early is the only way to prevent an attack before the first shot is fired.</p>
                        <p>The "See Something, Say Something" protocol is only effective if there is a clear, confidential reporting structure. 2026 standards mandate that organizations have a Threat Assessment Team (TAT) that can evaluate red flags objectively. Reporting concerning behavior is an act of safety, not an act of betrayal. By identifying a person in crisis early, the organization may be able to provide the necessary mental health interventions or security measures to de-escalate the threat. Awareness extends to the physical environment as well: notice propped-open doors, broken locks, or unauthorized individuals "tailgating" through secure entrances.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Establish a "baseline" for your environment and look for anomalies.</li><li>"Leakage" (sharing intent to harm) is the most common pre-attack indicator.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Active Shooter Ultimate (Part 1) pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
