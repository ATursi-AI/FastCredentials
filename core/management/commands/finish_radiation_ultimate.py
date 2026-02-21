from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Radiation Safety with Modules 5-12 at World-Class Density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Radiation Safety')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Biological Effects: Deterministic vs. Stochastic',
                    'content': """
                        <p>The biological impact of radiation is categorized into two distinct types. <strong>Deterministic Effects</strong> (Tissue Reactions) have a threshold; once you receive a certain dose, the damage is guaranteed. These include radiation-induced skin erythema (burns), hair loss, and acute radiation syndrome. In 2026, we monitor the "Dose-to-Skin" during long interventional procedures to prevent these injuries. <strong>Stochastic Effects</strong>, however, have no known safe threshold. These are random events, such as cancer or genetic mutations, where the <em>probability</em> of the effect increases with the dose, but the severity does not. Even a small "scatter" dose increases your lifetime stochastic risk.</p>
                        <p>The most sensitive tissues in the human body are those with high rates of cell division, such as the bone marrow, the lining of the intestines, and reproductive cells. In 2026, we also recognize the <strong>Cumulative Biological Burden</strong>. Every X-ray you receive or assist with adds to your lifetime "risk bucket." This is why ALARA is not just a workplace rule, but a life-long health strategy. Professionals who ignore shielding today are essentially gambling with stochastic outcomes 20 years in the future. Protecting your "Biological Capital" through rigid adherence to distance and shielding is the only way to ensure a long, healthy career in the radiological environment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Deterministic effects (burns) happen after a threshold; Stochastic (cancer) can happen at any dose.</li><li>Cells with high division rates (bone marrow, intestines) are most vulnerable to radiation.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Lead Apron Integrity and Care',
                    'content': """
                        <p>A lead apron is only effective if it is physically intact. In 2026, the <strong>Annual Fluoroscopic Inspection</strong> is a mandatory NRC and Joint Commission requirement. Every lead garment (apron, thyroid shield, and leaded glasses) must be uniquely numbered and tracked. Once a year, they must be placed under an X-ray or Fluoroscope to check for internal cracks, holes, or "thinning" of the lead core. If a crack is found in the "Critical Area" (the torso), the garment must be removed from service immediately. A crack as small as a few millimeters can allow a "Hot Spot" of radiation to reach your internal organs.</p>
                        
                        <p>Proper care extends the life of your lead. <strong>Never fold your lead apron.</strong> Folding causes the lead lining to crease and eventually crack. Aprons must be hung on dedicated heavy-duty hangers or stored on specialized rollers. In 2026, we also emphasize "Hybrid Shielding"—garments made of bismuth or tungsten-infused rubber that are 20-30% lighter than traditional lead while providing equivalent protection. Regardless of the material, you must ensure the "Lead Equivalence" (usually 0.5mm) is appropriate for the energy levels of the X-ray machines in your facility. Cleaning should be done with mild soap; harsh chemicals can degrade the protective vinyl covering.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Lead garments must undergo an annual fluoroscopic inspection for internal cracks.</li><li>Never fold lead aprons; always hang or roll them to prevent core damage.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Shielding the Lens and Thyroid',
                    'content': """
                        <p>The thyroid gland and the lens of the eye are two of the most radiation-sensitive areas of the head and neck. In 2026, <strong>Radiation-Induced Cataracts</strong> are recognized as a major occupational hazard for interventionalists who do not use eye protection. The lens of the eye has no way to clear dead cells caused by radiation; instead, they accumulate and turn the lens opaque. Lead-equivalent glasses (0.75mm Pb) with side shields are mandatory for anyone standing within 3 feet of a C-arm. Standard prescription glasses or "plastic" safety glasses provide zero protection against ionizing X-ray photons.</p>
                        <p>The thyroid gland is highly susceptible to radiation-induced carcinoma. A properly fitted <strong>Thyroid Shield</strong> (0.5mm Pb) should be worn snugly around the neck, leaving no gap between the shield and the top of the apron. In 2026, we utilize "Overlap Coverage" to ensure that the carotid arteries and the thyroid are protected from scatter. If you are scrubbed and cannot adjust your shield, ensure the circulator assists you before the procedure begins. Protecting these "Vital Glands" is a non-negotiable component of the 2026 O.R. uniform; ignoring this protection is a Tier 1 violation of the facility's Radiation Safety Manual.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Radiation-induced cataracts are permanent; leaded glasses are mandatory for near-source work.</li><li>Thyroid shields must be worn snugly to protect against radiation-induced carcinoma.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: The 2026 Pregnant Worker Protocol',
                    'content': """
                        <p>Radiation safety for the pregnant worker (the "Declared Pregnant Worker") is built on the protection of the developing fetus, which is significantly more sensitive to radiation than an adult. In 2026, once a worker "Declares" their pregnancy in writing, the facility must provide a <strong>Fetal Dosimeter</strong>. This second dosimeter is worn at the <strong>waist level, underneath the lead apron</strong>. The NRC limit for the fetus is 0.5 Rem (5 mSv) for the entire duration of the pregnancy, with a recommendation of no more than 0.05 Rem per month. This "Double-Monitoring" ensures the fetus never exceeds these tight safety margins.</p>
                        <p>A 2026 world-class facility does not "ban" pregnant workers from the O.R., but it does implement <strong>Workplace Modifications</strong>. This may include "Distance Rotation"—assigning the pregnant worker to tasks further from the X-ray tube—or providing "Wrap-Around" lead aprons that offer 1.0mm Pb equivalent protection for the abdomen. The pregnant worker has a right to a confidential consultation with the Radiation Safety Officer (RSO) to review their dose history and ensure their safety. In 2026, the "Right to Know" is paramount; the worker must be informed of the specific risks of "Organogenesis" (fetal organ development) during the first trimester, which is the period of highest sensitivity.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Declared pregnant workers wear a second "Fetal Dosimeter" under the apron at the waist.</li><li>The fetal dose limit is 0.5 Rem for the entire pregnancy to prevent developmental risks.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: The 2026 Shift in Patient Shielding',
                    'content': """
                        <p>One of the most significant 2026 clinical shifts is the <strong>Reduction in Patient Gonadal Shielding</strong> for certain exams. For decades, we placed lead over a patient's reproductive organs for every X-ray. However, 2026 research from the AAPM (American Association of Physicists in Medicine) indicates that modern digital X-ray systems are so sensitive that the lead shield can actually <em>increase</em> the dose. This happens because the "Automatic Brightness Control" (ABC) sees the heavy lead and automatically ramps up the X-ray power to "see through" it, inadvertently delivering a higher dose to the patient's internal organs.</p>
                        <p>Furthermore, shields can often obscure the very anatomy the doctor needs to see, leading to "Repeats"—which double the patient's exposure. In 2026, the standard is <strong>Selective Shielding</strong>. We only shield the patient if it does not interfere with the diagnostic quality of the image or the automatic sensors of the machine. The primary way we protect patients in 2026 is through <strong>Collimation</strong>—narrowing the X-ray beam so it only hits the specific area of interest. By "tightening the shutters," we eliminate the unnecessary scatter to the rest of the patient's body, providing a far more effective safety benefit than a piece of lead ever could.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Patient shielding is now selective; it can interfere with modern automatic dose sensors.</li><li>Collimation (narrowing the beam) is the most effective way to protect the patient in 2026.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Radioactive Seeds and Contrast Media',
                    'content': """
                        <p>In 2026, we utilize <strong>Brachytherapy</strong>—the placement of tiny radioactive "seeds" (often Iodine-125 or Palladium-103) directly into a tumor. For the O.R. professional, this introduces the risk of "Source Management." These seeds are permanent implants, but they are highly radioactive when first placed. You must follow strict "Chain of Custody" protocols to ensure no seeds are lost in the O.R. or accidentally discarded in the trash. Any patient with implanted seeds must be given a "Radiation Wallet Card" explaining their status to emergency personnel or airport security.</p>
                        <p>We also monitor for <strong>Radioactive Contrast Media</strong> used in nuclear medicine and PET scans. Unlike X-rays, which stop when the machine is turned off, a patient who has received a radioactive isotope is <strong>a walking source</strong>. Their blood, urine, and even sweat may be radioactive for several hours or days depending on the isotope's "Half-Life." In 2026, we follow "Universal Precautions for Isotopes": wear double gloves, use disposable floor covers, and utilize "Time and Distance" when providing care to these patients. Any spill of radioactive contrast is a "Hazardous Material" event that requires immediate isolation and cleanup by the RSO.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Radioactive seeds require a strict "Chain of Custody" to prevent loss or accidental disposal.</li><li>Nuclear medicine patients are active radiation sources; handle their fluids with double gloves.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Signage, Postings, and Access Control',
                    'content': """
                        <p>Radiation safety depends on clear visual warnings. In 2026, NRC-mandated signage is categorized by the level of risk. 1. <strong>"Radiation Area"</strong>: An area where an individual could receive more than 5 mrem in one hour. 2. <strong>"High Radiation Area"</strong>: An area where an individual could receive more than 100 mrem in one hour. These areas must be clearly marked with the magenta-on-yellow <strong>Trefoil Symbol</strong>. In a 2026 hospital, these signs are often "Smart Postings"—digital displays that light up "X-RAY IN USE" only when the beam is active to prevent "Warning Fatigue."</p>
                        
                        <p>Access control is the second layer of defense. Doors to X-ray suites and O.R.s using fluoroscopy must remain closed and, in high-dose areas, may be interlocked with the X-ray machine. If the door is opened, the beam automatically shuts off. As a professional, you must never "prop open" a door to a radiation area for convenience. You are also responsible for <strong>"Unauthorized Entry" Prevention</strong>—ensuring that family members, cleaning staff, or other "Unqualified Persons" do not wander into the scatter zone during an active procedure. In 2026, your "Visual Sweep" of the room before hitting the "Expose" button is a mandatory legal safety step.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "Trefoil" symbol (magenta/yellow) marks all radiation-controlled areas.</li><li>Never prop open doors to X-ray suites; you are responsible for preventing unauthorized entry.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Emergency Response: The "Stuck Shutter"',
                    'content': """
                        <p>The final module covers the "Worst-Case" scenarios. In 2026, the most common equipment emergency is the <strong>"Stuck Shutter" or "Continuous Beam"</strong> event, where the X-ray machine fails to turn off after the pedal is released. The protocol is immediate: 1. <strong>Push the Emergency Stop (E-Stop) Button</strong> on the console. 2. If the E-Stop fails, <strong>Unplug the Machine</strong> or flip the main circuit breaker. 3. Move the patient and staff out of the room immediately. You must never attempt to "fix" a malfunctioning radiation source yourself. The room must be locked, and the RSO must be notified to perform a "Dose Reconstruction" for the patient and staff.</p>
                        <p>We conclude with the <strong>Professional Responsibility</strong> of the radiation worker. By completing this 2026 certification, you have mastered the "Invisible Science." You understand that your lead apron is not a "lucky charm"—it is a piece of precision engineering that must be inspected and cared for. You understand that distance is your best friend and that ALARA is a lifelong commitment to your own DNA. Radiation is a powerful tool for healing, but only in the hands of a professional who respects its power. Stay distant, stay shielded, and stay professional. You are now a certified guardian of Radiation Safety.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>In a "Stuck Shutter" event, push the Emergency Stop or unplug the machine immediately.</li><li>Radiation safety is a lifelong commitment to protecting your DNA through ALARA.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Radiation Safety 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
