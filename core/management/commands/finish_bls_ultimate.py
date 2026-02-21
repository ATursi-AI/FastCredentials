from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Healthcare BLS with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Healthcare BLS (Basic Life Support)')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: AED and Manual Defibrillation Physics',
                    'content': """
                        <p>Defibrillation is the only effective treatment for Ventricular Fibrillation (VF) and Pulseless Ventricular Tachycardia (pVT). In 2026, healthcare providers use <strong>Biphasic Defibrillators</strong>, which deliver current in two directions, requiring lower energy levels and causing less myocardial damage than older monophasic units. The goal of the shock is not to "jump-start" the heart, but to provide <strong>Asystole (a total stop)</strong>, allowing the heart's natural pacemaker (the SA node) to resume a coordinated rhythm. If the AED or monitor identifies a "Non-Shockable" rhythm (Asystole or PEA), you must immediately resume compressions; never delay for a pulse check after a shock is delivered.</p>
                        
                        <p>Safety during defibrillation is paramount. In the oxygen-rich environment of a hospital, an electrical arc can trigger a <strong>Surgical Fire</strong>. You must ensure that the oxygen source is moved at least 3 feet away from the patient's chest before discharging the shock. Additionally, the 2026 standard for pad placement is the <strong>Anterolateral (AL)</strong> position, but <strong>Anteroposterior (AP)</strong> is preferred for patients with pacemakers or implanted defibrillators to avoid direct current flow through the device. "Clearing the Patient" must be a verbal and visual confirmation: look from the head to the toes of the patient to ensure no one is in contact with the bed or the patient before pushing the shock button.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Defibrillation stuns the heart to allow the SA node to take back control.</li><li>Clear the patient visually and move oxygen sources before discharging a shock.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Pediatric BLS: Clinical Ratios',
                    'content': """
                        <p>Pediatric cardiac arrest is rarely cardiac in origin; it is typically a <strong>Respiratory Failure</strong> event. Therefore, ventilations are even more critical in children (age 1 to puberty) than in adults. For a <strong>Single Rescuer</strong>, the ratio remains 30:2. However, for <strong>2-Rescuer Healthcare BLS</strong>, the ratio shifts to <strong>15:2</strong>. This higher frequency of ventilation (10-12 breaths per minute) addresses the primary metabolic need of the pediatric patient. Compressions should be at a depth of about 2 inches (one-third the chest depth) and should be performed with one or two hands depending on the size of the child.</p>
                        <p>Pulse checks in children are performed at the <strong>Carotid or Femoral artery</strong>. In 2026, the clinical threshold for starting CPR in a pediatric patient is a heart rate <strong>below 60 bpm</strong> with signs of poor perfusion (pallor, cyanosis, or altered mental status), even if a pulse is palpable. This is because a heart rate of 60 is insufficient to maintain the cardiac output required for a child's metabolism. If the patient is not breathing but has a pulse > 60, provide rescue breaths every 2-3 seconds. The focus is on preventing the "Bradycardic Slide" into full arrest through aggressive oxygenation and high-quality compressions.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>2-Rescuer Pediatric ratio is 15:2 to prioritize oxygenation.</li><li>Start CPR if the heart rate is below 60 bpm with signs of poor perfusion.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Neonatal Resuscitation: The 3:1 Ratio',
                    'content': """
                        <p>Resuscitation of the newborn (neonate) follows a highly specialized algorithm distinct from standard pediatric BLS. In 2026, the <strong>Neonatal Resuscitation Program (NRP)</strong> standard for chest compressions is a <strong>3:1 Ratio</strong> (3 compressions to 1 breath). This ensures a rate of approximately 90 compressions and 30 breaths per minute, totaling 120 events per minute. Compressions are performed using the <strong>Two-Thumb Encircling Hands Technique</strong>, which is superior for generating peak systolic and coronary perfusion pressure in the neonate. Depth should be one-third of the AP diameter of the chest.</p>
                        
                        <p>Temperature control is the second pillar of neonatal survival. Newborns lose heat rapidly, which increases oxygen consumption and leads to metabolic acidosis. Resuscitation should occur under a pre-heated <strong>Radiant Warmer</strong>. For the healthcare provider, the assessment follows the "Initial Steps": Dry, Stimulate, and Position the Airway. If the heart rate is below 100 bpm or the infant is gasping, begin Positive Pressure Ventilation (PPV). If the heart rate remains <strong>below 60 bpm</strong> after 30 seconds of effective PPV, begin chest compressions. The neonatal algorithm is a race against hypoxia and hypothermia.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Neonatal ratio is 3:1 (90 compressions/30 breaths per minute).</li><li>The Two-Thumb Encircling Hands technique is the preferred compression method.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Opioid-Associated Clinical Emergencies',
                    'content': """
                        <p>In 2026, the opioid epidemic has necessitated the inclusion of <strong>Naloxone (Narcan)</strong> in the BLS clinical algorithm. An opioid overdose causes death through profound respiratory depression. If a patient is found unresponsive with "Pinpoint Pupils" and is not breathing (or only gasping), you must first <strong>Start High-Quality CPR</strong>. While Naloxone is a life-saving reversal agent, it does not replace the need for oxygenation and circulation. The healthcare provider should administer Naloxone (intranasally or intramuscularly) as soon as it is available, but never at the expense of delaying compressions or breaths.</p>
                        <p>You must be prepared for the <strong>"Naloxone Surge."</strong> When the opioid receptors are cleared, the patient may wake up in acute withdrawal, which can manifest as agitation, vomiting, or aggressive behavior. Furthermore, many 2026 synthetic opioids (like Fentanyl analogues) have a longer half-life than Naloxone. This means the patient may "re-overdose" 30-60 minutes after the first dose of Naloxone wears off. Continuous clinical monitoring and supplemental oxygen are mandatory until the patient is fully stabilized. Your role as a BLS provider is to maintain life-support until the chemical reversal takes full effect.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Administer Naloxone for suspected overdose but do not delay CPR.</li><li>Monitor for "re-overdose" as Naloxone may wear off before the opioids leave the system.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Choking (FBAO) Clinical Algorithms',
                    'content': """
                        <p>Foreign Body Airway Obstruction (FBAO) in the clinical setting requires immediate recognition of the "Universal Choking Sign." For a conscious adult or child with a <strong>Severe Obstruction</strong> (unable to cough, speak, or breathe), perform <strong>Abdominal Thrusts (Heimlich Maneuver)</strong> until the object is expelled or the patient becomes unconscious. For infants, the 2026 standard remains the <strong>5 Back Slaps and 5 Chest Thrusts</strong> sequence. Never perform a "Blind Finger Sweep," as this can push the object deeper into the airway, causing a total obstruction.</p>
                        <p>If the patient becomes <strong>Unconscious</strong>, you must transition immediately to the BLS algorithm: 1. Lower them gently to the floor. 2. Activate the Emergency Response System. 3. <strong>Begin Chest Compressions</strong> (do not check for a pulse). The pressure from chest compressions is often more effective than abdominal thrusts at dislodging a deep obstruction. Every time you open the airway to give breaths, look inside the mouth. If you see the object and it is easily reachable, remove it. If not, continue CPR. Once the object is removed, you must still assess the patient for internal injuries caused by the thrusts or the obstruction itself.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Transition to CPR immediately if a choking victim becomes unconscious.</li><li>Look for the object during the ventilation phase of CPR; no blind finger sweeps.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Maternal Resuscitation: LUD Technique',
                    'content': """
                        <p>Resuscitating a pregnant patient (typically > 20 weeks gestation) introduces the complication of <strong>Aortocaval Compression</strong>. The weight of the gravid uterus can compress the mother's inferior vena cava and aorta when she is supine, reducing cardiac output by up to 30%. In 2026, the mandatory BLS modification is <strong>Continuous Lateral Uterine Displacement (LUD)</strong>. One rescuer should use one or two hands to physically push the uterus to the patient's left side while compressions are performed. This "manual shift" restores venous return to the heart, making CPR effective.</p>
                        
                        <p>If ROSC is not achieved within 5 minutes of arrest, the 2026 clinical standard moves toward <strong>Perimortem Cesarean Delivery (PMCD)</strong> to save both the mother and the infant. As a BLS provider, your duty is to maintain "High-Quality Compressions" during the surgical procedure. You must not stop CPR while the team is performing the PMCD. The relief of aortocaval compression after the delivery of the infant often results in immediate ROSC for the mother. In 2026, we emphasize that the best way to save the fetus is to save the mother through aggressive, modified BLS.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Perform Manual Lateral Uterine Displacement (LUD) to the left to restore venous return.</li><li>Do not stop CPR during a Perimortem Cesarean Delivery (PMCD).</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Special Circumstances: Drowning and Electrocution',
                    'content': """
                        <p>Drowning and Electrocution require specific modifications to the BLS sequence. For <strong>Drowning</strong>, the primary cause of arrest is profound hypoxia. In 2026, the standard for drowning is to <strong>Provide 5 Initial Rescue Breaths</strong> before starting compressions. This "Oxygen First" approach addresses the immediate metabolic deficit. If you are a lone rescuer, perform 2 minutes of CPR before leaving the patient to activate the emergency response system. Do not attempt to "drain water" from the lungs; most drowning victims only have a small amount of water in the lungs, and the "foaming" seen at the mouth is a surfactant reaction that should be cleared only enough to allow ventilation.</p>
                        <p>For <strong>Electrocution</strong>, the current often causes prolonged muscle tetany and respiratory paralysis. The patient may remain in respiratory arrest long after the cardiac rhythm has stabilized. Additionally, the risk of <strong>Spinal Injury</strong> is high if the patient was thrown by the current. Use the Jaw-Thrust maneuver for airway management. In 2026, we also monitor for "Delayed Arrhythmias." An electrocution victim who appears stable can suddenly drop into VF hours later. BLS providers must ensure these patients are transported for continuous ECG monitoring, regardless of their initial appearance.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Drowning: Give 5 rescue breaths before starting compressions.</li><li>Electrocution: Use Jaw-Thrust for airway and transport for delayed heart risks.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The Ethics of 2026 Resuscitation',
                    'content': """
                        <p>The final module addresses the 2026 ethical landscape of <strong>DNR (Do Not Resuscitate)</strong> and <strong>DNI (Do Not Intubate)</strong> orders. In a clinical setting, you must respect a valid, signed DNR/POLST form. If you are in the middle of a resuscitation and a valid DNR is produced, you must <strong>Stop Immediately</strong>. There is no legal or ethical obligation to continue once a patient's wish to avoid resuscitation is verified. However, in the absence of a document, "Presumed Consent" applies: you must provide full, aggressive BLS until a physician directs you to stop.</p>
                        <p>We conclude with <strong>Termination of Resuscitation (TOR)</strong>. In 2026, the criteria for stopping a code in the field or the facility include: 1. Arrest was not witnessed by EMS/Clinical staff. 2. No ROSC after 20-30 minutes of high-quality CPR. 3. No shocks were delivered. As a BLS professional, you are also responsible for <strong>Family Presence during Resuscitation (FPDR)</strong>. Research in 2026 shows that allowing family to witness the resuscitation efforts helps with the grieving process and confirms that "everything was done." By maintaining your professionalism and empathy during these final moments, you uphold the highest standards of the healthcare vocation.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Respect valid DNR/POLST orders immediately upon verification.</li><li>FPDR (Family Presence) is a 2026 best practice for clinical empathy and closure.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Healthcare BLS 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
