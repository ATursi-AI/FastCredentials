from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Completes HazCom (GHS) with 12 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Hazard Communication (GHS)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The "Right to Know" and "Right to Understand"',
                    'content': """
                        <p>The OSHA Hazard Communication Standard (HCS), aligned with the <strong>Globally Harmonized System (GHS)</strong>, is built on a simple premise: workers have both a right to know and a <em>right to understand</em> the identities and hazards of the chemicals they are exposed to. In 2026, HazCom is the second most cited OSHA violation. It applies to any workplace where employees may be exposed to hazardous chemicals under normal operating conditions or in foreseeable emergencies. This includes everything from industrial solvents and acids to common office cleaning supplies and toners.</p>
                        <p>The 2026 standard emphasizes that "Understanding" is a higher bar than "Knowledge." It is not enough for an employer to simply provide a binder of papers; they must ensure that the information is accessible, in the correct language, and that employees can interpret the warning signs. As a professional, your role is to act as a barrier between a chemical spill and a human injury. This module establishes the legal framework of the GHS and your responsibility to maintain a "Chemical-Safe" environment through vigilant labeling and awareness.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HazCom is the "Right to Understand" the chemicals in your workspace.</li><li>It applies to all hazardous chemicals, even common industrial cleaning supplies.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The 2026 GHS Pictograms: Visual Warnings',
                    'content': """
                        <p>GHS utilizes nine standardized <strong>Pictograms</strong> to convey health, physical, and environmental hazards. In 2026, these symbols are universal across the globe, ensuring that even in a multilingual workforce, a warning is understood at a glance. You must distinguish between the "Health Hazard" (the silhouette with the star) and the "Exclamation Mark" (irritant). The <strong>Health Hazard</strong> pictogram indicates chronic risks like carcinogens, respiratory sensitizers, or reproductive toxicity. The <strong>Exclamation Mark</strong> indicates acute hazards like skin irritation, narcotic effects, or hazardous to the ozone layer.</p>
                        
                        <p>A critical 2026 focus is the <strong>"Corrosive" vs. "Oxidizer"</strong> distinction. A Corrosive pictogram (showing a chemical dripping onto metal and a hand) indicates a substance that destroys living tissue or metal on contact. An Oxidizer pictogram (the "O" with flames) indicates a chemical that provides oxygen to a fire, making it burn more intensely. In 2026, "Pictogram Fatigue" is a major safety risk. You must treat every symbol with respect, as they represent immediate physical threats to your safety.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Pictograms provide universal, non-verbal warnings for specific chemical hazards.</li><li>The Health Hazard symbol indicates long-term risks like cancer or organ damage.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Signal Words: Danger vs. Warning',
                    'content': """
                        <p>Under GHS, every chemical label and Safety Data Sheet (SDS) must use one of two <strong>Signal Words</strong> to indicate the relative severity of the hazard. In 2026, these are strictly binary: 1. <strong>DANGER</strong> (Indicates more severe hazards). 2. <strong>WARNING</strong> (Indicates less severe, but still significant, hazards). There is no "Caution" or "Notice" in the GHS signal word system. If a label says "DANGER," the risk of permanent injury or death is high if the chemical is mishandled. If it says "WARNING," the risk is typically of a reversible injury or illness.</p>
                        <p>The Signal Word is accompanied by <strong>Hazard Statements</strong> (describing the nature of the hazard, e.g., "Highly flammable liquid and vapor") and <strong>Precautionary Statements</strong> (describing how to minimize exposure). In 2026, many labels also include QR codes that link directly to the full SDS. As a professional, you should never use a chemical if the label is missing or illegible. Proper label maintenance is a core component of your daily safety "pre-flight" check.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>"DANGER" is for the most severe hazards; "WARNING" is for less severe risks.</li><li>Always read the Hazard and Precautionary statements alongside the signal word.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Safety Data Sheets (SDS): The 16 Sections',
                    'content': """
                        <p>The <strong>Safety Data Sheet (SDS)</strong> is the "Technical Manual" for a chemical. In 2026, all SDSs follow a standardized <strong>16-Section Format</strong>. Section 4 covers First-Aid Measures, Section 8 covers Exposure Controls/PPE, and Section 10 covers Stability and Reactivity (what NOT to mix it with). In 2026, cloud-based SDS repositories are common, but OSHA requires that information be accessible to workers <em>without delay</em>. Preparation is the only antidote to chemical accidents.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The SDS is a 16-section document; Section 4 is First Aid, Section 8 is PPE.</li><li>SDSs must be accessible to every employee on every shift without delay.</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Labeling: Primary vs. Secondary Containers',
                    'content': """
                        <p>A "Primary Container" is the one the chemical came in from the manufacturer. In 2026, these must have the full GHS label. A <strong>Secondary Container</strong> (like a spray bottle or a smaller jar you filled) must also be labeled unless it is for <em>immediate use</em> by the person who filled it during their own shift. If you leave the room or the shift ends, that secondary container MUST have a GHS-compliant label showing the product name and the primary hazards. "Mystery liquids" in unlabelled bottles are a leading cause of accidental ingestion and chemical burns in 2026.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Secondary containers must be labeled if not used immediately by the person who filled them.</li><li>Labels must include the product name and key hazard warnings (Pictograms/Signal Word).</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Health Hazards: Acute vs. Chronic Toxicity',
                    'content': """
                        <p>Chemicals can damage your health in two ways. <strong>Acute Toxicity</strong> refers to immediate effects from a single exposure (e.g., a chemical burn or fainting from fumes). <strong>Chronic Toxicity</strong> refers to damage that builds up over years (e.g., cancer or liver damage). In 2026, we focus on <strong>Sensitizers</strong>—chemicals that you might be fine with once, but after repeated exposure, your body develops a severe allergic reaction. Once sensitized, even a tiny amount of the chemical can trigger a life-threatening response.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Acute effects are immediate; Chronic effects develop over long periods.</li><li>Sensitization can turn a common chemical into a life-threatening allergen for you.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Physical Hazards: Flammables and Gases',
                    'content': """
                        <p>Physical hazards are chemicals that can cause fires, explosions, or react violently. <strong>Flammables</strong> have a low "flash point" and can ignite easily at room temperature. <strong>Compressed Gases</strong> (like oxygen or nitrogen tanks) are "sleepy giants"—if the valve is sheared off, the tank can become a rocket capable of punching through concrete walls. In 2026, we also monitor <strong>Pyrophoric</strong> chemicals which ignite spontaneously in air. Proper grounding and bonding are required when transferring flammable liquids to prevent static sparks.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Flammable liquids can ignite at room temperature; keep away from all heat sources.</li><li>Compressed gas cylinders must be secured at all times to prevent valve damage.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: PPE and Engineering Controls',
                    'content': """
                        <p>In 2026, PPE is the "Last Line of Defense." We prioritize <strong>Engineering Controls</strong> (like fume hoods or ventilation) and <strong>Administrative Controls</strong> (like rotating shifts). If these aren't enough, PPE—gloves, goggles, respirators—must be used. You must check Section 8 of the SDS to ensure your gloves are made of the correct material (e.g., Nitrile vs. Latex). Some chemicals will eat right through the wrong type of glove in seconds. Always inspect PPE for cracks or holes before use.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>PPE is the last line of defense; use engineering controls first.</li><li>Check the SDS to ensure your gloves are resistant to the specific chemical you are using.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Spill Response and Emergency Procedures',
                    'content': """
                        <p>If a spill occurs, your first priority is <strong>Safety, not Cleanup</strong>. If you aren't trained for a hazardous spill, evacuate and notify your supervisor. If you are trained, follow the "S.S.S." rule: 1. <strong>Stop</strong> the leak. 2. <strong>Sorb</strong> (absorb) the liquid. 3. <strong>Secure</strong> the area. If a chemical splashes in your eyes, you must use the <strong>Emergency Eyewash</strong> for a full 15 minutes. In 2026, eyewash stations must be reachable within 10 seconds and must provide "tepid" water to prevent thermal shock to the eyes.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Flush eyes or skin for at least 15 minutes after chemical contact.</li><li>Only attempt to clean a spill if you have been specifically trained and have the correct PPE.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Chemical Storage and Incompatibility',
                    'content': """
                        <p>Storing chemicals incorrectly can cause spontaneous fires or toxic gas clouds. The #1 rule: <strong>Never store Incompatibles together</strong>. Oxidizers must be kept away from flammables. Acids must be kept away from bases (cyanides/sulfides). In 2026, we utilize secondary containment (drip trays) to prevent leaks from mixing on the floor. Storage areas must be well-ventilated and away from direct sunlight, which can cause chemicals to degrade or pressure to build in containers.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Store acids and bases separately; keep oxidizers away from flammables.</li><li>Use secondary containment trays to prevent leaks from mixing.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Employee Training Requirements',
                    'content': """
                        <p>OSHA requires HazCom training whenever a <strong>New Hazard</strong> is introduced to the workspace. It is not a "once and done" event. In 2026, training must be "Effective," meaning it is delivered in a way that employees can actually apply. You must know how to read your facility's specific labels and where the SDSs are stored. If you are a temporary worker or a contractor, the host employer is responsible for training you on the specific hazards of that site. You are the final link in the safety chain.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>You must be re-trained every time a new chemical hazard is introduced.</li><li>Contractors must be trained on the specific hazards of the site where they are working.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Digital HazCom Era',
                    'content': """
                        <p>We conclude with the <strong>Digital Future of Safety</strong>. In 2026, many facilities use "Smart Shelving" that alerts managers if incompatible chemicals are placed next to each other. Wearable sensors can now detect invisible toxic vapors and vibrate to warn the worker to leave the area. While these tools are incredible, they do not replace the <strong>Human Element</strong>. Vigilance, curiosity, and a commitment to the "Right to Understand" are what keep you safe. By completing this training, you are a certified guardian of the chemical workspace.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Digital sensors are a backup, not a replacement for manual safety checks.</li><li>Vigilance and understanding the SDS are your primary tools for survival.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)

            # --- EXAM (15 QUESTIONS) ---
            qs = [
                ('What does "GHS" stand for?', ['General Health System', 'Globally Harmonized System', 'Global Hazard Standard', 'Government Health Safety'], 2),
                ('Which Signal Word indicates the MOST severe hazard?', ['Warning', 'Caution', 'Danger', 'Notice'], 3),
                ('What does the "Health Hazard" pictogram (silhouette with a star) indicate?', ['Immediate skin irritation', 'Chronic risks like cancer or respiratory toxicity', 'Explosive materials', 'Environmental damage'], 2),
                ('How many sections are in a standardized GHS Safety Data Sheet (SDS)?', ['10', '16', '12', '8'], 2),
                ('Where should you look for First Aid instructions in an SDS?', ['Section 1', 'Section 4', 'Section 8', 'Section 16'], 2),
                ('When must a Secondary Container be labeled?', ['Never', 'Only if it is over 5 gallons', 'If it is not for immediate use by the person who filled it', 'Only if it contains acid'], 3),
                ('What is the "Right to Understand" in 2026?', ['The right to have labels in your native language', 'The right to be trained in a way that is actually effective and applicable', 'The right to ignore safety signs', 'The right to see the boss\'s emails'], 2),
                ('What is the difference between an Oxidizer and a Flammable?', ['Oxidizers put out fires', 'Oxidizers provide oxygen that makes fires burn more intensely', 'Flammables are always liquids', 'There is no difference'], 2),
                ('How long should you flush your eyes at an eyewash station?', ['30 seconds', '5 minutes', '15 minutes', 'Until it stops stinging'], 3),
                ('What is a "Sensitizer"?', ['A chemical that smells good', 'A chemical that causes an allergic-like reaction after repeated exposure', 'A chemical that cleans skin', 'A type of glove'], 2),
                ('Where do you find the specific PPE (gloves/respirator) needed for a chemical?', ['Section 1 of the SDS', 'Section 8 of the SDS', 'On the bottom of the bottle', 'In the HR handbook'], 2),
                ('What is "Acute Toxicity"?', ['Long-term damage over years', 'Immediate effects from a single exposure', 'A chemical that only affects animals', 'The weight of the chemical'], 2),
                ('Why should you NOT store acids and bases together?', ['They will evaporate', 'They can react violently if they mix', 'It is too expensive', 'They smell bad'], 2),
                ('What should you do if a chemical label is missing or illegible?', ['Use it anyway', 'Guess what it is based on the smell', 'Do not use it and notify your supervisor immediately', 'Throw it in the regular trash'], 3),
                ('What is the "Last Line of Defense" in the hierarchy of controls?', ['Engineering Controls', 'PPE (Personal Protective Equipment)', 'Elimination', 'Administrative Controls'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: HazCom (GHS) is now World-Class (21/24 Complete).'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
