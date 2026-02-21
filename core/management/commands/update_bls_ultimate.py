from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Healthcare BLS to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Healthcare BLS (Basic Life Support)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Systems of Care',
                    'content': """
                        <p>In 2026, Basic Life Support (BLS) for healthcare providers is defined by the <strong>System of Care</strong> approach, which distinguishes between In-Facility Cardiac Arrest (IHCA) and Out-of-Hospital Cardiac Arrest (OHCA). For the clinical professional, the IHCA chain of survival emphasizes <strong>Early Surveillance and Prevention</strong>. Unlike the layperson who waits for collapse, the healthcare provider utilizes "Rapid Response Teams" (RRT) or "Medical Emergency Teams" (MET) at the first sign of clinical deterioration—such as acute changes in respiratory rate, oxygen saturation, or mental status. This proactive intervention is designed to prevent the cardiac arrest before it occurs.</p>
                        <p>The 2026 standard also incorporates <strong>Post-Cardiac Arrest Care</strong> as a critical link. Survival is no longer measured just by Return of Spontaneous Circulation (ROSC), but by "Neurologically Intact Survival." This requires the seamless transition from BLS (compressions and ventilation) to ALS (advanced airway and pharmacology) and finally to specialized cardiac catheterization labs or ICU care. As a BLS provider, you are the foundation of this system. If the "Foundation" (high-quality compressions) is weak, the most advanced drugs and machines in the world will fail to save the patient. This module establishes your role as a high-stakes clinical interventionist.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The IHCA Chain of Survival begins with early surveillance and Rapid Response Teams.</li><li>High-quality BLS is the mandatory foundation for all advanced life support (ALS).</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: High-Performance Team Dynamics',
                    'content': """
                        <p>Resuscitation in 2026 is a "Team Sport." High-performance teams utilize <strong>Closed-Loop Communication</strong> and <strong>Clear Roles</strong> to minimize "hands-off" time. During a code, the Team Leader assigns specific roles: Compressor, Ventilator/Airway, AED/Monitor/Defibrillator, Recorder, and IV/IO/Medications. Closed-loop communication requires the team member to verbally repeat the order back to the leader (e.g., "Assigning roles: I am the Compressor") and confirm when the task is complete. This prevents errors in a high-adrenaline environment where verbal orders can be easily missed or misunderstood.</p>
                        
                        <p>A critical 2026 team skill is <strong>Constructive Intervention</strong>. If a team member observes the compressor becoming fatigued or the ventilation rate becoming too high, they have a professional duty to speak up immediately but respectfully. We also utilize <strong>Knowledge Sharing</strong>: the Team Leader should periodically provide a "Global Re-evaluation" (e.g., "We have been in PEA for 4 minutes, two doses of Epinephrine given, checking H's and T's"). This keeps the entire team synchronized on the clinical path. By maintaining "Mutual Respect" and avoiding ego-driven conflict, the team ensures the patient receives the maximum "Chest Compression Fraction" (CCF) possible.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Closed-Loop Communication ensures orders are heard and executed correctly.</li><li>Constructive Intervention is the duty of every team member to ensure quality care.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: 2026 Compression Physics and Capnography',
                    'content': """
                        <p>High-quality chest compressions are the only way to maintain coronary and cerebral perfusion during arrest. In 2026, the metrics are precise: <strong>Rate of 100-120 per minute</strong> and <strong>Depth of at least 2 inches (5cm)</strong> but no more than 2.4 inches (6cm). You must allow for <strong>Complete Chest Recoil</strong> between every compression; "leaning" on the chest prevents the heart from refilling with blood, significantly reducing the efficacy of the next compression. For the healthcare provider, the goal is a <strong>Chest Compression Fraction (CCF) of at least 80%</strong>—meaning the patient is receiving compressions for at least 48 seconds out of every minute.</p>
                        
                        <p>The 2026 "Gold Standard" for monitoring compression quality is <strong>Quantitative Waveform Capnography (EtCO2)</strong>. During CPR, an EtCO2 reading of <strong>less than 10 mmHg</strong> indicates that compressions are not effective and must be improved. If EtCO2 suddenly jumps to 35-45 mmHg, it is often the first clinical indicator of ROSC (Return of Spontaneous Circulation), even before a pulse is palpable. Furthermore, 2026 standards discourage the routine "Pulse Check" during compressions. You only check for a pulse during the 10-second rhythm analysis window to minimize interruptions. If there is any doubt about the presence of a pulse, you must resume compressions immediately.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Maintain a rate of 100-120 bpm and allow for full chest recoil.</li><li>EtCO2 < 10 mmHg indicates poor quality CPR; a sudden jump indicates ROSC.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Advanced Airway and Ventilation Ratios',
                    'content': """
                        <p>In 2026, the approach to ventilation in BLS depends on whether an advanced airway (Endotracheal tube or Supraglottic airway) is in place. For standard <strong>Bag-Mask Ventilation (BMV)</strong>, the ratio remains 30:2 (30 compressions to 2 breaths). Each breath should be delivered over 1 second with just enough volume to see visible chest rise. The 2026 standard emphasizes the <strong>E-C Clamp Technique</strong> to ensure a tight seal. Over-ventilation (giving too many breaths or too much volume) is a critical error; it increases intrathoracic pressure, which decreases blood return to the heart and effectively "shuts off" the circulation you are trying to create.</p>
                        
                        <p>Once an <strong>Advanced Airway</strong> is placed, the compression-to-breath ratio is eliminated. In 2026, the compressor provides continuous compressions at 100-120 bpm without pausing, while the ventilator provides <strong>1 breath every 6 seconds</strong> (10 breaths per minute). This "Asynchronous CPR" is only performed when the airway is secured. For the clinical provider, monitoring the "Gastric Inflation" risk is paramount; if you see the stomach rising rather than the chest, you must re-position the head using the Head-Tilt/Chin-Lift or, if a spinal injury is suspected, the <strong>Jaw-Thrust Maneuver</strong>. Proper ventilation ensures oxygenation while maintaining the hemodynamic stability required for survival.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Standard BMV ratio is 30:2; breaths should be delivered over 1 second.</li><li>With an advanced airway, provide 1 breath every 6 seconds with continuous compressions.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Healthcare BLS Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
