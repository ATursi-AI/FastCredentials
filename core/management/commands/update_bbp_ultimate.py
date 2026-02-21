from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades BBP to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Bloodborne Pathogens')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 OSHA 1910.1030 Mandate',
                    'content': """
                        <p>The OSHA Bloodborne Pathogens Standard (29 CFR 1910.1030) is a performance-based federal law. In 2026, the mandate has been refined to emphasize <strong>The Exposure Control Plan (ECP)</strong> as a "living document." An ECP is not a binder on a shelf; it must be reviewed and updated annually to reflect changes in technology (Safer Medical Devices) and shifts in personnel. Employers must solicit input from non-managerial "front-line" employees when evaluating new engineering controls. This ensures that the people actually using the needles have a say in which safety devices are implemented.</p>
                        <p>A critical 2026 update involves the <strong>Sharps Injury Log</strong>. Organizations with 11 or more employees must maintain a detailed log of every percutaneous (skin-piercing) injury from a contaminated sharp. This log must maintain employee privacy while detailing exactly which device was used, where the injury occurred, and the "Mechanism of Failure" of the safety device. By analyzing this data, the 2026 professional can identify "Cluster Trends"—if a specific brand of safety-needle is failing at a high rate, the ECP must be updated to replace that device. This data-driven approach is the hallmark of a world-class safety program.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The ECP must be updated annually with input from front-line staff.</li><li>The Sharps Injury Log is a mandatory tool for identifying device failure trends.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Epidemiology: The 2026 Pathogen Landscape',
                    'content': """
                        <p>While hundreds of pathogens exist, 2026 protocols focus on the "Big Three": <strong>HBV, HCV, and HIV</strong>. Hepatitis B (HBV) remains the primary occupational threat because of its extreme environmental stability. In 2026, clinical data confirms that HBV can survive in dried blood on a surface for at least <strong>7 days</strong>. It is significantly more infectious than HIV; a needlestick from an HBV-positive source has a 6% to 30% chance of causing infection, whereas an HIV-positive stick has only a 0.3% chance. Hepatitis C (HCV) is the most common chronic bloodborne infection in the US, and currently, there is no vaccine available.</p>
                        
                        <p>The 2026 standard for HIV management has been revolutionized by <strong>U=U (Undetectable = Untransmittable)</strong>. If a source patient is on consistent Antiretroviral Therapy (ART) and has an undetectable viral load, the risk of transmission to a healthcare worker through an accidental exposure is effectively zero. However, in the absence of known source data, the 2026 protocol assumes "Universal Precautions." We also monitor "Emerging Pathogens" such as viral hemorrhagic fevers and drug-resistant bacteria that may be present in blood. Understanding the "Survival Physics" of these viruses dictates why environmental disinfection (using 1:10 bleach or EPA-registered tuberculocidal agents) is a non-negotiable step in post-procedure cleanup.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HBV can survive on dry surfaces for 7 days; it is much more infectious than HIV.</li><li>HCV is the most common chronic bloodborne infection and has no vaccine.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Engineering Controls: Needlesafe 3.0',
                    'content': """
                        <p>Engineering Controls are the most effective way to prevent exposure because they <strong>isolate the hazard</strong> at the source. In 2026, we have moved beyond simple "self-sheathing" needles to <strong>Active and Passive Safety Systems</strong>. A "Passive" system requires no action from the user (e.g., a needle that automatically retracts into the syringe barrel upon completion of the injection). An "Active" system requires the user to flip a guard or click a button. 2026 OSHA standards mandate that if a safer medical device exists and is clinically appropriate, the employer MUST use it. Cost is generally not a valid legal excuse for choosing a non-safety device.</p>
                        <p>Common 2026 engineering controls include: <strong>Shielded Needle Systems</strong>, <strong>Blunt Suture Needles</strong> (reducing O.R. sticks by 80%), and <strong>Needleless IV Connectors</strong>. The "Sharps Container" is also a critical engineering control. It must be puncture-resistant, leak-proof on the sides and bottom, and labeled with the Biohazard symbol. In 2026, the "3/4 Full Rule" is strictly enforced: once a sharps container reaches the fill line (usually 75% capacity), it must be locked and replaced. Overfilling a sharps container—or reaching inside to "make room"—is one of the leading causes of preventable needlestick injuries in clinical settings.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Engineering controls isolate the hazard (e.g., retractable needles, sharps containers).</li><li>Replace sharps containers when 3/4 full; never overfill or force items inside.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Universal vs. Standard Precautions',
                    'content': """
                        <p>The 2026 standard has evolved from "Universal Precautions" (focusing only on blood) to <strong>"Standard Precautions."</strong> Standard Precautions assume that ALL human blood and "Other Potentially Infectious Materials" (OPIM)—including semen, vaginal secretions, cerebrospinal fluid, and any body fluid visibly contaminated with blood—are infectious. In 2026, the only body fluid generally excluded from this mandate (unless it contains visible blood) is <strong>Sweat</strong>. Fluids like saliva in dental procedures are always treated as OPIM due to the high likelihood of trauma-induced blood presence.</p>
                        
                        <p>Standard Precautions require the use of Personal Protective Equipment (PPE) whenever there is a "Reasonable Anticipation" of contact with blood or OPIM. This includes non-intact skin (cuts, rashes, or dermatitis) and mucous membranes (eyes, nose, mouth). In 2026, "Risk-Based Assessment" is the primary skill: if a procedure has a high "splash potential" (such as a trauma irrigation), a mask and eye protection are mandatory, not optional. By treating every patient as a potential carrier, we eliminate the bias and errors that occur when workers try to "guess" who is healthy and who is not.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Standard Precautions treat all blood and OPIM as infectious.</li><li>Saliva in dental settings is always treated as OPIM.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Work Practice Controls and "No-Touch" Zones',
                    'content': """
                        <p>Work Practice Controls reduce exposure by changing <strong>the way a task is performed</strong>. Unlike engineering controls, these depend on the behavior of the worker. In 2026, the most critical work practice control is the <strong>Prohibition of Recapping</strong>. Needles must never be bent, sheared, or recapped using a two-handed technique. If recapping is medically necessary (such as in certain dental anesthesia procedures), a "One-Handed Scoop" technique or a mechanical recapping device must be used. Furthermore, the 2026 "No-Touch" Zone in surgical suites requires that sharps be passed in a "Neutral Zone" (a tray or basin) rather than hand-to-hand.</p>
                        <p>Additional work practice controls involve the <strong>Prohibition of Consumables</strong> in exposure areas. You are strictly forbidden from eating, drinking, smoking, applying cosmetics (including lip balm), or handling contact lenses in any area where blood or OPIM are present. These actions provide a "Portal of Entry" for pathogens to enter your mucous membranes via contaminated hands. Even if you are wearing gloves, the "fomite" transfer of viruses to your face can occur during these activities. 2026 compliance requires a total "Clean Zone/Dirty Zone" separation in the workplace to prevent these accidental self-inoculations.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never recap needles using two hands; use the "one-handed scoop" if necessary.</li><li>No eating, drinking, or applying cosmetics in areas of potential exposure.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Hand Hygiene: The 2026 Science',
                    'content': """
                        <p>Hand hygiene remains the single most important practice to prevent the transmission of bloodborne pathogens. In 2026, the CDC distinguishes between <strong>Hand Washing</strong> (soap and water) and <strong>Hand Rubbing</strong> (alcohol-based hand rub/ABHR). ABHR is the preferred method for decontaminating hands if they are not visibly soiled because it is faster, more effective against most pathogens, and less irritating to the skin. However, if your hands are visibly contaminated with blood or OPIM, you <strong>MUST use soap and water</strong>. The mechanical action of scrubbing and rinsing is required to physically remove the organic protein (blood) that can "shield" viruses from the alcohol in a hand rub.</p>
                        
                        <p>The "Gloves are not a Substitute" rule is a 2026 focal point. Gloves are porous at a microscopic level and can develop "micro-tears" during use. Therefore, hand hygiene must be performed <strong>immediately after glove removal</strong>. If a sink is not immediately available, an alcohol-based rub must be used until a sink can be reached. Proper technique involves scrubbing for at least 20 seconds, focusing on the "high-load" areas: under the fingernails, between the fingers, and the backs of the hands. In 2026, "Artificial Nails" and long natural nails are restricted in high-risk clinical settings because they harbor high concentrations of pathogens that are resistant to standard washing.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Wash with soap and water if hands are visibly soiled; otherwise, ABHR is preferred.</li><li>Always perform hand hygiene immediately after removing gloves.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Personal Protective Equipment (PPE) Mastery',
                    'content': """
                        <p>PPE is the "Last Resort" in the hierarchy of controls. In 2026, the selection of PPE is based on the <strong>Anticipated Level of Exposure</strong>. For routine blood draws, gloves are sufficient. For procedures with "Spurt" or "Spray" potential (e.g., arterial bleeds or suctioning), a combination of gloves, fluid-resistant gowns, surgical masks, and eye protection (goggles or face shields) is mandatory. Standard prescription glasses are NOT considered eye protection; they lack the side-shields and impact-resistance required to prevent a lateral splash from entering the eye.</p>
                        <p>The 2026 <strong>Donning and Doffing</strong> (putting on and taking off) sequence is designed to prevent self-contamination. Most exposures occur while removing contaminated PPE. Gloves must be removed using the "Glove-to-Glove, Skin-to-Skin" technique to ensure the soiled exterior never touches your bare skin. Gowns should be pulled away from the body and rolled inward. PPE must be removed before leaving the work area and placed in designated "Biohazard" containers. Never "reuse" disposable PPE, and never wear contaminated gloves into "clean" areas like hallways, elevators, or breakrooms. This "Containment Discipline" is what separates a professional from a liability.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>PPE is selected based on the "Anticipated Level" of fluid contact.</li><li>Prescription glasses are not eye protection; goggles or face shields are required.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Hepatitis B Vaccination and 2026 Heplisav-B',
                    'content': """
                        <p>The Hepatitis B (HBV) vaccine is the most powerful tool in the BBP arsenal. In 2026, OSHA requires all employers to offer the HBV vaccine series to employees with "Occupational Exposure" within 10 days of initial assignment. The vaccine must be provided at no cost, at a reasonable time and place, and performed by a licensed healthcare professional. While an employee can "Decline" the vaccine, they must sign a specific <strong>OSHA Declination Statement</strong>. An employee who declines today can change their mind at any time and receive the vaccine for free as long as they are still covered by the standard.</p>
                        <p>The 2026 standard includes the <strong>2-Dose Heplisav-B</strong> protocol. Unlike the traditional 3-dose series that takes 6 months to complete, the 2-dose series can be completed in just 1 month and has shown higher "Seroprotection" rates (above 95%). After completion of the series, "Titer Testing" (antibody testing) is performed to confirm immunity. If an employee is a "Non-Responder" after two full series, they are managed as "Susceptible" to HBV in the event of an exposure. In 2026, the vaccine is considered "Safe and Highly Effective," and there is no evidence that it can cause HBV or any other viral infection.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Employers must offer the HBV vaccine for free within 10 days of hire.</li><li>Employees can decline but must sign an OSHA-mandated declination form.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: The 72-Hour Window: Exposure Protocol',
                    'content': """
                        <p>If an exposure incident occurs—such as a contaminated needlestick or a splash to a mucous membrane—the <strong>First 60 Seconds</strong> are critical. Immediately wash the area with soap and water. If the eyes are involved, flush with water or saline for at least 15 minutes. <strong>Do not use bleach</strong>, antiseptics, or "squeeze" the wound; these actions can damage the tissue and actually facilitate the entry of the virus into the bloodstream. Once the area is cleaned, you must report the incident to your supervisor immediately to initiate the "Post-Exposure Evaluation."</p>
                        <p>The 2026 clinical standard for HIV prevention is <strong>Post-Exposure Prophylaxis (PEP)</strong>. PEP consists of taking antiretroviral medications to prevent the virus from taking hold in your body. For PEP to be effective, it MUST be started as soon as possible—ideally within 2 hours, and <strong>no later than 72 hours</strong> after exposure. After 72 hours, the virus has usually integrated into the host's cells, and PEP is no longer effective. This is why immediate reporting is a medical necessity, not just an HR requirement. You have a right to a confidential medical evaluation, source patient testing (if legal and possible), and follow-up testing at 6 weeks, 3 months, and 6 months.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Wash the area with soap and water; do not use bleach or squeeze the wound.</li><li>PEP must be started within 72 hours (ideally within 2 hours) to be effective.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Decontamination and Spills',
                    'content': """
                        <p>Environmental decontamination is the process of using physical or chemical means to remove, inactivate, or destroy bloodborne pathogens on a surface. In 2026, we utilize <strong>EPA-Registered Tuberculocidal Disinfectants</strong> or a fresh solution of household bleach diluted 1:10 with water. Bleach solutions must be made fresh every 24 hours, as the chlorine breaks down and loses its "kill power" rapidly. For a blood spill, the 2026 "Mechanical First" rule applies: use absorbent material to soak up the bulk of the blood first, then apply the disinfectant. Applying disinfectant directly to a large pool of blood can "neutralize" the chemical before it can reach the pathogens.</p>
                        <p>Safety during cleanup is paramount. Never pick up broken glass or contaminated sharps with your hands, even if you are wearing gloves. Use <strong>Mechanical Means</strong>: a brush and dustpan, tongs, or forceps. All contaminated material—including the broken glass and the absorbent towels—must be placed in a red "Biohazard" bag. In 2026, the distinction between "Regulated Waste" (dripping with blood) and "Non-Regulated Waste" (a slightly soiled band-aid) is critical for cost and safety. If an item is "saturated" and could release blood if compressed, it is Regulated Waste and must be disposed of in a professional biohazard waste stream.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use 1:10 bleach (freshly mixed) or EPA-registered tuberculocidal agents.</li><li>Never pick up broken glass with hands; use tongs or a brush and dustpan.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Biohazard Logistics and Labeling',
                    'content': """
                        <p>The <strong>Biohazard Symbol</strong> is one of the most recognized safety icons in the world. In 2026, OSHA mandates that this symbol must be fluorescent orange or orange-red, with the symbol and lettering in a contrasting color. It must be prominently displayed on any container used to store, transport, or ship blood or OPIM. This includes waste containers, refrigerators containing specimens, and containers used to transport contaminated laundry. Labeling provides an immediate "Visual Warning" to everyone in the vicinity that the material inside is potentially infectious and requires specialized handling.</p>
                        
                        <p>A common 2026 compliance error involves "Secondary Labeling." If you move a biohazard from a labeled bag to a secondary container for transport, that secondary container must also be labeled. Exceptions to the labeling rule include: 1. Individual containers of blood/OPIM placed in a labeled secondary container for transport. 2. Red bags or red containers, which are universally recognized as biohazards (the "Red Bag Rule"). However, for shipping outside the facility, strict <strong>DOT Biohazard Regulations</strong> apply, including double-bagging and leak-proof primary containers. Proper labeling ensures that the "Chain of Safety" is never broken from the point of generation to the point of final incineration.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Biohazard symbol must be orange-red and attached to all containers of OPIM.</li><li>The "Red Bag Rule" allows a red bag to substitute for a symbol in internal use.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The Rescuer Mindset: Rights and Recordkeeping',
                    'content': """
                        <p>The final module focuses on your <strong>Legal Rights</strong> as a protected worker. In 2026, OSHA requires that your employer maintain a Medical Record for the duration of your employment PLUS 30 years. This ensures that if you develop a chronic condition (like Hepatitis C) decades after an exposure, the records of that incident are available for workers' compensation claims. These records are strictly confidential and cannot be shared with your manager or coworkers without your written consent. You have a right to a copy of your records and the results of any "Source Patient" testing performed after an exposure.</p>
                        <p>Beyond rights, we emphasize <strong>Professional Vigilance</strong>. A world-class professional doesn't just "follow the rules" when being watched; they maintain a culture of safety even when alone. This means speaking up if you see a coworker not wearing eye protection during a splash-risk procedure, and it means reporting every "Near-Miss"—the needlestick that *didn't* happen because you were careful, but *could* have happened because of a poor room layout. By completing this 2026 certification, you are now a part of the "Human Firewall" against infectious disease. Stay alert, stay protected, and stay professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Medical records must be kept for the duration of employment plus 30 years.</li><li>Records are confidential and cannot be shared without your written consent.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: BBP (Pathogen Defense) 12-Module Upgrade Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
