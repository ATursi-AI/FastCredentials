from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades CPR/AED to BBP-Level Depth (2000+ chars per module)'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Standard CPR / AED')
            Lesson.objects.filter(course=course).delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'The 2026 Chain of Survival: A Systems Approach',
                    'content': """
                        <p>The Chain of Survival is the internationally recognized clinical framework for maximizing the probability of survival following a Sudden Cardiac Arrest (SCA). In 2026, the standard has transitioned into a <strong>6-link system</strong> that emphasizes a continuum of care starting from the second a victim collapses. The first three links—Early Recognition, High-Quality CPR, and Rapid Defibrillation—are the exclusive domain of the lay rescuer. Research indicates that for every minute that passes without these interventions, the probability of successful resuscitation drops by approximately 10%. By the time professional EMS arrives (typically 8-12 minutes in urban settings), the physiological window for survival has often closed unless a bystander has initiated the chain.</p>
                        <p>The 2026 guidelines introduce the <strong>Recovery Link</strong> as the sixth and final component of the chain. This link acknowledges that survival is not merely the return of spontaneous circulation (ROSC), but a long-term process involving neurological rehabilitation and psychological support. Sudden Cardiac Arrest is a massive physical and emotional trauma; the Recovery Link mandates that discharge planning include assessments for anxiety, depression, and post-cardiac arrest syndrome. It also emphasizes the importance of "Rescuer Support," providing mental health resources for the laypeople who performed the life-saving measures, as the stress of the event can have lasting impacts.</p>
                        <p>As a certified rescuer, you are the most critical variable in this system. Clinical data proves that "Hands-Only" CPR initiated by a bystander can double or triple a victim's chance of survival. This module establishes the mindset that you are not merely a witness, but a vital medical link. Your goal is to maintain perfusion—the flow of oxygenated blood—to the brain and heart until the heart can be "restarted" by an AED or advanced medical intervention. This course will provide the technical depth required to perform these links with the precision of a professional responder.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The 2026 Chain has 6 links, culminating in long-term Recovery and Rescuer Support.</li><li>The first three links (Recognition, CPR, AED) are the most time-sensitive for survival.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'The Biomechanics of High-Quality Compressions',
                    'content': """
                        <p>Chest compressions are the mechanical substitute for a beating heart. To be effective, they must create enough intrathoracic pressure to force blood out of the heart and into the arterial system. In 2026, "High-Quality CPR" is defined by four strict clinical metrics: Depth, Rate, Recoil, and Minimal Interruptions. For an adult, you must compress the chest to a <strong>depth of 2 to 2.4 inches (5 to 6 cm)</strong>. Pushing shallower than 2 inches is a "non-perfusing" event, meaning the blood never reaches the brain. Conversely, pushing deeper than 2.4 inches significantly increases the risk of catastrophic internal injuries, such as liver lacerations or rib fractures that can puncture the lungs.</p>
                        
                        <p>The compression rate is the "metronome" of survival. The current standard is <strong>100 to 120 compressions per minute</strong>. This specific window is based on the physics of the human heart; it allows the heart enough time to refilled with blood (diastolic filling) while maintaining high enough mean arterial pressure to keep brain cells alive. If you exceed 120 BPM, the heart does not have time to refill, and you are effectively "pumping an empty chamber." If you fall below 100 BPM, the pressure in the system drops too low to fight gravity and reach the cerebral cortex.</p>
                        <p>The most commonly overlooked component of CPR is <strong>Full Chest Recoil</strong>. Between every compression, you must allow the chest to return completely to its natural position without "leaning" on the victim. Leaning—maintaining even slight pressure on the chest during the upstroke—prevents the heart from expanding and refilling with blood. Finally, interruptions must be minimized; every time you stop compressions (to check a pulse or move the victim), the blood pressure in the system immediately crashes to zero. It takes nearly 10-15 continuous compressions to build that pressure back up to a perfusing level. Therefore, you should never stop compressions for more than 10 seconds.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Maintain a depth of 2.0 to 2.4 inches and a rate of 100-120 BPM.</li><li>Ensure full chest recoil to allow the heart to refill with blood between strokes.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Advanced Airway Management and Ventilation',
                    'content': """
                        <p>While compressions move the blood, rescue breaths ensure that the blood being moved is carrying oxygen. In the first few minutes of a sudden collapse, the victim's blood contains a residual supply of oxygen. However, as the arrest progresses, or in cases of drowning and drug overdose, that oxygen is depleted, leading to cellular death. The 2026 standard for a single rescuer remains a <strong>ratio of 30 compressions to 2 rescue breaths</strong>. To deliver these breaths effectively, you must first open the airway using the <strong>Head-Tilt/Chin-Lift maneuver</strong>. This action lifts the tongue away from the posterior pharynx, which is the most common cause of airway obstruction in an unresponsive victim.</p>
                        <p>When delivering breaths, you are acting as the victim's lungs. Each breath should be delivered over <strong>one second</strong> with just enough volume to see the chest visibly rise. You must avoid "hyperventilation"—blowing too hard or too fast. Excessive air can enter the esophagus instead of the trachea, causing gastric inflation. This leads to vomiting and the potential for aspiration, where stomach contents enter the lungs, causing severe infection or blocking the airway entirely. Furthermore, excessive pressure in the chest can actually decrease the amount of blood that can return to the heart, making your compressions less effective.</p>
                        <p>In 2026, the use of a <strong>barrier device or pocket mask</strong> is mandatory for rescue breaths to protect the rescuer from infectious diseases (referencing Bloodborne Pathogen standards). If you do not have a barrier device, or if you are not trained in rescue breathing, you should provide <strong>Hands-Only CPR</strong> (continuous compressions). Hands-Only CPR is the preferred method for untrained bystanders and is highly effective for the first few minutes of a cardiac event. However, for infants, children, and victims of respiratory-based arrest (drowning/choking), rescue breaths are considered mandatory as their primary issue is oxygen depletion rather than a cardiac rhythm failure.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The 30:2 ratio is the standard for adult, child, and infant CPR for single rescuers.</li><li>Provide breaths over 1 second, ensuring chest rise while avoiding gastric inflation.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Defibrillation: The Physics of the AED',
                    'content': """
                        <p>An Automated External Defibrillator (AED) is a high-precision medical device that analyzes the heart's electrical activity and determines if a shock is necessary. It is a common misconception that an AED "restarts" a dead heart. In reality, the AED is used to <strong>stop</strong> a heart that is in a lethal, chaotic rhythm, such as Ventricular Fibrillation (V-Fib). In V-Fib, the heart's electrical signals are firing randomly, causing the muscle to quiver rather than pump. The AED delivers a controlled burst of electricity that momentarily stops all electrical activity, allowing the heart's natural pacemaker (the SA Node) to re-establish a normal, organized rhythm.</p>
                        
                        <p>The 2026 generation of AEDs is designed for rapid deployment. The most critical step is to <strong>Turn the AED ON immediately</strong> upon its arrival. Once powered on, the device will provide verbal and visual prompts. You must apply the electrode pads to the victim's bare chest. The standard placement is "Anterolateral": one pad on the upper right chest (below the collarbone) and the other on the lower left ribs (below the armpit). For victims with hairy chests, you may need to use the "press and pull" method with a set of pads or a razor to ensure a clear electrical connection. If the victim has a visible medication patch, remove it with a gloved hand and wipe the area clean before applying the pad.</p>
                        <p>Safety during defibrillation is a non-negotiable legal and safety requirement. When the AED begins its analysis phase, you must loudly shout <strong>"Clear!"</strong> and ensure no one is touching the victim. Touching the patient during analysis can cause the AED to misinterpret your own heart rate or movement as the victim's rhythm. If a shock is advised, you must perform a final visual sweep from head to toe to ensure no one is in contact with the patient or any conductive surfaces (like a metal floor) before pressing the shock button. Immediately after the shock is delivered, you must resume chest compressions—do not wait for the AED to tell you to start. The heart is very weak after a shock and needs the mechanical support of CPR to maintain perfusion.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The AED stops chaotic rhythms to allow a normal rhythm to return.</li><li>Rescuers must be "Clear" of the victim during analysis and shock delivery.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: CPR/AED updated with World-Class Depth.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
