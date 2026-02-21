from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades First Aid to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Standard First Aid')
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 First Aid Legal Landscape',
                    'content': """
                        <p>The legal framework for First Aid has undergone significant shifts in 2026, primarily driven by the expansion of <strong>Good Samaritan Laws</strong> to cover advanced layperson interventions. These laws are designed to encourage bystanders to act without the fear of civil liability, provided they act in good faith, are not willfully negligent, and do not accept compensation. Modern updates specifically protect the use of tourniquets, epinephrine auto-injectors, and opioid-reversal agents (Naloxone). Understanding your local "Duty to Act" is also critical; while most laypeople have no legal duty to assist, those in certain professions (or those who have initiated care) must continue until a higher medical authority takes over.</p>
                        <p>The concept of <strong>Consent</strong> remains a cornerstone of first aid ethics. For a conscious victim, you must obtain verbal consent before any physical contact occurs. If a victim is a minor, you must seek consent from a parent or guardian if present; if no guardian is available, consent is "implied." Implied consent also applies to any adult who is unconscious, confused, or otherwise mentally incapacitated. Respecting a victim's refusal of care is legally mandatory for a conscious adult, even if their choice seems medically unwise. In such cases, your role shifts to monitoring and waiting for professional EMS to arrive.</p>
                        <p>Finally, <strong>Confidentiality and Documentation</strong> are increasingly scrutinized. Under HIPAA-inspired standards, you must protect the victim's privacy, sharing their medical details only with the arriving EMS personnel. If you are providing aid in a workplace setting, your employer may require a formal incident report. This report should be factual and objective, focusing on the "Mechanism of Injury" (what happened) and the "Primary Assessment" (what you found). Accurate documentation not only ensures continuity of care but also serves as your best legal protection should the intervention be questioned later.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Good Samaritan laws protect rescuers from liability for "good faith" interventions.</li><li>Consent is implied for unconscious victims or minors without guardians.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Major Bleeding and Hemorrhage Control',
                    'content': """
                        <p>In 2026, the #1 priority in trauma management has shifted from "Airway" to <strong>Life-Threatening Bleeding</strong>. A victim with a severed femoral artery can bleed to death in less than three minutes—faster than the time it takes for a brain to die from lack of oxygen. Identifying "Life-Threatening" bleeding is the first skill: look for blood that is "spurting," "pooling," or soaking through clothing and bandages. If the bleeding is coming from a limb (arm or leg), you must move immediately to aggressive intervention.</p>
                        
                        <p>For extremity bleeding that cannot be controlled by direct pressure, the 2026 gold standard is the <strong>Combat Application Tourniquet (C-A-T)</strong> or a similar windlass-style device. Apply the tourniquet 2-3 inches <em>above</em> the wound, between the injury and the heart. If the exact wound site is unclear (e.g., inside a pant leg), apply the tourniquet "High and Tight" at the top of the limb. Tighten the windlass until the bleeding stops completely and the distal pulse is no longer felt. Note the time of application on the victim\'s forehead or the device itself. A properly applied tourniquet is extremely painful; you must warn the victim and never loosen it once it is set.</p>
                        <p>For wounds in "junctional" areas—such as the groin, armpit, or neck—where a tourniquet cannot be placed, the technique is <strong>Wound Packing</strong>. You must use hemostatic gauze (gauze treated with blood-clotting agents) or plain sterile gauze and "stuff" it deep into the wound cavity until it is full. Once packed, apply heavy, two-handed direct pressure for at least 3 minutes (or longer if using plain gauze). This mechanical pressure, combined with the packing material, creates an artificial clot that can stabilize a victim until they reach a surgical suite.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Life-threatening bleeding is the #1 priority in trauma.</li><li>Apply tourniquets 2-3 inches above the wound; never loosen them.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Shock: The Silent Killer',
                    'content': """
                        <p>Shock is a life-threatening medical condition that occurs when the body's peripheral tissues and organs do not receive enough oxygenated blood (hypoperfusion). In first aid, we primarily deal with <strong>Hypovolemic Shock</strong>, caused by severe blood or fluid loss. When a victim enters shock, their body begins to "shunt" blood away from the skin and extremities toward the vital organs (heart, brain, lungs). This leads to the classic clinical signs: pale, cool, and clammy skin, a rapid but weak pulse, and increased respiration.</p>
                        <p>The 2026 protocol for shock management is "Wait and Stabilize." The most effective intervention a layperson can provide is <strong>Maintaining Body Temperature</strong>. Even in warm weather, a victim in shock will lose body heat rapidly as their metabolic processes fail. Cover the victim with a space blanket, coat, or regular blanket to prevent hypothermia, which is part of the "lethal triad" of trauma. Keep the victim lying flat on their back to maximize blood flow to the brain; the old practice of elevating the feet is no longer universally recommended as it can interfere with respiratory mechanics.</p>
                        <p>Do not give a victim in shock anything to <strong>eat or drink</strong>. While they may complain of extreme thirst, giving fluids can lead to vomiting or complicate the administration of anesthesia if they require emergency surgery later. Your goal is to keep the victim calm and still. Anxiety increases the heart rate and oxygen demand, which accelerates the progression of shock. Stay with the victim, provide continuous reassurance, and monitor their level of consciousness until advanced medical teams can initiate intravenous fluid resuscitation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Shock is hypoperfusion; signs include cool, clammy skin and rapid pulse.</li><li>Keep the victim flat and warm; never give food or water.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Burn Pathophysiology and Care',
                    'content': """
                        <p>Burns are classified by the depth of tissue damage: <strong>Superficial (1st Degree)</strong> involving only the epidermis; <strong>Partial-Thickness (2nd Degree)</strong> involving the dermis and characterized by blisters; and <strong>Full-Thickness (3rd Degree)</strong> where the skin is charred or white and nerves may be destroyed. In 2026, the primary focus is on "Stopping the Burning Process." For thermal burns, this means immediate cooling with <strong>cool (not cold) running water</strong> for at least 10 to 20 minutes. Cooling significantly reduces the "after-burn" effect where heat continues to damage deeper tissues even after the source is removed.</p>
                        
                        <p>There are several dangerous myths in burn care that 2026 standards explicitly reject. <strong>Do not use ice</strong> or ice-cold water, as this can cause vasoconstriction and further tissue damage (frostbite). Never apply butter, ointments, or home remedies to a fresh burn, as these trap heat and increase the risk of infection. For partial-thickness burns, do not pop blisters; the blister act as a sterile "natural bandage" for the sensitive tissue underneath. If clothing is stuck to the burn, do not pull it off; instead, cut the surrounding fabric and leave the stuck portion for a physician to remove.</p>
                        <p>Chemical and electrical burns require specialized approaches. For <strong>Chemical Burns</strong>, you must flush the area with water for at least 20 minutes, ensuring the chemical is washed <em>away</em> from the body rather than onto unaffected skin. If the chemical is a dry powder, brush it off with a gloved hand or cloth before flushing. <strong>Electrical Burns</strong> are deceptively dangerous because the most significant damage is often internal (cardiac arrhythmias or internal organ cooking). Every victim of a significant electrical shock—even if they look fine—requires an immediate EKG at a hospital.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cool thermal burns with running water for 10-20 minutes; avoid ice.</li><li>Never pop blisters or apply ointments to severe burns.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: First Aid Ultimate Upgrade (Part 1) pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
