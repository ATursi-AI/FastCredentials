from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Upgrades HazCom (GHS) to Platinum Standard (High Density)'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Hazard Communication (GHS)')
            # We keep the questions, only rewriting the lesson content for density.
            course.lessons.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The Regulatory Framework: OSHA 1910.1200 and the GHS',
                    'content': """
                        <p>The Hazard Communication Standard (HCS), codified in <strong>29 CFR 1910.1200</strong>, is the law of the land. In 2026, it is fully harmonized with the <strong>United Nations Globally Harmonized System (GHS)</strong> Revision 7. This alignment ensures that a chemical manufactured in Germany carries the exact same warning label as one made in Ohio. The core philosophy has shifted from the "Right to Know" to the <strong>"Right to Understand."</strong> It is not enough to simply have Safety Data Sheets (SDSs) in a binder; employers must demonstrate that employees can actually <em>read, interpret, and act</em> upon the hazard information provided.</p>
                        <p>The standard applies to <strong>"All Chemicals Known to be Present"</strong> in the workplace to which employees may be exposed under normal conditions of use or in a foreseeable emergency. This includes simple cleaning supplies if used in greater volume/frequency than a standard consumer would use. Manufacturers and importers are responsible for evaluating the hazards (classification) and producing the label and SDS. Employers are responsible for the written HazCom program, maintaining the SDS library, and training employees. Employees are responsible for reading the label <em>before</em> every use. Ignorance of the hazard is not a defense; it is a violation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>OSHA 1910.1200 is aligned with the UN GHS Revision 7 for global consistency.</li><li>The "Right to Understand" requires employers to verify employee comprehension, not just attendance.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The 9 GHS Pictograms: A Visual Language',
                    'content': """
                        <p>The GHS utilizes nine standardized <strong>Pictograms</strong> (black symbols on a white background with a red diamond border) to convey specific hazards instantly. In 2026, you must be able to identify these without hesitation:
                        <br><strong>1. Health Hazard (Silhouette with Star):</strong> Indicates chronic, long-term health risks such as Carcinogenicity, Mutagenicity, Reproductive Toxicity, Respiratory Sensitization, and Target Organ Toxicity (STOT). This is the "silent killer" symbol.
                        <br><strong>2. Flame:</strong> Flammables, Pyrophorics, Self-Heating, Emits Flammable Gas, Self-Reactives, Organic Peroxides.
                        <br><strong>3. Exclamation Mark:</strong> Irritant (skin and eye), Skin Sensitizer, Acute Toxicity (harmful), Narcotic Effects, Respiratory Tract Irritation.
                        <br><strong>4. Gas Cylinder:</strong> Gases under pressure (Compressed, Liquefied, Dissolved). Risk of explosion if heated or projectile hazard if valve breaks.
                        <br><strong>5. Corrosion:</strong> Skin Corrosion/Burns, Eye Damage, Corrosive to Metals.
                        <br><strong>6. Exploding Bomb:</strong> Explosives, Self-Reactives, Organic Peroxides.
                        <br><strong>7. Flame Over Circle:</strong> Oxidizers. These chemicals provide oxygen to a fire, making it burn hotter and faster. *Critical distinction from the standard Flame.*
                        <br><strong>8. Skull and Crossbones:</strong> Acute Toxicity (fatal or toxic). Immediate danger to life upon exposure.
                        <br><strong>9. Environment (Dead Tree/Fish):</strong> Aquatic toxicity. (Note: Not mandatory under OSHA but common on labels).</p>
                        
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "Health Hazard" pictogram indicates chronic risks like cancer; "Skull and Crossbones" is acute lethality.</li><li>"Flame Over Circle" specifically identifies Oxidizers, which are distinct from Flammables.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Signal Words, Hazard Statements, and Precautionary Statements',
                    'content': """
                        <p>The 2026 GHS label is a precision document. It includes three critical text elements that define the risk level:
                        <br><strong>1. Signal Word:</strong> A binary indicator of severity.
                        <br>&nbsp;&nbsp;- <strong>DANGER:</strong> Used for more severe hazards (e.g., Category 1 or 2). Risk of death or permanent injury.
                        <br>&nbsp;&nbsp;- <strong>WARNING:</strong> Used for less severe hazards. Risk of reversible injury or illness.
                        <br>There is no "Caution" in GHS. If a label says DANGER, you are handling a high-threat substance.
                        <br><strong>2. Hazard Statements:</strong> Standardized phrases assigned to a hazard class and category that describe the nature of the hazard. Examples: "Highly flammable liquid and vapor," "Causes severe skin burns and eye damage," "May cause cancer." These phrases are fixed and cannot be altered by the manufacturer.
                        <br><strong>3. Precautionary Statements:</strong> Recommended measures to minimize or prevent adverse effects. They are grouped into four types: <strong>Prevention</strong> ("Keep away from heat"), <strong>Response</strong> ("If on skin: Wash with plenty of water"), <strong>Storage</strong> ("Store in a well-ventilated place"), and <strong>Disposal</strong> ("Dispose of contents in accordance with local regulations"). Always read the "Response" section <em>before</em> you start work so you know the immediate first aid protocol.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>"DANGER" indicates severe hazards; "WARNING" indicates moderate hazards.</li><li>Read the "Response" precautionary statements BEFORE opening the container to know the first aid plan.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Safety Data Sheets (SDS): Sections 1-8',
                    'content': """
                        <p>The SDS is the "User Manual" for the chemical. It must follow a strict 16-section format. In 2026, finding information quickly is a required skill.
                        <br><strong>Section 1: Identification.</strong> Product name, manufacturer contact, and emergency phone number (Chemtrec).
                        <br><strong>Section 2: Hazard(s) Identification.</strong> The GHS classification, signal word, pictograms, and hazard statements. This is your "Executive Summary" of the risk.
                        <br><strong>Section 3: Composition/Information on Ingredients.</strong> Lists the ingredients and their concentration ranges. Trade secrets may be listed as "Proprietary," but the hazards must still be disclosed.
                        <br><strong>Section 4: First-Aid Measures.</strong> *Critical.* Describes initial care for exposure routes (inhalation, skin, eye, ingestion). It differentiates between immediate and delayed symptoms.
                        <br><strong>Section 5: Fire-Fighting Measures.</strong> Suitable extinguishing media (e.g., "Do not use water jet") and special hazards arising from the fire (e.g., toxic fumes).
                        <br><strong>Section 6: Accidental Release Measures.</strong> Emergency procedures, protective equipment, and methods for containment and cleanup (e.g., "Use non-sparking tools").
                        <br><strong>Section 7: Handling and Storage.</strong> Precautions for safe handling (e.g., "Use only outdoors or in a well-ventilated area") and conditions for safe storage, including incompatibilities.
                        <br><strong>Section 8: Exposure Controls/Personal Protection.</strong> *Critical.* Lists OSHA Permissible Exposure Limits (PELs) and ACGIH Threshold Limit Values (TLVs). Specifies the exact type of PPE required (e.g., "Wear nitrile gloves," "Use N95 respirator").</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Section 4 (First Aid) and Section 8 (PPE) are the most frequently consulted sections during daily work.</li><li>Section 5 tells you if water will make a chemical fire worse (e.g., with certain metals or oils).</li></ul></div>"""
                },
                {
                    'order': 5,
                    'title': 'Module 5: Safety Data Sheets (SDS): Sections 9-16',
                    'content': """
                        <p>The second half of the SDS provides the technical data needed by safety professionals and engineers.
                        <br><strong>Section 9: Physical and Chemical Properties.</strong> Appearance, odor, pH, flash point, vapor pressure, and relative density. (e.g., Is it heavier than air? If so, vapors will sink to the floor).
                        <br><strong>Section 10: Stability and Reactivity.</strong> Describes chemical stability and the possibility of hazardous reactions. *Crucial for storage.* It lists "Incompatible Materials" (e.g., "Reacts violently with water").
                        <br><strong>Section 11: Toxicological Information.</strong> Routes of exposure, symptoms (acute and chronic), and numerical measures of toxicity (LD50/LC50). Lists if the chemical is a known carcinogen (NTP, IARC, OSHA).
                        <br><strong>Section 12: Ecological Information.</strong> Ecotoxicity (fish/invertebrates), persistence, and degradability. (Non-mandatory for OSHA).
                        <br><strong>Section 13: Disposal Considerations.</strong> Description of waste residues and safe handling methods. (Non-mandatory for OSHA but critical for EPA compliance).
                        <br><strong>Section 14: Transport Information.</strong> UN number and proper shipping name for DOT/IATA/IMDG. (Non-mandatory for OSHA).
                        <br><strong>Section 15: Regulatory Information.</strong> Safety, health, and environmental regulations specific to the product (e.g., TSCA, SARA Title III).
                        <br><strong>Section 16: Other Information.</strong> Date of preparation or last revision. Always check this to ensure you have the most current version.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Section 10 (Stability) prevents accidents by telling you what NOT to mix the chemical with.</li><li>Section 11 (Toxicology) lists the LD50 and cancer risks associated with the substance.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Labeling Requirements: Primary vs. Workplace Containers',
                    'content': """
                        <p>The GHS requires strict labeling for containers. 
                        <br><strong>Primary Containers:</strong> These are the containers shipped from the manufacturer (drums, pails, bottles). They <em>must</em> have the full GHS label: Product Identifier, Signal Word, Hazard Statements, Pictograms, Precautionary Statements, and Supplier Information. You may <em>never</em> deface or remove a primary label unless the container is empty and cleaned.
                        <br><strong>Workplace (Secondary) Containers:</strong> These are portable containers (spray bottles, jugs) into which chemicals are transferred. They <em>must</em> be labeled with at least the Product Identifier and Words, Pictures, or Symbols that convey the general hazards.
                        <br><strong>The "Immediate Use" Exemption:</strong> A secondary container does NOT need a label <em>if and only if</em>:
                        <br>1. The chemical is transferred from a labeled container.
                        <br>2. It is for the <em>immediate</em> use of the employee who performed the transfer.
                        <br>3. It is used entirely within that specific work shift.
                        <br>If you leave the container unattended, take a break, or hand it to another worker, it <strong>MUST</strong> be labeled immediately. Unlabeled "mystery fluids" are a top 2026 OSHA citation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Primary labels must never be defaced or removed.</li><li>Secondary containers must be labeled unless used immediately and entirely by the transferor in one shift.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Health Hazards: Toxicity, Sensitizers, and Carcinogens',
                    'content': """
                        <p>Health hazards are classified based on their interaction with the human body.
                        <br><strong>Acute Toxicity:</strong> Adverse effects occurring following oral or dermal administration of a single dose, or multiple doses given within 24 hours, or an inhalation exposure of 4 hours.
                        <br><strong>Skin Corrosion vs. Irritation:</strong> Corrosion is irreversible damage (visible necrosis) to the skin. Irritation is reversible damage.
                        <br><strong>Respiratory or Skin Sensitization:</strong> A <strong>Sensitizer</strong> is a chemical that causes a substantial proportion of exposed people or animals to develop an allergic reaction in normal tissue after repeated exposure to the chemical. Once sensitized, even minute exposure can trigger a fatal anaphylactic reaction (e.g., Isocyanates in paint).
                        <br><strong>Carcinogenicity:</strong> Ability to cause cancer. (Category 1A: Known human carcinogen; 1B: Presumed; 2: Suspected).
                        <br><strong>Germ Cell Mutagenicity:</strong> Ability to cause genetic mutations in reproductive cells.
                        <br><strong>Reproductive Toxicity:</strong> Adverse effects on sexual function and fertility in adult males and females, or on development of the offspring (Teratogens).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Sensitizers cause allergic reactions that worsen with repeated exposure, potentially leading to anaphylaxis.</li><li>Carcinogens (Cancer) and Mutagens (DNA damage) are chronic hazards often marked by the "Health Hazard" star.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Physical Hazards: Flammables, Pyrophorics, and Oxidizers',
                    'content': """
                        <p>Physical hazards are properties of the chemical that can cause it to be physically dangerous.
                        <br><strong>Flammable Liquids:</strong> Classified by Flash Point (the lowest temperature at which vapors can ignite). Category 1 flammables (Flash Point < 73.4°F) are extremely dangerous at room temperature.
                        <br><strong>Pyrophoric Liquids/Solids:</strong> Substances that, even in small quantities, ignite within five minutes of coming into contact with air. These require specialized handling under inert gas (Nitrogen/Argon).
                        <br><strong>Self-Heating Substances:</strong> Substances that react with air and generate heat without an energy supply. Unlike pyrophorics, they require large amounts (kilograms) and long periods of time to ignite.
                        <br><strong>Oxidizers:</strong> Liquids or solids that readily yield oxygen or other oxidizing substances to stimulate the combustion of other matter. *Never store Oxidizers with Flammables.* The oxidizer will feed the fire, making it burn violently and resisting standard extinguishing methods.
                        <br><strong>Corrosive to Metals:</strong> A substance which by chemical action will materially damage, or even destroy, metals. These must be stored in specialized plastic or glass containers.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Flash Point determines the flammability category; lower flash point = higher danger.</li><li>Oxidizers provide oxygen to fires; never store them near flammables or combustibles.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: PPE Selection: Permeation, Penetration, and Degradation',
                    'content': """
                        <p>Selecting the right Personal Protective Equipment (PPE) is a science, not a guess. In 2026, you must understand three concepts:
                        <br><strong>1. Degradation:</strong> The physical changes to the material caused by the chemical (swelling, stiffening, breaking down).
                        <br><strong>2. Penetration:</strong> The movement of a chemical through zippers, seams, or pinholes in the material.
                        <br><strong>3. Permeation:</strong> The process by which a chemical dissolves in or moves through a material on a molecular level. A glove may look intact, but the chemical could be permeating through it to your skin.
                        <br>You must consult the <strong>Manufacturer's Compatibility Chart</strong> or Section 8 of the SDS. For example, Acetone will eat through a Latex glove in seconds; you need Butyl rubber. Nitrile is good for oils but poor for strong oxidizers. "One glove fits all" is a myth that leads to chemical burns.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Permeation allows chemicals to pass through intact gloves on a molecular level.</li><li>Always check the chemical compatibility chart; Latex, Nitrile, and Butyl rubber all have different strengths.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Spill Response: The "SSS" and "Dike" Protocols',
                    'content': """
                        <p>When a spill occurs, the first decision is: <strong>Incidental vs. Emergency.</strong> An incidental spill is one that can be safely cleaned up by employees in the immediate area. An emergency spill involves high toxicity, fire risk, or lack of knowledge—this requires evacuation and the HazMat team.
                        <br><strong>The "SSS" Protocol:</strong>
                        <br><strong>1. Safety:</strong> Assess the risk. Don PPE. Evacuate if necessary.
                        <br><strong>2. Stop:</strong> Stop the source (close the valve, upright the bottle) <em>if safe to do so</em>.
                        <br><strong>3. Secure:</strong> Secure the area with tape or signage.
                        <br><strong>Containment Strategy:</strong> Use the <strong>"Diking"</strong> method. Place absorbent socks or snakes <em>around</em> the perimeter of the spill first to stop it from spreading to drains or walkways. Then, work from the outside in with absorbent pads.
                        <br><strong>Neutralization:</strong> For acids, use a base (sodium bicarbonate). For bases, use a weak acid (citric acid). *Never* simply wipe up a strong corrosive without neutralizing it first, as the rag becomes hazardous waste.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Determine if a spill is "Incidental" or "Emergency" before acting.</li><li>Use the "Diking" method (surround then absorb) to prevent spread to drains.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Chemical Storage: Segregation and Incompatibility',
                    'content': """
                        <p>Improper storage is a leading cause of facility fires and toxic gas releases. The Golden Rule of 2026: <strong>Segregate by Hazard Class, not Alphabetically.</strong>
                        <br><strong>The Segregation Matrix:</strong>
                        <br>- <strong>Acids</strong> must be separated from <strong>Bases</strong>. (Mixing creates heat and violent splattering).
                        <br>- <strong>Oxidizers</strong> must be separated from <strong>Flammables/Combustibles</strong>. (Mixing creates explosion risk).
                        <br>- <strong>Water-Reactives</strong> must be stored in dry, watertight cabinets.
                        <br><strong>Secondary Containment:</strong> Liquids should be stored in secondary trays capable of holding 110% of the volume of the largest container.
                        <br><strong>Ventilation:</strong> Flammables must be stored in rated "Flammable Safety Cabinets" (yellow) that are grounded. Corrosives should be stored in "Acid Cabinets" (blue/plastic) that resist corrosion. Never store chemicals above eye level or in fume hoods (which disrupts airflow).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Segregate chemicals by Hazard Class (e.g., Oxidizers away from Flammables), never alphabetically.</li><li>Use secondary containment trays to catch leaks and prevent incompatible mixing.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Training, Contractors, and the 2026 Digital Era',
                    'content': """
                        <p>Training is the backbone of HazCom. Employers must provide training:
                        <br>1. At the time of initial assignment.
                        <br>2. Whenever a <strong>new chemical hazard</strong> is introduced into the work area.
                        <br><strong>Multi-Employer Worksites:</strong> In 2026, the "Host Employer" is responsible for informing contractors of the hazards they may encounter. Conversely, contractors must inform the host employer of any hazardous chemicals they are bringing onto the site (e.g., solvents, welding gases).
                        <br><strong>Digital Access:</strong> While SDS binders are traditional, OSHA allows electronic access (tablets, QR codes) provided there is a backup system (battery backup, paper copies) in case of power failure. The system must be barrier-free; asking a supervisor for the password to the SDS computer is a violation. Access must be immediate and direct. By mastering GHS, you ensure that you are never "blind" to the invisible dangers of the chemical world.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Training is required upon hiring and whenever a new hazard (not just a new product) is introduced.</li><li>Contractors and Host Employers must exchange hazard information before work begins.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Hazard Communication (GHS) Upgraded to PLATINUM Standard.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
