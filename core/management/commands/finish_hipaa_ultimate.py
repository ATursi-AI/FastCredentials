from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes HIPAA with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='HIPAA Patient Confidentiality')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Reproductive Health Privacy: The 2026 Mandate',
                    'content': """
                        <p>In 2026, one of the most significant HIPAA updates involves the <strong>Reproductive Health Privacy Rule</strong>. This rule prohibits covered entities and their business associates from using or disclosing Protected Health Information (PHI) for the purpose of investigating or prosecuting patients or providers for seeking, obtaining, or providing lawful reproductive healthcare. This includes abortion services, contraception, and fertility treatments. Even in the face of a state-level subpoena, HIPAA now provides a <strong>Federal Privacy Shield</strong> that takes precedence over state investigations into lawful medical care.</p>
                        <p>For healthcare professionals, this creates a new "Attestation" requirement. Before disclosing any PHI that could potentially involve reproductive health to law enforcement or administrative bodies, the requester must provide a signed, legally binding document stating that the request is not for a prohibited purpose. If you work in a state with conflicting laws, you must follow the federal HIPAA standard: <strong>Do not disclose reproductive health data for legal pursuit.</strong> Failure to follow this 2026 mandate can result in criminal penalties for the provider and a complete loss of patient trust.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HIPAA now prohibits sharing PHI for the investigation of lawful reproductive healthcare.</li><li>A signed Attestation is required before sharing sensitive data with law enforcement.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Business Associate Agreements (BAAs) in 2026',
                    'content': """
                        <p>A <strong>Business Associate (BA)</strong> is any person or entity that performs a service for a covered entity that involves the use or disclosure of PHI. This includes cloud storage providers, billing companies, IT consultants, and even AI-transcription services. In 2026, the <strong>"Chain of Liability"</strong> is strictly enforced. You must have a signed Business Associate Agreement (BAA) in place before any PHI is shared. A BAA is a legal contract that binds the vendor to the same high security and privacy standards as the healthcare provider itself.</p>
                        <p>In 2026, BAs are directly liable for their own HIPAA violations. If a third-party billing company experiences a breach, they are legally responsible for the fines. However, the covered entity can still be penalized if they failed to perform <strong>Due Diligence</strong> on the vendor. This means you must verify that your BAs are using Multi-Factor Authentication (MFA) and NIST-standard encryption. Simply "having a BAA" is no longer enough; you must ensure your vendors are actively compliant. If a BA refuses to sign an updated 2026 BAA, you must terminate the relationship to protect your organization's "Safe Harbor" status.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A BAA is mandatory for any vendor that handles, stores, or transmits PHI.</li><li>Business Associates are now directly liable to the federal government for breaches.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: The Breach Notification Rule: 2026 Timelines',
                    'content': """
                        <p>A breach is defined as the "unauthorized acquisition, access, use, or disclosure of PHI" which compromises the security or privacy of the information. In 2026, the timeline for action has accelerated. While the OCR still requires notification "without unreasonable delay" and no later than 60 days for major breaches, most world-class 2026 <strong>Internal Sanction Policies</strong> mandate a <strong>24-Hour Reporting Window</strong>. As soon as you suspect a breach—such as a lost laptop, a misdirected email containing PHI, or a ransomware alert—you must notify your Privacy Officer immediately.</p>
                        <p>For breaches affecting 500 or more individuals, the organization must notify the HHS, the affected patients, and the <strong>Media</strong> in the jurisdiction. For smaller breaches (under 500), the log must be submitted to HHS annually. In 2026, the <strong>"Burden of Proof"</strong> is on the organization. You must prove that a breach did *not* occur through a 4-factor risk assessment: 1. The nature and extent of the PHI. 2. The unauthorized person who used it. 3. Whether the PHI was actually viewed. 4. The extent to which the risk was mitigated. If you cannot prove the risk is low, you must treat it as a reportable breach.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Report any suspected breach internally within 24 hours.</li><li>Breaches affecting 500+ people require notification of the media and the HHS.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Patient Access Fees and 2026 Transparency',
                    'content': """
                        <p>Providing patients with access to their own records is a core HIPAA right. In 2026, the <strong>"Information Blocking"</strong> prohibition is strictly enforced. Providers cannot charge "unreasonable" fees that act as a barrier to a patient getting their data. For electronic records (ePHI), the 2026 standard is <strong>Zero Fee</strong> for data that is already stored in a digital portal. If a patient requests a digital copy via email or USB, you may only charge a "Reasonable Cost-Based Fee" that covers the labor for copying and the cost of the media (USB drive).</p>
                        <p>You are strictly prohibited from charging for the time spent "searching" or "retrieving" the records. Furthermore, you cannot require a patient to "come in person" to sign a request if they can provide a secure digital signature. In 2026, <strong>Digital Portals</strong> are the primary method for patient access. Patients must be able to download their data in a "machine-readable format" (like XML or JSON) to facilitate care coordination with other doctors. Transparency in fee structures must be clearly outlined in your updated Notice of Privacy Practices (NPP).</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Digital records should generally be provided to patients for free or a low cost-based fee.</li><li>Charging for "retrieval time" is a violation of the 2026 Information Blocking rules.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Disclosures for Law Enforcement: Subpoenas vs. Warrants',
                    'content': """
                        <p>Interacting with law enforcement requires a high level of HIPAA precision. In 2026, you cannot simply "hand over" a chart because an officer asks for it. To disclose PHI to law enforcement without patient consent, you must have a <strong>Valid Legal Order</strong>. A standard Subpoena signed by an attorney is often <strong>NOT enough</strong> to release PHI unless it is accompanied by a court order or an "Attestation" that the patient has been notified and given time to object. A Search Warrant or a Court Order signed by a judge, however, is a mandatory disclosure.</p>
                        <p>There are limited exceptions: 1. To identify or locate a suspect, fugitive, or missing person (limited to basic demographic data only). 2. If the patient is a victim of a crime and is unable to consent due to an emergency. 3. To report a death that may have resulted from criminal conduct. In 2026, every disclosure to law enforcement must be <strong>Tracked in the Accounting of Disclosures</strong>. Patients have a legal right to request a list of everyone who has seen their PHI for purposes other than treatment, payment, or healthcare operations (TPO) over the last six years.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Always verify a legal order (Warrant or Court Order) before sharing PHI with police.</li><li>Disclosures to law enforcement must be recorded in the patient\'s "Accounting of Disclosures."</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Sanction Policies and Internal "Snooping"',
                    'content': """
                        <p>One of the most frequent HIPAA violations in 2026 is <strong>Internal Snooping</strong>—employees accessing the records of celebrities, coworkers, family members, or "high-profile" patients out of curiosity. In 2026, Electronic Health Records (EHR) utilize <strong>AI-Audit Trails</strong> that flag any access that falls outside of an employee's normal job duties. For example, if a billing clerk views the clinical notes of a neighbor, the system will trigger an automatic alert. "Curiosity" is never a valid reason for accessing PHI and is a direct violation of the Privacy Rule.</p>
                        <p>Every 2026 covered entity must have a written <strong>Sanction Policy</strong> that outlines the consequences for privacy violations. These range from mandatory re-training for minor accidents to <strong>Immediate Termination</strong> and a report to the licensing board for intentional snooping or "Selling PHI." Under the HITECH Act, individuals can also be held personally liable and face criminal charges, including jail time, for knowingly obtaining or disclosing PHI for malicious reasons. HIPAA compliance is an individual professional responsibility; "I was just checking on a friend" is a career-ending admission.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>AI-Audit Trails now monitor for any "Snooping" outside of your job duties.</li><li>Intentional privacy violations can lead to personal criminal charges and termination.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Disposal of PHI: The NIST Standard',
                    'content': """
                        <p>PHI must be protected until the moment of its final destruction. In 2026, "throwing it in the trash" is a Tier 3 violation. Paper records must be <strong>Shredded, Burned, or Pulped</strong> so that the PHI is unreadable and cannot be reconstructed. Cross-cut shredding is the minimum 2026 standard. For electronic media (ePHI), the 2026 <strong>NIST 800-88 Standard</strong> for Media Sanitization must be followed. Simply "deleting" a file or "formatting" a hard drive is not enough; the data must be "Wiped" using specialized software or the drive must be physically destroyed through "De-gaussing" or shredding.</p>
                        <p>This rule applies to all devices: photocopiers, scanners, and fax machines often have internal hard drives that store every document they have ever processed. Before retiring or returning a leased office machine, the hard drive must be professionally sanitized. For remote workers, the 2026 standard requires a <strong>Locked Shred-Bin</strong> at the home office. You are prohibited from disposing of any work-related papers in your residential recycling or trash. By ensuring a "Secure Lifecycle" for data, you prevent the "Dumpster Diving" breaches that continue to haunt healthcare organizations in 2026.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Paper PHI must be shredded or burned; it can never be thrown in regular trash.</li><li>Electronic devices (copiers/hard drives) must be professionally wiped before disposal.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The 2026 Culture of Privacy',
                    'content': """
                        <p>The final module focuses on the transition from "knowing the rules" to <strong>"Living the Standard."</strong> A 2026 culture of privacy means that patient dignity is the primary filter for every action. This involves "The Elevator Rule": never discuss patient cases in public areas, even if you don\'t use the patient\'s name. It means being a "Privacy Advocate"—speaking up if you see a coworker leave a laptop unlocked or if a PHI-containing document is left on a printer. In 2026, privacy is not a "hurdle" to patient care; it is a <strong>Component of Patient Care</strong>.</p>
                        <p>We conclude with <strong>Personal Professionalism</strong>. By maintaining your HIPAA certification, you are proving to your patients, your employer, and the federal government that you are a competent guardian of human dignity. In an era of AI and global data networks, the promise of "Doctor-Patient Confidentiality" is more fragile than ever. Your commitment to the 15-day access rule, the 2026 encryption mandates, and the "Minimum Necessary" principle is what keeps the healthcare system trustworthy. Stay vigilant, stay secure, and stay professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Privacy is a core component of patient care and professional dignity.</li><li>Vigilance includes speaking up when you see others compromising security.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: HIPAA 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
