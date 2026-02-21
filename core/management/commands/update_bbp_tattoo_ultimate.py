from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades BBP for Body Art to 10 World-Class Tactical Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Bloodborne Pathogens (Body Art & Tattoo)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The OSHA Standard for Body Art Professionals',
                    'content': """
                        <p>The OSHA Bloodborne Pathogens Standard (29 CFR 1910.1030) applies to any profession with "Reasonable Anticipation" of contact with blood or OPIM. In the body art industry, this exposure is not accidental; it is a fundamental part of the procedure. In 2026, the standard emphasizes the <strong>Exposure Control Plan (ECP)</strong> as a specific roadmap for the studio. It must detail exactly how you handle contaminated needles, how you disinfect your station between clients, and what your specific protocol is for an accidental "Artist Stick."</p>
                        <p>A world-class studio in 2026 maintains a <strong>Sharps Injury Log</strong> even if they have fewer than 11 employees, as a best practice for insurance and liability protection. This log tracks every instance where a needle or piercing tool breaks the skin of the artist. By law, your employer must also provide the <strong>Hepatitis B Vaccination</strong> series to you for free within 10 days of starting work. Because HBV can survive in dried blood on a tattoo machine or a countertop for 7 days, this vaccine is the most important health investment for a body art professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>BBP compliance is mandatory for all tattoo and piercing professionals.</li><li>Hepatitis B is the primary risk due to its 7-day survival on dry surfaces.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Anatomy of the Skin and Portals of Entry',
                    'content': """
                        <p>Tattooing and piercing involve the intentional breaching of the <strong>Epidermis and Dermis</strong>. In 2026, we view the skin as the body's primary immune barrier. When you perform a procedure, you are creating thousands of "Micro-Portals of Entry." If your equipment, ink, or hands are contaminated, you are directly inoculating the client with pathogens. Conversely, if the client is a carrier of HBV, HCV, or HIV, the "backflow" of blood and interstitial fluid into your equipment creates a portal of entry for you.</p>
                        
                        <p>We also focus on <strong>Non-Intact Skin</strong> on the artist. If you have a small cut, a hangnail, or even dry, cracked skin (dermatitis) on your hands, you have an open portal for infection. Viruses like HBV are small enough to pass through microscopic gaps in the skin that you cannot see. This is why "Hand Hygiene" and "Barrier Protection" (gloves) are not just about the client's safety—they are about your survival in a high-exposure environment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Tattooing creates portals of entry for both the artist and the client.</li><li>Artist hand health is a critical safety factor; cracks in skin are entry points.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Aseptic Technique and Station Setup',
                    'content': """
                        <p>In 2026, the standard for station setup is <strong>Total Aseptic Isolation</strong>. This means creating a "Clean Field" where only sterile items touch the client. Before the client sits down, the station must be disinfected with an EPA-registered tuberculocidal agent. All "High-Touch" surfaces—the power supply, the clip cord, the lamp, and the client chair—must be covered with single-use <strong>Plastic Barriers</strong>. If you touch a non-barrier surface (like your phone or a cabinet handle) during the procedure, your gloves are now contaminated and must be changed.</p>
                        <p>The 2026 "No-Cross" Rule: Once a procedure begins, you never reach into a drawer or a box of gloves with your contaminated procedure-gloves. All supplies (ink caps, ointment, wipes) must be "Pre-Staged" on the clean field before you start. If you run out of a supply, you must either have an assistant get it for you or perform a full "Doffing and Redonning" sequence (remove gloves, wash hands, get supply, re-glove). This prevents the "Cross-Contamination" of your entire studio's inventory.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use plastic barriers on all high-touch surfaces; change them between every client.</li><li>Pre-stage all supplies to avoid reaching into drawers with contaminated gloves.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Engineering Controls: Cartridges and Sharps',
                    'content': """
                        <p>Engineering Controls are devices that <strong>isolate or remove the hazard</strong>. In the 2026 body art industry, the primary engineering control is the <strong>Single-Use Needle Cartridge System</strong> with an internal safety membrane. These membranes prevent blood and ink from flowing back into the machine's drive bar, protecting the machine from internal contamination. If you are using a legacy "tube and needle" setup, the tubes must be processed through a multi-stage sterilization cycle involving ultrasonic cleaning and autoclaving.</p>
                        <p><strong>Sharps Containers</strong> are the second critical engineering control. In a tattoo studio, the sharps container must be located within arm's reach of your workstation so you don't have to walk across the room with a contaminated needle. In 2026, the "3/4 Full Rule" is strictly enforced: once the needles reach the fill line, lock the container and replace it. Never attempt to "force" a needle into a full container; this is the leading cause of "Artist Sticks" in the industry.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cartridges with safety membranes prevent backflow into the tattoo machine.</li><li>Sharps containers must be within arm's reach and never overfilled.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Work Practice Controls: The "Dirty Arm" Protocol',
                    'content': """
                        <p>Work Practice Controls involve changing <strong>how</strong> you do the work to reduce risk. For 2026, we emphasize the <strong>"Single-Handed Wipe"</strong> and the "Dirty Arm" protocol. When wiping away excess ink and blood, always wipe *away* from your own body and your non-dominant hand. A common injury occurs when an artist wipes toward themselves and accidentally sticks their own finger with the needle still in the machine. By maintaining a "Neutral Zone" on the client's skin, you keep your hands clear of the needle's path.</p>
                        <p>Another 2026 standard is the <strong>Prohibition of Consumables</strong>. You must never eat, drink, smoke, or apply lip balm in the procedure area. This includes "vaping." These actions create a "Hand-to-Mouth" transmission route for pathogens. Even if you think your station is clean, the aerosolized blood droplets (micro-splatter) produced during tattooing can land on your water bottle or coffee cup. In a world-class studio, the "Break Area" and the "Procedure Area" are strictly separated by physical walls.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Always wipe ink away from your body and your free hand.</li><li>Vaping and drinking in the procedure area are major BBP violations.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Ink Safety and Pigment Contamination',
                    'content': """
                        <p>In 2026, <strong>Ink Contamination</strong> is recognized as a major source of infection outbreaks. Ink can be contaminated at the factory or, more commonly, at the studio through "Dipper Contamination." When you dip your needle into an ink cap, you are transferring the client's fluids into that cap. If you then use the same bottle of ink to refill that cap, or if you touch the tip of the ink bottle to the contaminated cap, you have contaminated the entire bottle for every future client.</p>
                        <p>The 2026 "Ink Discipline": Always pour ink into single-use caps and <strong>never let the bottle tip touch the cap</strong>. Once the procedure is over, all remaining ink in the caps must be disposed of as biohazard waste—never pour it back into the bottle. Furthermore, you must only use inks from reputable manufacturers that provide a "Lot Number" and "Sterility Certification." In 2026, we also monitor for "Biofilm" growth in large-format ink bottles; if a bottle has been open for more than 12 months, it should be discarded to prevent the growth of non-tuberculous mycobacteria.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never touch the ink bottle tip to an ink cap during a procedure.</li><li>Discard all remaining ink in caps as biohazard waste; never reuse.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Sterilization: The 2026 Autoclave Standard',
                    'content': """
                        <p>For studios that do not use 100% disposable supplies, the <strong>Autoclave</strong> is the most important piece of safety equipment. An autoclave uses saturated steam under pressure to achieve a "Sterility Assurance Level." In 2026, "looking at the color-change tape" is not enough. You must use <strong>Biological Indicators (Spore Tests)</strong> at least weekly. A spore test is the only way to prove that the autoclave is actually killing the most resistant forms of life, like <i>Geobacillus stearothermophilus</i>.</p>
                        <p>Log-keeping is a legal requirement. For every autoclave "load," you must record: the date, the duration of the cycle, the temperature (must reach at least 121°C/250°F), the pressure, and the results of the chemical indicator. If a spore test fails, you must immediately stop using the autoclave, recall all items from that load, and have the unit serviced. In 2026, the move toward "All-Disposable" studios is driven by the fact that it eliminates the massive liability and labor costs associated with a professional-grade sterilization room.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Weekly Spore Testing is mandatory to verify autoclave performance.</li><li>Maintain a detailed log for every sterilization cycle performed.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: PPE for Artists: Nitrile vs. Latex',
                    'content': """
                        <p>In 2026, <strong>Nitrile Gloves</strong> are the industry standard for body art. Nitrile provides superior puncture resistance compared to latex and is immune to the "degradation" caused by petroleum-based ointments (like A&D or Vaseline), which can cause latex to become porous in minutes. Gloves must be changed if they become torn, heavily soiled, or if you leave the procedure area for any reason. "Double-Gloving" is sometimes used during high-blood procedures (like large-scale heavy saturation) to provide an extra layer of protection.</p>
                        <p>Beyond gloves, <strong>Aprons and Eye Protection</strong> are critical. Micro-splatter from a high-speed tattoo machine can travel several feet. If you are working close to the skin, you should wear clear safety glasses to prevent "Conjunctival Splashes." Your work clothing should be protected by a single-use plastic apron. In 2026, we also emphasize "Grooming Safety": artists with long hair must tie it back, and jewelry (especially rings) should be removed as they can tear gloves and harbor bacteria that standard hand washing cannot reach.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Nitrile is preferred over latex due to better puncture and chemical resistance.</li><li>Change gloves immediately if they touch a non-barrier surface (phone, face, chair).</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Accidental Sticks and Post-Exposure (PEP)',
                    'content': """
                        <p>If you experience an "Artist Stick" (sticking yourself with a needle that has been used on a client), you must act within seconds. <strong>Wash the wound with soap and water</strong> for at least 1 minute. Do not use bleach or "soak" the finger in alcohol, as this can irritate the tissue and spread the virus. Report the incident to the studio owner immediately. In 2026, your studio should have a pre-arranged relationship with an Urgent Care clinic that understands the <strong>72-Hour PEP Window</strong>.</p>
                        <p>Post-Exposure Prophylaxis (PEP) is a course of anti-viral medication that can prevent HIV from taking hold if started immediately after an exposure. Ideally, it should be started within <strong>2 hours</strong>. You also have the right to ask the "Source Client" to go for testing. While you cannot force them in most states, a professional and calm explanation of the situation often leads to cooperation. If the client refuses, you must be treated as if they were positive. Your health is more important than "finishing the piece"—stop the procedure and seek medical attention immediately.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Wash "Artist Sticks" with soap and water immediately; do not use bleach.</li><li>Seek medical attention within 2 hours for the best chance of PEP efficacy.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Studio Decontamination and Waste',
                    'content': """
                        <p>At the end of the day, the studio must undergo a <strong>Terminal Clean</strong>. This involves removing all barriers and disinfecting all surfaces with a 1:10 bleach solution or an EPA-registered tuberculocidal spray. The "Contact Time" is critical: the surface must stay wet with the disinfectant for the time specified on the label (usually 2–10 minutes). If you wipe it dry immediately, the pathogens may survive. This is a common 2026 compliance failure.</p>
                        <p>Biohazard waste management is the final step. Any material "saturated" with blood (meaning it would drip if squeezed) must go in a red <strong>Biohazard Bag</strong>. This includes used paper towels and drapes from heavy-saturation tattoos. Used needles must always go in the sharps container. In 2026, your studio must have a contract with a medical waste disposal company to haul this waste away; you cannot legally dispose of biohazard bags in the regular municipal trash. Proper waste logistics are the mark of a professional, world-class studio.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Disinfectants must remain wet on surfaces for the full "Contact Time" (2-10 mins).</li><li>Saturated waste must go in red bags and be handled by a medical waste company.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: BBP for Body Art updated to World-Class Standards.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
