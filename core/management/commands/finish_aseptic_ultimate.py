from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Aseptic Technique with Modules 5-12 at World-Class Density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Aseptic Technique')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Skin Antisepsis: The "Back-and-Forth" Science',
                    'content': """
                        <p>In 2026, the standard for prepping a patient's skin has moved beyond the "circular motion" of the past. For <strong>Chlorhexidine Gluconate (CHG)</strong> to be effective, it requires mechanical friction to reach the lower layers of the epidermis where bacteria reside. The 2026 standard is a <strong>Vigorous Back-and-Forth Scrub</strong> for at least 30 seconds. This friction breaks up the skin oils and allows the antiseptic to penetrate. If you are using Povidone-Iodine (Betadine), the circular motion is still used, but it must be allowed to dry completely to achieve its "Kill-Power."</p>
                        
                        <p>A critical 2026 compliance factor is <strong>Dry Time</strong>. You must never fan, blow on, or blot the skin after applying an antiseptic. The "Chemical Action" occurs while the solution is drying. If you puncture the skin while it is still wet, you are "Inoculating" the patient with both the chemical and any surviving surface bacteria. For high-risk procedures like central line insertions, the "Prep Area" must be large enough to allow for accidental movement; if the clinician touches an un-prepped area and then touches the "Key Site," the entire procedure is contaminated and must be restarted.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use a vigorous back-and-forth scrub for CHG to ensure deep penetration.</li><li>Never fan or blow on an antiseptic; it must air-dry to be effective.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Sterile Gloving: The Open Technique',
                    'content': """
                        <p>While "Closed Gloving" is for the O.R., the <strong>Open Gloving Technique</strong> is the 2026 standard for bedside aseptic procedures, such as urinary catheterization or sterile dressing changes. The primary risk during open gloving is the bare hand touching the sterile exterior of the glove. You must only touch the "Inside Cuff" of the first glove with your bare hand. Once the first glove is on, you use that sterile hand to slide under the "Outside Cuff" of the second glove. This "Sterile-to-Sterile" contact is the only way to maintain the bio-shield.</p>
                        
                        <p>Once both gloves are on, your hands must remain in the <strong>"Safe Zone"</strong>—between your waist and your shoulders, and within your field of vision. If your hands drop below your waist, they are considered contaminated by the "Air-Shedding" of your own body. In 2026, we also emphasize the <strong>"Glove-Check"</strong>: if you feel a "wetness" or a "stickiness" during the procedure, you may have a micro-puncture. You must stop, de-glove, perform hand hygiene, and re-glove immediately. A compromised glove is an open door for biofilms to establish on the patient's internal tissues.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Touch only the inside cuff of the first glove with your bare hand.</li><li>Keep gloved hands in the "Safe Zone" (between waist and shoulders) at all times.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Wound Care and Aseptic Integrity',
                    'content': """
                        <p>Aseptic technique in wound care distinguishes between <strong>Acute Wounds</strong> (surgical incisions) and <strong>Chronic Wounds</strong> (pressure ulcers). For acute wounds, the goal is "Surgical Asepsis"—maintaining a totally sterile environment to prevent infection. For chronic wounds, which are already "Colonized" with bacteria, the goal is <strong>Clean Technique</strong> (using non-sterile gloves but sterile instruments/dressings) to prevent "Cross-Contamination" from one wound to another or from the environment into the wound bed.</p>
                        <p>In 2026, the <strong>"Wound-to-Dressing"</strong> direction is critical. When cleaning a wound, always move from the "Cleanest" area (the center of the wound or the incision line) to the "Dirtiest" area (the surrounding skin). Never use the same swab twice. If you are packing a deep wound, you must use <strong>Surgical ANTT</strong>—using sterile forceps to handle the packing material so that your gloves (which may have touched the patient's outer skin) never touch the "Key Part" (the sterile gauze) entering the deep tissue. This prevents the introduction of deep-seated biofilms that lead to sepsis.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Clean from the center of the wound outward to avoid dragging bacteria into the site.</li><li>Use sterile instruments for deep wound packing to prevent deep tissue infection.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: IV and Central Line Access: "Scrub the Hub"',
                    'content': """
                        <p>Intravenous (IV) access is the most common invasive procedure in healthcare, and it is the primary source of <strong>CLABSI (Central Line-Associated Bloodstream Infections)</strong>. In 2026, the mandate is <strong>"Scrub the Hub."</strong> Before accessing any IV port or "Hub," you must scrub the connection surface with a 70% Alcohol or CHG wipe for a full <strong>15 seconds</strong>. This mechanical scrubbing is required to break down the biofilm that forms on the surface of the plastic. Simply "swiping" the hub is insufficient and is a major 2026 compliance violation.</p>
                        
                        <p>After scrubbing, the hub must be allowed to <strong>Air-Dry for 15 seconds</strong>. If you connect the IV tubing while the hub is still wet, the alcohol can enter the patient's bloodstream and cause "hemolysis" (destruction of red blood cells), and more importantly, the antiseptic has not had time to kill the surface pathogens. For Central Lines, the 2026 standard also includes the use of <strong>CHG-Impregnated Caps</strong> (Green Caps), which provide continuous disinfection when the line is not in use. However, even with these caps, you must still perform a manual "Scrub the Hub" when the cap is removed before connecting a new line.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Scrub the IV hub for 15 seconds and allow it to air-dry for another 15 seconds.</li><li>The mechanical scrub is necessary to break the biofilm on the plastic connector.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Urinary Catheterization Asepsis (CAUTI Prevention)',
                    'content': """
                        <p>Catheter-Associated Urinary Tract Infections (CAUTIs) are largely preventable through rigid aseptic technique. In 2026, the <strong>Aseptic Insertion</strong> of a urinary catheter is a two-person procedure: one to maintain the sterile field and one to assist with patient positioning. The "Key Parts" are the catheter tip and the sterile lubricant. Once the "Non-Dominant Hand" touches the patient's labia or penis to expose the meatus, that hand is <strong>Contaminated</strong> and must never touch the sterile catheter or the sterile field again.</p>
                        <p>The 2026 "Maintenance Asepsis" is equally important. The drainage bag must always be kept below the level of the bladder to prevent the <strong>"Backflow" of Urine</strong>, which carries bacteria from the bag back into the bladder. The "Drainage Spout" must never touch the floor or any non-sterile container during emptying. In 2026, we utilize <strong>Closed-System Catheters</strong>, where the seal between the catheter and the bag is never broken. If the system is disconnected, the risk of infection increases by 50% within 24 hours. Daily "Meatal Care" with soap and water (not antiseptics) is the standard for long-term catheter management.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "hand that holds the patient" is contaminated; it must never return to the sterile field.</li><li>Keep drainage bags below the bladder to prevent bacterial backflow.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Aseptic Disposal and Waste Streams',
                    'content': """
                        <p>Aseptic technique concludes with the safe removal and disposal of contaminated materials. In 2026, we follow the <strong>"Containment at Source"</strong> rule. Contaminated dressings and PPE must be placed directly into a <strong>Biohazard (Red Bag)</strong> container at the bedside, rather than being carried through the hallway. This prevents "Aerosolization" of pathogens from dried blood or fluids. If an item is "Dripping or Saturated," it is Regulated Medical Waste; if it is only slightly soiled, it may be disposed of in regular trash according to 2026 local facility policies.</p>
                        <p>The management of "Sharps" is a critical safety component. Never recap a needle after a procedure unless using a mechanical device or the "one-handed scoop." The <strong>Sharps Container</strong> must be located at the point of use. In 2026, we emphasize <strong>"Passive Safety"</strong>—using needles that automatically retract or shield themselves after use. Once the procedure is complete, the clinician must perform a "Final Sweep" of the area to ensure no Key Parts or sharps were left behind. Final hand hygiene is the 12th and final step of every aseptic procedure, signaling the closing of the "Bio-Shield."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Dispose of biohazard waste at the bedside to prevent environmental contamination.</li><li>Perform final hand hygiene immediately after removing contaminated PPE.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: The "Stop the Line" Culture',
                    'content': """
                        <p>In 2026, <strong>Surgical Conscience</strong> is applied to every bedside procedure. This is the "Stop the Line" culture: the ethical requirement to stop a procedure immediately if a break in asepsis occurs. If your sterile glove touches the patient's bedrail, or if a sterile gauze drops onto the 1-inch border of the wrapper, you must stop, discard the items, and restart. There is no "five-second rule" in asepsis. The 2026 professional understands that a 5-minute delay to restart a sterile field is better than a 5-week hospital stay for a patient with a preventable infection.</p>
                        <p>This culture also involves <strong>Mutual Accountability</strong>. If a junior nurse observes a senior physician "scrubbing the hub" for only 2 seconds instead of 15, they have the professional authority and duty to speak up. Organizations in 2026 utilize <strong>"Safety Huddles"</strong> to discuss near-misses in aseptic technique. By de-stigmatizing errors and focusing on process improvement, we create an environment where the "Bio-Shield" is maintained by the entire team, not just the individual clinician. Aseptic technique is an act of advocacy for the patient's life.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>There is no "five-second rule"; if a sterile item is compromised, discard it immediately.</li><li>"Stop the Line" means safety and sterility always override the clinical schedule.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: 2026 Certification Mastery',
                    'content': """
                        <p>The final module summarizes the <strong>"Bio-Shield" Mindset</strong>. Aseptic technique is the application of microbiology to the clinical setting. By mastering the 15-second hub scrub, the 2-inch safe zone for hands, and the vigorous back-and-forth skin prep, you have reduced the patient's risk of infection to the lowest possible level. In 2026, HAIs are viewed as "Never Events"—complications that should not happen in a modern, professional healthcare system. Your technical precision is the primary tool for achieving this goal.</p>
                        <p>As you conclude this certification, remember that <strong>Asepsis is a Perceptual Skill</strong>. You must be able to "see" the invisible bacteria and "visualize" the boundaries of your sterile field. Every time you open a package, every time you don a glove, and every time you access an IV, you are making a clinical decision that affects a human life. By maintaining these 2026 world-class standards, you represent the highest level of clinical integrity. Stay vigilant, stay precise, and stay committed to the Bio-Shield. You are now a certified master of Aseptic Technique.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Asepsis is a perceptual skill; you must always "visualize" the sterile boundaries.</li><li>Mastering these 2026 standards directly prevents "Never Event" infections.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Aseptic Technique 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
