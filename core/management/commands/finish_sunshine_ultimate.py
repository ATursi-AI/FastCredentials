from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Sunshine Act with Modules 5-10 at World-Class Density'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='The Sunshine Act')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: The 2026 Review and Dispute Window',
                    'content': """
                        <p>The Open Payments process does not end with the manufacturer\'s submission. In 2026, the <strong>Review and Dispute Window</strong> is the most critical period for Healthcare Professionals (HCPs). Every year, from April 1 to May 15, covered recipients have a 45-day window to log into the CMS portal and review the data submitted about them. If an HCP finds an error—such as a meal they didn\'t attend or an inflated consulting fee—they can initiate a "Dispute." In 2026, many HCPs utilize "Digital Compliance Assistants" that automatically cross-reference their personal calendars against the CMS data to flag discrepancies instantly.</p>
                        <p>Manufacturers have an additional 15 days (until May 30) to resolve these disputes with the HCP. If a dispute is not resolved by the deadline, the data will still be published on the public website, but it will be marked as <strong>"Disputed."</strong> This tag is a red flag for hospital compliance departments and the media. In 2026, the "Correction of Inaccurate Data" is a top priority; failing to resolve a valid dispute can lead to a loss of trust and potential litigation from the HCP. As a professional, your meticulous record-keeping during the year is what prevents these disputes from happening in the first place.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HCPs have a 45-day window (April 1 – May 15) to dispute reported data.</li><li>Resolved disputes must be finalized by May 30 to avoid being marked as "Disputed" publicly.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: The 2026 Penalty Landscape: Knowing Failures',
                    'content': """
                        <p>In 2026, the financial consequences for Sunshine Act violations have reached record levels. CMS has adjusted penalties for inflation, and for the 2026 program year, the maximum penalty for a single manufacturer that "knowingly fails" to report a transfer of value is <strong>$1.45 Million per year</strong>. A "Knowing Failure" occurs when the organization was aware of the payment but chose not to report it or utilized third parties to hide the transfer. Even "Unintentional" errors can lead to a maximum annual penalty of over $145,000. These fines are per reporting entity, meaning large parent companies with multiple subsidiaries can face compounded penalties.</p>
                        <p>Beyond the direct fines, 2026 enforcement focuses on <strong>Data Integrity Audits</strong>. If CMS finds that a company has a high error rate in its "Nature of Payment" categorizations, they may launch a full-scale audit of the company’s entire compliance program. Furthermore, the Office of Inspector General (OIG) uses Open Payments data as a "Lead Generator" for <strong>Anti-Kickback Statute</strong> investigations. If the data shows a surgeon receiving high consulting fees alongside a massive spike in their use of that company\'s device, it triggers an automatic "Risk Score" flag. In 2026, transparency is not just about a website; it is an active investigative tool for the federal government.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Knowing failures to report can lead to annual penalties exceeding $1.45 million.</li><li>Open Payments data is used by the OIG to flag potential Anti-Kickback violations.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Teaching Hospitals and Specialized Reporting',
                    'content': """
                        <p>The Sunshine Act specifically monitors <strong>Teaching Hospitals</strong>—institutions that receive Medicare funding for medical residency programs. In 2026, CMS publishes a "Mandatory Teaching Hospital List" every October. If a hospital is on this list, every research grant, educational donation, or sponsorship provided to that institution must be reported under the hospital\'s name. In 2026, the reporting must include the specific <strong>Department</strong> (e.g., Cardiology, Orthopedics) that received the value to provide granular transparency into how industry funds are flowing through academic medical centers.</p>
                        <p>A common 2026 challenge is <strong>Split-Reporting</strong>. If a company provides a meal for 20 residents and one attending physician at a teaching hospital, the meal for the residents is reported as a single transfer to the <em>Hospital</em>, while the meal for the attending physician is reported as a transfer to that <em>individual</em> HCP. This "Dual-Tracking" requires precise attendance logs. In 2026, we also track "Research Infrastructure" support. If a company pays for a new simulation lab or a specialized computer system for a teaching hospital, this must be reported as a "Transfer of Value," as it lowers the institution\'s operational costs and could be seen as an inducement for future device adoption.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Payments to Teaching Hospitals must be reported using the annual CMS hospital list.</li><li>Reports should specify the receiving department within the hospital for greater transparency.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Ownership and Investment Interests',
                    'content': """
                        <p>The Sunshine Act requires the reporting of <strong>Physician Ownership and Investment Interests</strong> in medical technology companies. If a physician (or an immediate family member) owns stock, stock options, or has an ownership stake in a manufacturer, the company must report the total dollar amount of that interest. This is designed to identify "Physician-Owned Distributors" (PODs), which in 2026 are under intense federal scrutiny. The concern is that a physician-investor may be inclined to use products from a company they own, regardless of whether it is the best or most cost-effective clinical option for the patient.</p>
                        <p>In 2026, "Immediate Family" includes spouses, children, step-children, parents, and siblings. If a manufacturer hires the brother of a hospital executive as a high-paid consultant, and that brother has an ownership interest in the company, the transaction is reportable. Failure to disclose these <strong>Conflicts of Interest</strong> is a Tier 3 violation. Furthermore, any dividends or "Return on Investment" (ROI) payments made to the physician-investor must also be reported as a transfer of value. Transparency in ownership ensures that patients can verify if their doctor has a "vested interest" in the specific implants or devices being used in their surgery.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>All physician and family ownership or investment interests must be reported annually.</li><li>Dividends and ROI payments to physician-investors are reportable transfers of value.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Recruiting and Pre-Employment Spend',
                    'content': """
                        <p>A 2026 "Compliance Trap" involves <strong>Recruiting and Pre-Employment Spending</strong>. If a company is recruiting a physician to be an In-House Medical Director or a consultant, the travel, lodging, and meals provided during the interview process are <strong>Full Reportable</strong>. Many professionals mistakenly believe that since the physician isn't an "employee" or "contractor" yet, the Sunshine Act doesn't apply. It does. As long as the individual meets the definition of a "Covered Recipient" (e.g., they hold an active NPI), every dollar spent on their recruitment must be tracked and reported.</p>
                        <p>This also applies to "Candidate Dinners" and site visits. In 2026, the standard is to notify the candidate <em>before</em> the interview that the expenses will be reported under the Sunshine Act. This "Proactive Disclosure" prevents future disputes and maintains professional trust. If the candidate is hired, the reporting continues; if they are not hired, the reporting of the recruitment spend still remains on their public record for six years. Accurate "Pipeline Tracking" ensures that the company remains compliant even during periods of rapid growth and high-level medical recruitment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Interview and recruitment expenses for HCPs are fully reportable under the Sunshine Act.</li><li>Always notify candidates that recruitment-related transfers of value will be made public.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: State vs. Federal Preemption',
                    'content': """
                        <p>The final module covers the complex interplay between the Federal Sunshine Act and <strong>State Transparency Laws</strong>. While the Sunshine Act preempts (overrides) most state laws regarding the reporting of the *same* information, many states have "Stricter" or "Additional" requirements. For example, states like <strong>Massachusetts, Vermont, and Maine</strong> have laws that require the reporting of payments to healthcare professionals who are <em>not</em> covered by the federal act (such as registered nurses or office managers) or require the reporting of samples and marketing materials that are exempt federally.</p>
                        <p>In 2026, a "One-Size-Fits-All" compliance plan is a recipe for failure. You must follow the <strong>"Strictness Standard"</strong>: if a state law requires more data than the federal law, you must collect and report that additional data to the state agency. Some states also have "Gift Bans" that prohibit certain transfers of value entirely, even if they would be reportable federally. As a 2026 professional, you are responsible for knowing the specific regulations of the state where you are doing business. By mastering the 2026 Sunshine Act, you protect your organization's reputation and contribute to a healthcare system built on trust and clinical integrity.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Federal law preempts state law only on identical reporting requirements.</li><li>Always follow the "Strictness Standard" when state laws require more data than the federal act.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Sunshine Act 2026 World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
