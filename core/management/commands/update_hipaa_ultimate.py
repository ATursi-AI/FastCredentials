from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades HIPAA to 12 Deep-Dive 2026 World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='HIPAA Patient Confidentiality')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 HIPAA Regulatory Landscape',
                    'content': """
                        <p>The Health Insurance Portability and Accountability Act (HIPAA) of 1996 remains the bedrock of patient privacy, but in 2026, it has undergone its most significant modernization in a decade. The regulatory focus has shifted from "passive compliance" to <strong>Operational Accountability</strong>. As of February 16, 2026, the Department of Health and Human Services (HHS) requires all "Covered Entities" (healthcare providers, plans, and clearinghouses) to update their <strong>Notice of Privacy Practices (NPP)</strong>. This update is not merely administrative; it reflects new, stringent protections for sensitive health data and faster patient access timelines. Failure to have an updated NPP posted prominently by this date is a Tier 1 compliance violation.</p>
                        <p>The 2026 standard also introduces the <strong>15-Day Access Rule</strong>. Previously, providers had 30 days to respond to a patient\'s request for their medical records. That window has been cut in half. Patients now have a legal right to inspect their Protected Health Information (PHI) in person, take photographs of their records, and receive electronic copies within 15 calendar days. This change is designed to support patient autonomy and care coordination. As a professional, you must understand that "gatekeeping" or delaying access to PHI is now a primary target for Office for Civil Rights (OCR) enforcement actions and heavy financial penalties.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The February 16, 2026, deadline requires an updated Notice of Privacy Practices (NPP).</li><li>Providers now have only 15 days to fulfill a patient\'s request for medical records.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Defining PHI and the 18 Identifiers',
                    'content': """
                        <p><strong>Protected Health Information (PHI)</strong> is any information in a medical record that can be used to identify an individual and that was created, used, or disclosed in the course of providing a healthcare service. In 2026, the definition has expanded to include <strong>Biometric Data</strong> (facial recognition, iris scans, and fingerprints) and <strong>Digital Identifiers</strong> (IP addresses and device IDs used in telehealth). HIPAA protects PHI in all forms: verbal, paper, and electronic (ePHI). There are 18 specific identifiers that, when linked to health data, make it PHI, including names, geographic subdivisions smaller than a state, Social Security numbers, and full-face photographic images.</p>
                        
                        <p>Understanding the "Minimum Necessary" standard is critical for 2026 compliance. This rule states that when using or disclosing PHI, you must limit the information to only what is necessary to accomplish the intended purpose. For example, a billing clerk does not need to see a patient’s full clinical progress notes to process a claim; they only need the codes and dates of service. In 2026, "Data Minimization" is the primary technical defense against breaches. If you are handling data that has been "De-Identified" (all 18 identifiers removed), it is no longer considered PHI and is not subject to the HIPAA Privacy Rule. However, re-identifying that data through AI or other means is a serious criminal offense.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>PHI includes health data linked to any of 18 specific identifiers, including IP addresses.</li><li>The "Minimum Necessary" standard requires you to only access data required for your specific job.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: 42 CFR Part 2: Substance Use Disorder Privacy',
                    'content': """
                        <p>The February 2026 HIPAA updates focus heavily on the alignment of HIPAA with <strong>42 CFR Part 2</strong>, the federal regulation protecting the confidentiality of Substance Use Disorder (SUD) treatment records. Historically, SUD records had much stricter protections than standard PHI to prevent discrimination and prosecution of patients. In 2026, these rules have been harmonized to improve care coordination, but they still carry <strong>Stricter Consent Requirements</strong>. Your updated Notice of Privacy Practices (NPP) must explicitly state how SUD records are handled and that they cannot be used in legal proceedings against the patient without specific written consent or a court order.</p>
                        <p>For healthcare professionals, this means "redisclosure" of SUD records is now more strictly monitored. If you receive SUD records from a specialized treatment facility, you cannot simply pass them along to another provider without ensuring the patient\'s consent covers that specific transfer. The 2026 standard requires <strong>Segregated Data Handling</strong> in Electronic Health Records (EHR) for SUD notes. This ensures that a patient\'s history of addiction is not visible to every administrative staff member, but remains accessible to the clinical team for life-safety reasons (such as preventing lethal drug interactions). Understanding the "Part 2" nuances is the benchmark for high-level healthcare compliance in 2026.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>SUD records (Part 2) have heightened confidentiality to prevent legal discrimination.</li><li>SUD records cannot be used in court against a patient without a specific court order or consent.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: The 2026 Security Rule: Mandatory Encryption',
                    'content': """
                        <p>The 2026 <strong>HIPAA Security Rule Modernization</strong> has eliminated the longstanding "addressable" vs. "required" distinction. Previously, some smaller entities could opt-out of encryption if they had "alternative" safeguards. That is over. In 2026, <strong>Encryption is mandatory for all ePHI</strong> both "At Rest" (on servers, laptops, and USB drives) and "In Transit" (via email or messaging). If an unencrypted laptop is stolen, it is automatically a "Presumed Breach" under the 2026 standard, regardless of whether the data was actually accessed. Encryption is the "Safe Harbor" that protects the organization from penalties.</p>
                        <p>Telehealth security is the second pillar of the 2026 Security Rule. You must only use platforms that provide a <strong>Business Associate Agreement (BAA)</strong> and end-to-end encryption. Using public-facing apps like standard FaceTime or Skype for clinical consultations is now a high-risk violation. Furthermore, the 2026 standard requires <strong>Multi-Factor Authentication (MFA)</strong> for any system containing ePHI. "Password-only" access is considered a "Known Vulnerability." As a professional, you are responsible for securing your workspace: this includes "Lock-Before-Walk" protocols for workstations and ensuring that monitors are not visible to patients or the public in shared areas.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Encryption for all ePHI (at rest and in transit) is now a mandatory requirement.</li><li>Multi-Factor Authentication (MFA) is required for all systems that access patient data.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: HIPAA Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
