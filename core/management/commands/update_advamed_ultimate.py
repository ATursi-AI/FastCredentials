from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades AdvaMed Code of Ethics to 10 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='AdvaMed Code of Ethics')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 AdvaMed Framework and "Medical Technology"',
                    'content': """
                        <p>The AdvaMed Code of Ethics is the voluntary but industry-standard framework governing the interactions between Medical Technology companies and Healthcare Professionals (HCPs). In 2026, the definition of "Medical Technology" has expanded to include not only hardware (implants, instruments) but also <strong>Digital Health Software</strong> and AI-driven diagnostic tools. The core philosophy remains <strong>Patient-Centricity</strong>: all interactions must ensure that medical decisions are made based on the best interests of the patient, free from the undue influence of improper financial incentives or "quid pro quo" arrangements.</p>
                        <p>The 2026 Code emphasizes that companies are responsible for the actions of their "Channel Partners" (distributors and agents). You can no longer outsource unethical behavior; if a third-party distributor provides an improper kickback to a surgeon to use your device, the parent company is legally and ethically liable. The 2026 standard requires <strong>Continuous Compliance Monitoring</strong>. This module establishes the four cornerstones of the Code: 1. Integrity. 2. Respect. 3. Responsibility. 4. Transparency. As a professional, you are the guardian of this code; your adherence ensures that the medical technology industry remains a trusted partner in the healthcare ecosystem.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Code covers everything from surgical robots to AI diagnostic software.</li><li>Companies are legally responsible for the ethical conduct of their third-party distributors.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: HCP Consultations and Fair Market Value (FMV)',
                    'content': """
                        <p>Medical technology companies often need the expertise of Healthcare Professionals (HCPs) for R&D, product testing, and training. In 2026, these <strong>Consulting Arrangements</strong> are strictly regulated to ensure they are not "disguised kickbacks." To be compliant, a consulting agreement must fulfill three criteria: 1. There must be a <strong>Legitimate Need</strong> for the service identified in advance. 2. The consultant must be selected based on their expertise, not their sales volume. 3. Compensation must be at <strong>Fair Market Value (FMV)</strong>. In 2026, FMV is calculated using localized, data-driven benchmarks for the specific specialty and experience level of the HCP.</p>
                        <p>You are strictly prohibited from paying an HCP for "passive attendance" at a meeting. Every dollar paid must correspond to a specific, documented "Work Product" (e.g., a written report or a training presentation). 2026 standards also require that the number of consultants engaged must be "reasonably necessary" to achieve the goal—hiring 50 surgeons to review one instrument design is a red flag for compliance. All consulting contracts must be in writing and signed before any services are rendered. By adhering to the FMV standard, you prove that the payment is for the HCP’s <em>knowledge</em>, not their <em>prescribing power</em>.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Consulting must meet a pre-identified "Legitimate Need."</li><li>Payments must be at Fair Market Value (FMV) and never tied to sales volume.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Educational Grants and Third-Party Events',
                    'content': """
                        <p>Companies may support medical education through <strong>Educational Grants</strong> to third-party organizations (like hospitals or professional societies). In 2026, the "Separation of Powers" is absolute. The sales and marketing team <strong>must not have any control</strong> over which HCPs receive support from these grants. The grant must be provided to the <em>institution</em>, never directly to the individual HCP. The institution is solely responsible for selecting the attendees and the content of the program. This ensures that the company’s support is for the advancement of science, not the recruitment of "Brand Ambassadors."</p>
                        <p>When a company provides a grant for a third-party conference, the 2026 Code prohibits the funding of "Social Events" or "Entertainment." You cannot provide a grant specifically to pay for a golf outing or a luxury dinner during the conference. Furthermore, the venue for the event must be "conducive to the exchange of information." In 2026, "Resort Locations" are heavily scrutinized; if a conference is held at a Five-Star Caribbean resort during peak season with minimal scientific sessions, it is considered a non-compliant event. Compliance requires that the educational content be the primary focus of the sponsorship, with no "perceived or actual" influence over the attendees\' future clinical decisions.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Educational grants must go to the institution, never directly to an HCP.</li><li>Sales and marketing teams cannot influence the selection of grant recipients.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Business Meals and Hospitality Limits',
                    'content': """
                        <p>Business meals are a common part of the industry, but in 2026, they are subject to <strong>Strict Monetary Caps</strong> and "Occasionality" rules. A compliant business meal must be: 1. Modest by local standards. 2. Subordinate in time and focus to the educational or business discussion. 3. Provided in a setting conducive to business (e.g., the HCP's office or a quiet restaurant). You are strictly prohibited from providing meals to an HCP's spouse, staff members who do not have a "bona fide" professional interest in the discussion, or as a "thank you" for a recent purchase.</p>
                        <p>The 2026 Code also addresses <strong>Alcohol Consumption</strong>. While not strictly prohibited, the provision of alcohol must be "incidental" and modest. An "open bar" or high-end wine tasting is considered a violation, as it shifts the focus from professional exchange to entertainment. Furthermore, 2026 data shows that "Frequent Flyers"—HCPs who receive meals multiple times a week from the same company—are a primary target for government audits. You must track the "Aggregate Spend" for every HCP to ensure your hospitality remains truly "occasional." If the meal feels like a "Gift" rather than a "Working Session," it is non-compliant.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Meals must be modest, occasional, and in a setting conducive to business.</li><li>Hospitality cannot be extended to spouses or non-professional staff.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: AdvaMed Code Part 1 Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
