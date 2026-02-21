from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes AdvaMed Code with Modules 5-10'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='AdvaMed Code of Ethics')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Charitable Donations and Independence',
                    'content': """
                        <p>Medical technology companies have a long history of supporting charitable causes, but in 2026, the <strong>Separation of Charity from Sales</strong> is a mandatory legal boundary. A charitable donation must be made for <em>bona fide</em> charitable purposes, such as supporting indigent care, community health education, or disaster relief. The donation must be made to a registered non-profit organization (501(c)(3) or equivalent) and never directly to an individual Healthcare Professional (HCP) or their private practice.</p>
                        <p>In 2026, the "Inducement Rule" is strictly monitored. You must never make a donation as a reward for a customer's past purchases or as an incentive for future business. If a surgeon asks you to donate to their favorite local charity in exchange for "opening the door" to a new product line, you must refuse. This is considered a "Quid Pro Quo" and a direct violation of the Anti-Kickback Statute. All donations must be reviewed and approved by the company's <strong>Compliance Department</strong>, not the sales team, to ensure there is no "actual or perceived" conflict of interest.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Donations must be for genuine charitable purposes and go to non-profit entities.</li><li>Sales teams must be excluded from the donation approval process to prevent "Quid Pro Quo."</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Educational Items, Gifts, and "No Trinkets"',
                    'content': """
                        <p>The 2026 AdvaMed Code is absolute regarding gifts: <strong>The provision of "Trinkets" and non-educational items is strictly prohibited.</strong> This includes pens, mugs, pads, high-end electronics, and even flowers. These items have no scientific value and are seen as "Gratuities" intended to build improper personal influence. You are also prohibited from providing items for the personal use of the HCP or their staff, such as gift cards, tickets to sporting events, or luxury items. In 2026, "Relationship Selling" must be based on the quality of the technology, not the quality of the gifts.</p>
                        <p>The only exception in 2026 is for <strong>Modest Educational Items</strong>. To be compliant, the item must have a fair market value of less than $100 and must be intended for the <em>benefit of the patient</em> or the <em>education of the HCP</em>. Examples include anatomical models, medical textbooks, or patient education brochures. These items cannot be given frequently—they must be "occasional." If an item can be used outside of a professional medical context (like a branded tablet or a high-end stethoscope), it is generally considered a non-compliant gift. The 2026 standard is: "If it doesn't help the patient, don't give it."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Gifts of any kind (pens, mugs, gift cards) are strictly prohibited.</li><li>Educational items must be under $100 and directly benefit the patient or HCP education.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Value-Based Care (VBC) and Compliant Risk-Sharing',
                    'content': """
                        <p>In 2026, the shift toward <strong>Value-Based Care (VBC)</strong> has introduced new "Safe Harbors" under the Anti-Kickback Statute. These allow medical technology companies to engage in "Risk-Sharing" arrangements with hospitals. In a VBC contract, the company may agree to provide a discount or a rebate if a product does not meet specific clinical outcomes (e.g., "Outcome-Based Pricing"). While these arrangements are encouraged to lower healthcare costs, they must be transparent, data-driven, and centered on <strong>Patient Outcomes</strong>, not just volume-based incentives.</p>
                        <p>To remain compliant in 2026, VBC arrangements must have <strong>Clearly Defined Benchmarks</strong>. You cannot simply offer a "rebate" based on how many units are sold. The contract must outline exactly how the "Value" is measured (e.g., reduced readmission rates or lower infection scores). Furthermore, the company must not offer these arrangements as an inducement to "Switch" from a competitor without a clinical justification. VBC is a technical, clinical partnership, not a marketing gimmick. Every VBC contract must be vetted by legal counsel to ensure it meets the 2026 OIG (Office of Inspector General) Safe Harbor requirements.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>VBC allows for "Risk-Sharing" based on clinical outcomes, not sales volume.</li><li>Contracts must have transparent, data-driven benchmarks to be legally compliant.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Evaluation and Demonstration Products',
                    'content': """
                        <p>Providing "Free" products for evaluation is a high-risk area for compliance. In 2026, the <strong>"Evaluation Period"</strong> must be limited to a "reasonable" time necessary for the HCP to assess the technology—typically no more than 30 to 90 days. For single-use disposables, the company should only provide the minimum quantity necessary for the assessment. For capital equipment (like surgical robots or monitors), there must be a <strong>Written Evaluation Agreement</strong> that specifies the equipment will be returned or purchased at the end of the trial period.</p>
                        <p>Allowing a hospital to keep an "Evaluation Unit" indefinitely without payment is considered a "Kickback." In 2026, companies must perform "Inventory Audits" to ensure that all demo units are accounted for. You are also prohibited from providing "Service Credits" or "Free Maintenance" as a gift; these must be part of a legitimate, Fair Market Value contract. The goal of an evaluation is to allow the HCP to make an <strong>Informed Clinical Choice</strong>, not to provide free inventory that lowers the customer’s overhead and creates an improper financial incentive to use the product.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Evaluation periods must be time-limited and documented in a written agreement.</li><li>Providing free equipment indefinitely is a violation of the Anti-Kickback Statute.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Transparency and the 2026 Sunshine Act',
                    'content': """
                        <p>The <strong>Open Payments (Sunshine Act)</strong> is a federal law that requires medical technology companies to report all "Transfers of Value" made to Healthcare Professionals and Teaching Hospitals. In 2026, this transparency has reached a "Real-Time" reporting standard. Every meal, travel expense, consulting fee, and educational item must be tracked and submitted to the CMS (Centers for Medicare & Medicaid Services). This data is made <strong>Publicly Available</strong> on the Open Payments website, allowing patients to see the financial relationships between their doctors and the industry.</p>
                        <p>In 2026, the Sunshine Act includes <strong>Non-Physician Practitioners</strong> (NPs, PAs, CRNAs, and even some clinical pharmacists). As a professional, you are responsible for accurate "Spend Tracking." If you provide a $25 lunch to an HCP, that must be recorded accurately against their NPI (National Provider Identifier) number. Inaccurate or "Missing" reports can lead to massive federal fines for the company and can damage the reputation of the HCP. Transparency is the "Sunlight" that prevents unethical behavior; if you are not willing to have the transaction posted on a public website, you should not be doing it.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Sunshine Act requires public reporting of all financial transfers to HCPs.</li><li>Non-Physician Practitioners (NPs/PAs) are now included in the reporting requirements.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: The Seven Elements of a Compliance Program',
                    'content': """
                        <p>The final module focuses on the <strong>OIG "Seven Elements"</strong> of an effective compliance program. In 2026, simply having a "Code of Ethics" is not enough; the program must be active and effective. The elements include: 1. Written Policies and Procedures. 2. A designated Compliance Officer and Committee. 3. Effective Training and Education. 4. Open Lines of Communication (Hotlines). 5. Internal Monitoring and Auditing. 6. Consistent Enforcement and Sanctions. 7. Prompt Response to Detected Problems.</p>
                        <p>A world-class 2026 professional is a "Compliance Champion." This means utilizing the <strong>Whistleblower Hotline</strong> if you observe unethical behavior without fear of retaliation. It means participating in "Audit Prep" with the same seriousness as a sales pitch. In 2026, ethical conduct is not a "barrier" to sales—it is a <strong>Requirement for Market Access</strong>. Large hospital systems will not do business with companies that have a history of non-compliance. By completing this certification, you have proven that you are a high-integrity professional dedicated to the 2026 AdvaMed standards. Stay ethical, stay transparent, and stay professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A compliance program must include internal auditing and a whistleblower hotline.</li><li>Ethical conduct is a mandatory requirement for doing business with major hospital systems.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: AdvaMed Code 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
