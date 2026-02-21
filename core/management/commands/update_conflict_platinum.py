from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades Conflict Resolution to Platinum Standard (High Density)'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Conflict Resolution & De-escalation')
            # We keep the questions, only rewriting the lesson content for density.
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Physiology of Aggression and the "Amygdala Hijack"',
                    'content': """
                        <p>To master de-escalation, one must first understand the biology of violence. Aggression is rarely a random choice; it is a physiological cascade known as the <strong>"Amygdala Hijack."</strong> When a person feels threatened (whether the threat is physical safety or a blow to their ego), the amygdala takes over the brain's processing, bypassing the prefrontal cortex (the center of logic and reason). In this state, the aggressor is physically incapable of processing complex sentences or logical arguments. Their body is flooded with adrenaline and cortisol, leading to "Auditory Exclusion" (temporary deafness) and "Tunnel Vision."</p>
                        <p>The 2026 standard for crisis intervention recognizes four distinct phases of this cycle: 
                        <br><strong>1. The Trigger Phase:</strong> The initial deviation from baseline behavior. The person may seem withdrawn or subtly sarcastic. This is the <em>only</em> time rational intervention is highly effective.
                        <br><strong>2. The Escalation Phase:</strong> The body prepares for "Fight or Flight." You will see physical signs: pacing, clenching of the jaw, flushed skin, and rapid breathing. The voice raises in pitch and volume. 
                        <br><strong>3. The Crisis (Explosion) Phase:</strong> Rational thought is suspended. The person may scream, swear, or become physically violent. In this phase, your goal shifts entirely from "Resolution" to "Safety."
                        <br><strong>4. The Recovery Phase:</strong> As adrenaline fades, the person may become exhausted, confused, or remorseful. This is the "Post-Crisis Drain." 
                        <br>Understanding these phases prevents you from making the fatal mistake of trying to "reason" with a brain that is currently chemically incapable of logic.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "Amygdala Hijack" physically prevents an aggressor from processing logic.</li><li>Identify the "Trigger Phase" early; it is the window of opportunity for rational intervention.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Advanced Verbal De-escalation: The HEAT & LARA Models',
                    'content': """
                        <p>Verbal de-escalation is a strategic negotiation. In 2026, we utilize the <strong>HEAT Model</strong> for customer-facing conflicts and the <strong>LARA Model</strong> for high-stakes emotional crises. 
                        <br><strong>The HEAT Model:</strong>
                        <br><strong>1. Hear:</strong> Allow the person to vent without interruption. This "exhausts the energy" of the initial burst. If you interrupt, you reset their internal clock.
                        <br><strong>2. Empathize:</strong> Use "Validation Scripts" such as "I can see why that would be incredibly frustrating" or "It makes sense that you are angry about this." Validation is not agreement; it is acknowledgement.
                        <br><strong>3. Apologize:</strong> Apologize for the <em>situation</em> or the <em>experience</em>, not necessarily for your actions. "I am sorry you are going through this process."
                        <br><strong>4. Take Action:</strong> pivot to the future. "Here is what I can do for you right now."</p>
                        <p><strong>The LARA Model (Listen, Affirm, Respond, Add):</strong> Used when the aggressor is seeking a fight. <strong>Affirm</strong> their central value ("You care about getting this done right") before you <strong>Respond</strong> to their specific complaint. This separates the person's identity from the problem, lowering their defensive walls. 2026 protocols strictly forbid phrases like "Calm down," "Relax," or "It's not policy," as these are known "High-Risk Triggers" that escalate 90% of interactions.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never interrupt the "Venting" phase; it resets the aggression cycle.</li><li>Avoid command phrases like "Calm down"; use validation scripts instead.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Non-Verbal Dynamics and the "Reactionary Gap"',
                    'content': """
                        <p>Research indicates that 55% of communication is body language, 38% is tone, and only 7% is the actual words spoken. If your body language signals dominance or fear, your words are irrelevant. The 2026 standard for safe positioning is the <strong>"Reactionary Gap."</strong> You must maintain a distance of at least <strong>4 to 6 feet</strong> (two arm lengths) from an agitated person. This distance provides you with the time to react if they strike (the "OODA Loop" delay) and keeps you out of their "Intimate Zone," preventing the sensation of being trapped.</p>
                        <p>Your physical stance is a constant signal. Avoid the "Squared-Up" stance (chest to chest, toes pointing at the subject), as this is evolutionarily wired as a "Challenge Stance." Instead, adopt the <strong>"Interview Stance"</strong> (also known as the Field Inquiry Stance):
                        <br>1. Stand at a 45-degree angle to the subject. This minimizes your target profile and signals non-aggression.
                        <br>2. Keep your hands open and visible between your waist and chest (the "Safety Zone"). Hidden hands signal a threat; crossed arms signal dismissal.
                        <br>3. Keep your knees slightly bent and weight balanced. 
                        <br>By controlling your micro-behaviors—relaxing your eyebrows, unclenching your jaw—you can subconsciously influence the aggressor's mirror neurons to mimic your calmness.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Maintain a Reactionary Gap of 4–6 feet to ensure reaction time.</li><li>Use the 45-degree "Interview Stance" to signal non-aggression and protect your centerline.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Pre-Attack Indicators and "Code Gray" Protocols',
                    'content': """
                        <p>Violence is rarely spontaneous; it is "telegraphed" through specific biological markers known as <strong>Pre-Attack Indicators</strong>. In 2026, situational awareness means recognizing these subtle cues before the first punch is thrown.
                        <br><strong>The "Big 5" Indicators:</strong>
                        <br><strong>1. Target Glancing:</strong> The subject looks around to see if there are witnesses or cameras, or looks at a specific part of your body (chin, nose) where they intend to strike.
                        <br><strong>2. The "Thousand-Yard Stare":</strong> The subject breaks eye contact and looks "through" you. This indicates they have shut down verbal processing and are preparing for physical action.
                        <br><strong>3. Clenching:</strong> Rhythmic clenching of the jaw or fists ("knuckle popping").
                        <br><strong>4. Weight Shifting:</strong> Subtle shifting of weight to the back foot to prepare for a lunge or strike.
                        <br><strong>5. Radical Fluctuation:</strong> A sudden, unexplained drop in volume. If a screaming person suddenly goes deadly silent, an attack is imminent.</p>
                        <p>If you observe these indicators, you must initiate <strong>"Disengagement Protocols."</strong> Do not turn your back. Step backwards at a 45-degree angle toward an exit while keeping your hands up in a "defensive" but "open" gesture (the "Stop" motion). In healthcare and corporate settings, this is the trigger for a <strong>"Code Gray"</strong> (Security Assistance Needed) or <strong>"Code Silver"</strong> (Weapon/Hostage Situation). Your survival instinct must override your desire to "fix" the customer service issue.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Target glancing and sudden silence are high-probability indicators of imminent violence.</li><li>If observed, initiate Disengagement Protocols immediately; do not turn your back.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Active Listening: The "Looping" and "Fogging" Techniques',
                    'content': """
                        <p>Active listening is not just "hearing"; it is a tactical maneuver to lower the emotional temperature. The 2026 curriculum emphasizes two advanced techniques: <strong>Looping</strong> and <strong>Fogging</strong>.
                        <br><strong>Looping:</strong> This technique forces the aggressor's brain to switch from the emotional amygdala to the logical prefrontal cortex. You listen to their rant, strip away the abuse, isolate the core fact, and repeat it back to them. "So, if I understand correctly, you are upset because the billing department did not return your call on Tuesday. Is that right?" The requirement to verify your statement forces them to pause, think, and say "Yes." Getting a "Yes" breaks the cycle of "No" and resistance.
                        <br><strong>Fogging:</strong> Used when dealing with personal insults. Instead of defending yourself ("I am not stupid!"), you agree with a small probability of truth in their statement. Aggressor: "You are all incompetent idiots!" You: "I can see how our failure to call you back would make us seem incompetent." By refusing to fight back, you become like fog—there is nothing for their anger to hit. This exhausts the aggressor quickly as they are denied the conflict they seek.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Looping forces the aggressor to engage their logical brain to verify facts.</li><li>Fogging deflects insults by finding a grain of truth, denying the aggressor a target.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Limit Setting: The "Choice" Strategy',
                    'content': """
                        <p>De-escalation does not mean being a doormat. You must set boundaries to protect your safety and dignity. The 2026 standard is <strong>Limit Setting with Choices</strong> (The A-B Choice Model). Direct commands ("Stop yelling!") usually trigger defiance. Instead, offer two choices where <em>you</em> are happy with either outcome.
                        <br><strong>The Structure:</strong>
                        <br>1. Validate the feeling.
                        <br>2. Set the boundary (The Behavior).
                        <br>3. Offer the Choice (The Consequence).
                        <br><strong>Example:</strong> "Sir, I want to help you fix this billing error (Validate), but I cannot understand you when you are shouting (Boundary). If you can lower your voice, we can fix this right now (Choice A). If you continue to shout, I will have to end this call and you can try again tomorrow (Choice B). The choice is yours."
                        <br>This technique puts the onus of the consequence on <em>their</em> behavior, not your authority. If they continue, you <strong>must</strong> follow through immediately. Empty threats destroy your credibility and escalate future conflicts.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never give a command; offer an A-B Choice where you accept either outcome.</li><li>Consistency is key: if the behavior continues, the consequence must be immediate.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: The "Tap-Out" System and Bystander Intervention',
                    'content': """
                        <p>Conflict takes a physiological toll. As cortisol rises, your own ability to think clearly diminishes (Compassion Fatigue). 2026 workplace safety protocols mandate a <strong>"Tap-Out" System</strong>. This is a non-verbal agreement among teams. If you see a colleague losing their cool, becoming flushed, or getting stuck in a circular argument, you have a duty to intervene.
                        <br><strong>The Intervention Script:</strong> Do not ask "Do you need help?" (which implies incompetence). Instead, use a "Procedural Interruption." Walk up and say, "Excuse me, [Name], there is a Priority One call for you on Line 2, I can take over here."
                        <br>This allows your colleague to leave the situation with their dignity intact ("saving face") while resetting the interaction with the aggressor. A new face often breaks the cycle of conflict because the aggressor has to start their story over, often with less intensity. <strong>"Tagging In"</strong> is not an insult to your coworker; it is a safety maneuver to prevent burnout and escalation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use the "Tap-Out" system to rescue colleagues who are becoming emotionally compromised.</li><li>A "Procedural Interruption" allows the colleague to exit gracefully without losing face.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Digital Aggression and Remote Conflict',
                    'content': """
                        <p>In the hybrid workforce of 2026, conflict often occurs without visual cues. <strong>Digital Aggression</strong> (hostile Slack messages, ALL CAPS emails, passive-aggressive copying of bosses) requires a different toolkit. Text lacks tone, often leading to the "Negativity Bias" where neutral messages are read as hostile.
                        <br><strong>The 2026 Digital Protocol:</strong>
                        <br><strong>1. The 30-Minute Rule:</strong> Never reply to a hostile message immediately. The "Send" button is the enemy of de-escalation. Draft your response, then wait 30 minutes.
                        <br><strong>2. The Channel Switch:</strong> If a text thread goes back and forth more than three times with rising tension, you MUST switch channels. Move from Text -> Voice or Video. Hearing a human voice re-engages the empathy centers of the brain.
                        <br><strong>3. The "BIFF" Response:</strong> Keep responses Brief, Informative, Friendly, and Firm. Strip out all adjectives, adverbs, and emotional justifications.
                        <br><strong>4. Screenshot and Document:</strong> Digital harassment is permanent. Do not delete hostile messages; archive them for HR review if the pattern continues.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>If a digital conflict escalates, switch to voice or video immediately (The 3-Reply Rule).</li><li>Use the BIFF method (Brief, Informative, Friendly, Firm) for all written responses.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: The "Grey Rock" Method for High-Conflict Personalities',
                    'content': """
                        <p>While most conflict is situational, some is driven by personality disorders (Narcissistic, Histrionic, or Antisocial traits). These "High-Conflict Personalities" (HCPs) do not seek resolution; they seek <strong>Emotional Fuel</strong>. They thrive on your frustration, fear, or anger. Trying to "explain" or "defend" yourself only feeds the fire.
                        <br><strong>The Strategy: The Grey Rock Method.</strong>
                        <br>You must become as uninteresting and unreactive as a grey rock. 
                        <br>1. <strong>Monosyllabic Responses:</strong> "Okay." "I see." "Understood."
                        <br>2. <strong>No Eye Contact (if safe):</strong> Look at paperwork or a screen while listening.
                        <br>3. <strong>Zero Emotion:</strong> Keep your face blank and your voice monotone.
                        <br>By denying them the emotional payoff (the "Supply"), they will eventually get bored and move on to a softer target. This is not "rude"; it is a psychological boundary required for self-preservation against chronic manipulators.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>High-Conflict Personalities seek emotional reactions, not solutions.</li><li>"Grey Rocking" denies them emotional fuel by remaining boring and unreactive.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Trauma-Informed Care and "Psychological First Aid"',
                    'content': """
                        <p>In 2026, we recognize that many aggressors are acting out of unrecognized trauma. <strong>Trauma-Informed De-escalation</strong> shifts the question from "What is wrong with you?" to "What happened to you?" An angry patient in an ER or a frustrated client may be reacting to a loss of control that triggers a past trauma response.
                        <br><strong>Psychological First Aid (PFA) Principles:</strong>
                        <br><strong>1. Safety:</strong> Ensure they feel physically safe and not trapped.
                        <br><strong>2. Calming:</strong> Model calmness. "I am here. You are safe. We are going to figure this out."
                        <br><strong>3. Connectedness:</strong> Use their name. Establish a human connection before a bureaucratic one.
                        <br><strong>4. Self-Efficacy:</strong> Give them a small task or control over a small detail. "Would you like a glass of water?" or "Do you want to sit here or there?" Restoring a tiny amount of control can deactivate the panic response.
                        <br>Recognizing trauma doesn't mean excusing abuse; it means understanding that the aggression is likely not about <em>you</em>, which helps you remain detached and professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Trauma often manifests as aggression due to a loss of control.</li><li>Restore small choices ("Do you want water?") to give the person a sense of agency.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Post-Incident Decompression and Reporting',
                    'content': """
                        <p>The conflict does not end when the person leaves. The <strong>"Adrenaline Dump"</strong> that follows a high-stress interaction can leave you shaking, nauseous, or exhausted. Ignoring this leads to long-term burnout.
                        <br><strong>The 2026 Recovery Protocol:</strong>
                        <br>1. <strong>The 10-Minute Reset:</strong> You are biologically incapable of high-level work immediately after a crisis. Take 10 minutes. Walk. Drink water. Do "Box Breathing" (Inhale 4, Hold 4, Exhale 4, Hold 4).
                        <br>2. <strong>The Hot Wash (Debrief):</strong> Discuss the event with a supervisor or peer within 24 hours. Focus on: What went well? What triggered the escalation? Could we have tapped out sooner?
                        <br>3. <strong>Documentation:</strong> Write the incident report immediately while facts are fresh. Use objective language. Quote specific phrases used ("He said 'I will kill you'", not "He was threatening").
                        <br>4. <strong>Employee Assistance Program (EAP):</strong> If the incident involved physical threats, engage professional counseling early to prevent PTSD symptoms.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Mandatory 10-minute biological reset after any Code Gray event.</li><li>Document exact quotes in incident reports; avoid subjective descriptions.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Certification Mastery: The "Peacekeeper" Mindset',
                    'content': """
                        <p>We conclude with the philosophy of the <strong>Peacekeeper</strong>. Conflict resolution is not about "winning" the argument; it is about "winning the peace." It requires the confidence to be insulted without taking offense, the strength to set boundaries without aggression, and the wisdom to know when to walk away.
                        <br>In 2026, the ability to de-escalate is a superpower. Whether in a hospital, a warehouse, or a boardroom, the person who can remain calm in the midst of chaos is the natural leader. By mastering the HEAT model, the Reactionary Gap, and the Physiology of Aggression, you protect not only yourself but the culture of your entire organization. Stay calm. Stay safe. Stay professional. You are now a certified Conflict Resolution Specialist.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The goal is to "Win the Peace," not the argument.</li><li>Your calmness is your greatest weapon; it stabilizes the entire room.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Conflict Resolution Upgraded to PLATINUM Standard.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
