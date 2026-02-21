from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Conflict Resolution to 12 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Conflict Resolution & De-escalation')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Aggression Cycle',
                    'content': """
                        <p>Conflict in the workplace rarely explodes out of nowhere; it follows a predictable <strong>Cycle of Aggression</strong>. It begins with the <strong>Trigger Phase</strong> (a denied request, a long wait time), escalates to the <strong>Agitation Phase</strong> (pacing, raised voice), peaks at the <strong>Explosion Phase</strong> (verbal abuse or violence), and eventually leads to the <strong>Recovery Phase</strong>. In 2026, your goal is to intervene during the Trigger or Agitation phase. Once the Explosion phase is reached, "rational" communication is impossible. You must shift from "Service Mode" to "Safety Mode."</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Intervene early in the Trigger or Agitation phase.</li><li>Rational negotiation fails during the Explosion phase; prioritize safety.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The "HEAT" Method for Verbal De-escalation',
                    'content': """
                        <p>When facing a verbally aggressive person, the 2026 industry standard is the <strong>HEAT Method</strong>: 1. <strong>Hear</strong> them out (do not interrupt). 2. <strong>Empathize</strong> (validate their feelings, not necessarily their behavior). 3. <strong>Apologize</strong> (for the situation, even if it's not your fault). 4. <strong>Take Action</strong> (resolve the issue or explain the next steps). "Hearing" is the most critical step; an angry person cannot listen to you until they feel they have been heard. Interrupting them during their "venting" phase will only reset their aggression clock.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Do not interrupt the "Venting" phase; let them run out of steam.</li><li>Validate feelings ("I understand why you are frustrated") to lower defenses.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Non-Verbal De-escalation: The "Open Stance"',
                    'content': """
                        <p>55% of communication is non-verbal. If your words say "Calm down" but your body says "Fight me," the conflict will escalate. In 2026, we teach the <strong>Open Stance</strong>: stand at a 45-degree angle to the person (not head-on), keep your hands visible and open (not crossed or clenched), and maintain a neutral facial expression. Standing "Squared Up" (chest-to-chest) is a primal challenge signal. By angling your body, you subconsciously signal that you are not a threat, while also protecting your vital organs if the situation turns physical.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Stand at a 45-degree angle to reduce the "challenge" signal.</li><li>Keep hands visible and open; clenched fists signal aggression.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Pre-Attack Indicators',
                    'content': """
                        <p>Violence is rarely random. People typically broadcast <strong>Pre-Attack Indicators</strong> before they strike. In 2026, you must recognize these signs instantly: 1. <strong>"Target Glancing"</strong> (looking around to see if anyone is watching). 2. <strong>"Clenching"</strong> (jaw tightening, fist balling). 3. <strong>"Thousand-Yard Stare"</strong> (ignoring you completely). 4. <strong>"Pacing"</strong> or sudden movements. If you see these signs, de-escalation has failed. You must immediately create distance, locate an exit, and call for security or law enforcement (Code Gray/Silver).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Target glancing and clenching are immediate warning signs of physical violence.</li><li>If you see these signs, stop talking and prioritize your exit.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Active Listening: The "Looping" Technique',
                    'content': """
                        <p>Active listening is the antidote to anger. In 2026, we use the <strong>"Looping" Technique</strong>: Listen to what the person says, and then repeat it back to them in your own words to confirm understanding. "So, what I'm hearing is that you are frustrated because your appointment was delayed. Is that correct?" This forces the person to stop shouting and engage their logical brain to verify your statement. It proves you are listening and breaks the "feedback loop" of their anger.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>"Looping" forces the aggressor to switch from emotional to logical processing.</li><li>Confirming understanding lowers the temperature of the interaction.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Setting Limits: The "Choice" Strategy',
                    'content': """
                        <p>You do not have to accept abuse. In 2026, we teach <strong>Limit Setting with Choices</strong>. Instead of saying "Stop yelling," say: "I want to help you, but I cannot do that while you are shouting. If you can lower your voice, we can solve this together. If you continue to shout, I will have to end this conversation. It is your choice." This puts the control back in their hands while firmly establishing your boundary. If they choose to continue, you must follow through on the consequence immediately.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Give the aggressor a choice: "Calm down and get help, or continue and I leave."</li><li>Follow through on the consequence immediately if the behavior continues.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Proxemics: The "Reactionary Gap"',
                    'content': """
                        <p><strong>Proxemics</strong> is the study of personal space. An angry person requires <em>more</em> space than a calm person. In 2026, you must maintain a <strong>Reactionary Gap</strong> of at least 4 to 6 feet (two arm lengths). This gives you time to react if they lunge at you and prevents you from invading their "intimate zone," which triggers a fight-or-flight response. Never corner an angry person; always ensure they have a clear path to the exit so they don't feel trapped.</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Maintain a 4-6 foot Reactionary Gap at all times.</li><li>Never corner an angry person; leave them an exit route.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Bystander Intervention in Conflict',
                    'content': """
                        <p>If you witness a coworker being harassed, you have a duty to intervene. In 2026, we use the <strong>"Tap Out" Protocol</strong>. If you see a colleague losing their cool or becoming a target, simply walk up and say, "Hey, [Name], there is a call for you on line 1," or "I can take it from here." This gives your colleague a graceful exit strategy to leave the situation and decompress. Supporting your team means recognizing when they are overwhelmed and stepping in before the conflict explodes.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use the "Tap Out" method to rescue a colleague from an escalating situation.</li><li>Provide a face-saving excuse for them to leave the interaction.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Digital Conflict: Emails and Chats',
                    'content': """
                        <p>Conflict isn't always face-to-face. <strong>Digital Aggression</strong> (rude emails, Slack attacks) is common in 2026. The rule is <strong>"Wait 30 Minutes."</strong> Never reply to a hostile message immediately. Draft your response, then walk away. Remove all "emotional" language. Stick to the facts. If a digital thread becomes heated, move it to a voice call or video meeting immediately. Text lacks tone, and 90% of digital conflicts are resolved once the parties hear each other's voices.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never reply to a hostile message instantly; wait 30 minutes.</li><li>Move heated text threads to voice/video calls to restore human tone.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: The "Grey Rock" Method for Chronic Aggressors',
                    'content': """
                        <p>Some individuals thrive on drama. For chronic complainers or narcissists, use the <strong>"Grey Rock" Method</strong>. Make yourself as uninteresting as a grey rock. Give short, factual, non-emotional answers ("Yes," "No," "I see"). Do not engage with their attempts to provoke you. By denying them the "emotional fuel" they crave, they will eventually lose interest and move on. This is a survival strategy for dealing with high-conflict personalities in the workplace.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Be uninteresting and non-emotional with chronic aggressors.</li><li>Deny them the "emotional reaction" they are seeking.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Debriefing and Recovery',
                    'content': """
                        <p>After a conflict, your body is flooded with adrenaline. You cannot return to work immediately. In 2026, we mandate a <strong>"Post-Incident Debrief."</strong> Take 10 minutes to walk, breathe, or talk to a supervisor. Discuss what went well and what could be improved. This "Emotional Hygiene" prevents burnout. If you suppress the stress, it will accumulate and lead to "Compassion Fatigue." You must process the event to put it behind you.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Take a mandatory 10-minute break after a high-stress conflict.</li><li>Debriefing prevents long-term burnout and compassion fatigue.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 "Calm Command" Mindset',
                    'content': """
                        <p>We conclude with the <strong>Calm Command</strong> mindset. In a chaotic situation, the person who remains calm is the one in charge. Your calmness is contagious. By mastering your own fight-or-flight response, controlling your breathing, and using the HEAT method, you become an anchor in the storm. Conflict resolution is not about "winning" the argument; it is about winning the peace. You are now a certified master of De-escalation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The calmest person in the room is the one in control.</li><li>Your goal is to "win the peace," not the argument.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)

            # --- EXAM (15 QUESTIONS) ---
            qs = [
                ('What is the first step of the "HEAT" method?', ['Hurry up', 'Hear them out (Do not interrupt)', 'Hide', 'Hit back'], 2),
                ('At which phase of the Aggression Cycle should you intervene?', ['Explosion Phase', 'Trigger or Agitation Phase', 'Recovery Phase', 'Never'], 2),
                ('What is the "Reactionary Gap" distance?', ['1 foot', '4 to 6 feet (two arm lengths)', '10 feet', 'Touching distance'], 2),
                ('What does the "Open Stance" look like?', ['Arms crossed, staring', 'Standing sideways at 45 degrees, hands open and visible', 'Back turned', 'Lying down'], 2),
                ('What is a "Pre-Attack Indicator"?', ['Smiling', 'Target Glancing, Clenching fists, Thousand-Yard Stare', 'Laughing', 'Sleeping'], 2),
                ('What is the "Tap Out" protocol?', ['A wrestling move', 'Stepping in to relieve a coworker who is being harassed', 'Quitting your job', 'Leaving for lunch'], 2),
                ('Why should you wait 30 minutes before replying to a hostile email?', ['To let the internet load', 'To let emotions cool and draft a factual response', 'To ignore them', 'To ask a lawyer'], 2),
                ('What is "Looping" in active listening?', ['Walking in circles', 'Repeating back what the person said in your own words to confirm understanding', 'Ignoring the person', 'Recording the conversation'], 2),
                ('What is the "Grey Rock" method?', ['Throwing rocks', 'Being as uninteresting and non-emotional as possible to deny drama', 'Yelling back', 'Hiding under a desk'], 2),
                ('If someone is in the "Explosion Phase," what is your priority?', ['Reasoning with them', 'Safety and exit strategies', 'Offering them coffee', 'Laughing at them'], 2),
                ('Why should you not say "Calm Down" to an angry person?', ['It usually makes them angrier', 'It works perfectly', 'It is too long', 'It is illegal'], 1),
                ('What is the purpose of a "Post-Incident Debrief"?', ['To punish the employee', 'To process the event, reduce stress, and prevent burnout', 'To write a book', 'To waste time'], 2),
                ('What does "Proxemics" refer to?', ['The study of rocks', 'The study of personal space', 'The study of conflict', 'The study of words'], 2),
                ('When setting limits, what should you offer?', ['A threat', 'A choice (e.g., "Lower your voice or I must leave")', 'Money', 'Candy'], 2),
                ('Who is in control during a chaotic situation?', ['The loudest person', 'The person who remains calm', 'The customer', 'No one'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Conflict Resolution is World-Class (24/24 Complete). ONE STOP SHOP ACHIEVED.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
