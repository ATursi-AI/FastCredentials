from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Active Shooter with Modules 6-10 at Tactical Depth'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Active Shooter Preparedness')
            
            lessons = [
                {
                    'order': 6,
                    'title': 'Module 6: Interacting with Law Enforcement',
                    'content': """
                        <p>The arrival of law enforcement is the most dangerous and chaotic phase of an active threat. In 2026, police doctrine is "Immediate Entry," meaning the first officers on the scene will not wait for a SWAT team or a supervisor; they will move directly toward the sound of gunfire. Their sole objective is to neutralize the shooter. This means they will move past injured people, they will not stop to comfort victims, and they may be shouting loud, aggressive commands. You must understand that in the initial minutes, the police do not know who the shooter is—they must treat everyone as a potential threat until proven otherwise.</p>
                        <p>Your behavior during this interaction is critical for your safety. <strong>Keep your hands visible and empty at all times.</strong> As officers approach, raise your hands above your head with fingers spread wide. Do not carry anything in your hands—not even a cell phone, as the silhouette of a black object in a high-stress environment can be mistaken for a weapon. Do not make sudden movements toward the officers or attempt to grab them for help. Do not point at the shooter or scream directions unless specifically asked. Follow every command immediately and without question. If you are told to get on the floor or be handcuffed, comply instantly.</p>
                        <p>Once the immediate threat is neutralized, rescue teams and paramedics will enter. You will likely be moved to a secure "assembly area." Do not leave this area until law enforcement has officially identified you and taken your statement. Arriving officers need specific information: the last known location of the shooter, their physical description, the type of weapons used (long gun vs. handgun), and the location of any victims who need immediate medical attention. Be concise and factual. Remember that the scene is still a crime scene, and your cooperation is vital for the ensuing investigation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Keep hands visible, empty, and fingers spread; do not carry anything.</li><li>Comply with all police commands immediately, even if they seem aggressive.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Tactical Medicine: Ballistic Trauma',
                    'content': """
                        <p>In an active shooter event, the window between injury and death from blood loss is measured in minutes. Because the scene may not be "safe" for paramedics to enter for a significant amount of time, civilians must be prepared to provide <strong>Tactical Medicine (TECC)</strong>. The primary cause of death in these events is uncontrolled extremity hemorrhage. If you or someone near you is shot in an arm or leg, you must apply a <strong>Tourniquet</strong> immediately. Apply it "High and Tight" on the limb, over the clothing, and tighten it until the bleeding stops. In a tactical environment, you do not have the luxury of precise placement; the goal is total occlusion of the artery.</p>
                        
                        <p>Gunshot wounds to the torso (chest, back, or abdomen) are a different clinical challenge because tourniquets cannot be used. For a chest wound, there is a high risk of a "Tension Pneumothorax," where air enters the chest cavity and collapses the lung. The 2026 standard is to use a <strong>Vented Chest Seal</strong>. This is a specialized adhesive dressing that allows air to escape the chest but prevents it from entering. If a chest seal is not available, a piece of plastic secured on three sides can act as an improvised valve. For wounds in the groin or armpit (junctional areas), you must perform aggressive <strong>Wound Packing</strong>, stuffing gauze deep into the cavity and applying heavy direct pressure.</p>
                        <p>The "Stop the Bleed" mindset is essential for survival. You should know where the nearest "Bleeding Control Kit" is located in your building. These kits typically contain tourniquets, hemostatic gauze (which contains blood-clotting agents), and chest seals. If no kit is available, use improvised materials: a belt as a tourniquet (though less effective), or clean shirts for wound packing. Do not stop compressions or pressure until a medical professional explicitly takes over. Your goal is to "Buy Time" for the victim to reach a surgical suite.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Apply tourniquets "High and Tight" for limb wounds immediately.</li><li>Use vented chest seals for torso wounds to prevent lung collapse.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: The Role of HR and Management',
                    'content': """
                        <p>Organizational leadership and HR are the architects of prevention. In 2026, the legal standard for "Workplace Safety" includes a robust Active Threat Emergency Action Plan (EAP). HR is responsible for establishing a <strong>zero-tolerance policy</strong> for workplace violence and bullying, ensuring that every report of a threat is investigated by a multi-disciplinary Threat Assessment Team. Management must ensure that employees are not just "aware" of the plan, but are actively trained through tabletop exercises and walkthrough drills. A plan that sits in a binder on a shelf is useless during the first 60 seconds of a crisis.</p>
                        <p>Termination protocols are a high-risk area for workplace violence. 2026 HR standards emphasize <strong>"Dignified Departure"</strong> strategies. When an employee is being fired, especially one with a history of conflict, the meeting should be handled with professional empathy to minimize the "humiliation trigger." Security should be present but discreet. Access to company systems (email, Slack, servers) and physical building access (keycards) must be revoked the moment the meeting begins. Following the termination, management should monitor for "leakage" or retaliatory social media posts from the former employee.</p>
                        <p>Physical security is the final layer of management responsibility. This includes ensuring that <strong>Access Control Systems</strong> are functional and that "tailgating" (allowing someone to enter behind you without swiping) is strictly prohibited. Managers should conduct regular "security sweeps" to ensure that fire exits are not propped open and that safe rooms are stocked with basic emergency supplies. By fostering a culture of "Collective Security," management empowers every employee to take ownership of the environment’s safety, significantly reducing the organization’s profile as a soft target.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HR must establish a Threat Assessment Team to evaluate "red flag" behaviors.</li><li>Revoke all digital and physical access immediately during high-risk terminations.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Psychological Recovery and PTSD',
                    'content': """
                        <p>The trauma of an active threat event does not end when the police leave. Survivors often experience a range of acute psychological responses, including flashbacks, hyper-vigilance, and "Survivor's Guilt." In 2026, we recognize <strong>Post-Traumatic Stress Disorder (PTSD)</strong> as a major long-term risk for those involved in mass casualty events. Organizations must be prepared to provide immediate and long-term mental health support through Employee Assistance Programs (EAPs) and specialized trauma counselors. Recovery is a marathon, and the "return to work" process must be handled with extreme sensitivity.</p>
                        <p>Psychological First Aid (PFA) should be implemented in the "Assembly Area" immediately following the event. PFA involves <strong>stabilizing</strong> survivors by ensuring their basic needs (safety, water, contact with family) are met and providing a calm, non-intrusive presence. You should avoid "Critical Incident Stress Debriefing" (CISD) in the first 24 hours—forcing survivors to retell their story too early can actually increase the risk of developing PTSD. Instead, allow survivors to share as much or as little as they wish, and focus on providing factual information to reduce the anxiety caused by uncertainty.</p>
                        <p>Community resilience is built through transparency and shared grieving. The physical space where the event occurred may need to be remodeled or repurposed, as visual triggers can cause severe setbacks for survivors. Anniversaries and media coverage of other shootings can also act as triggers. Leaders must remain visible and admit to their own struggles, which gives employees "permission" to seek help. By acknowledging the trauma and providing a structured, empathetic path toward a "new normal," the organization can begin the slow process of healing the psychological wounds of the attack.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>PTSD is a high risk; provide long-term mental health support and EAPs.</li><li>Avoid forcing survivors to retell their stories immediately after the event.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: The 2026 Personal Preparedness Kit (IFAK)',
                    'content': """
                        <p>Personal preparedness is the final link in the survival chain. In 2026, many professionals carry an <strong>Individual First Aid Kit (IFAK)</strong> in their vehicle or laptop bag. Unlike a standard "band-aid" first aid kit, an IFAK is a tactical kit designed specifically for trauma. It should contain four essential items: 1. A windlass-style Tourniquet (C-A-T or SOFT-W), 2. Hemostatic Gauze (QuikClot), 3. Vented Chest Seals (HyFin), and 4. Trauma Shears to cut through thick clothing. Having these tools available can turn a bystander into a life-saver during the critical minutes before EMS arrival.</p>
                        
                        <p>Beyond physical tools, your "Kit" must include <strong>Mental Preparedness</strong>. This involves the practice of "Visualization Training." When you enter a new environment, play the "What If" game. "What if a shooter came through that door? Where is my nearest exit? Where is my nearest hard-cover?" By pre-programming these responses, you reduce your reaction time during a real crisis. This mental rehearsal creates "muscle memory" in the brain, allowing you to bypass the "Freeze" response and move directly into the "Run" or "Hide" phase of survival.</p>
                        <p>Finally, stay informed about local alert systems. Most modern cities and corporate campuses use <strong>Mass Notification Systems</strong> (MNS) that send text, email, and desktop alerts during an emergency. Ensure your contact information is updated and that you recognize the "Alert Tone." If your area has "Text to 911" capabilities, familiarize yourself with how to use them, as a text message may go through when a voice call fails due to tower congestion or the need for silence. Preparedness is a lifestyle of awareness; by carrying the right tools and maintaining the right mindset, you become a "Hard Target" and a guardian for those around you.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Carry an IFAK with a tourniquet, hemostatic gauze, and chest seals.</li><li>Practice "Visualization Training" to pre-program your survival responses.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Active Shooter Ultimate pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
