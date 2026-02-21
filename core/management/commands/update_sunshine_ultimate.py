from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Sunshine Act to 10 World-Class 2026 Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='The Sunshine Act')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Open Payments Mandate',
                    'content': """
                        <p>The Physician Payments Sunshine Act (Section 6002 of the ACA) is the federal law requiring medical technology and pharmaceutical manufacturers to report nearly all "Transfers of Value" made to healthcare providers. In 2026, the program is officially known as <strong>Open Payments</strong> and is managed by the Centers for Medicare & Medicaid Services (CMS). The goal is total financial transparency: by making these payments public, the law seeks to reduce conflicts of interest that could compromise clinical judgment or increase healthcare costs. In 2026, patients can access the "Open Payments Database" in real-time via mobile apps to see exactly how much money their doctor has received from the industry.</p>
                        <p>For the 2026 Program Year, the reporting criteria are strict. Manufacturers must track and report payments made to "Covered Recipients." While it was originally limited to doctors, the 2026 definition includes <strong>Physician Assistants (PAs), Nurse Practitioners (NPs), Clinical Nurse Specialists (CNSs), Certified Registered Nurse Anesthetists (CRNAs), and Certified Nurse Midwives (CNMs)</strong>. As a professional, you must understand that every cup of coffee, every consulting fee, and every flight you provide to any of these practitioners is a reportable event. Failure to report even a $20 meal can lead to significant federal audits for the organization.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Sunshine Act is now known as the "Open Payments" program managed by CMS.</li><li>Covered Recipients include NPs, PAs, and CRNAs, in addition to Physicians.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: 2026 Reporting Thresholds and Aggregation',
                    'content': """
                        <p>In 2026, CMS has updated the "De Minimis" thresholds for reporting. For the 2026 data collection period (January 1 – December 31, 2026), individual transfers of value less than <strong>$13.82</strong> are generally not reportable. However, there is a critical "Aggregation Rule": if the total annual value provided to a single recipient exceeds <strong>$138.13</strong>, then <em>every single cent</em>—including those under the $13.82 limit—must be reported retroactively. This requires meticulous "Aggregate Spend Tracking" by sales and marketing teams.</p>
                        <p>For example, if you provide a $10 lunch to a Nurse Practitioner 14 times in a year, you have exceeded the $138.13 threshold. Even though each individual lunch was below the $13.82 single-item limit, you are now legally required to report all 14 lunches. In 2026, "Manual Tracking" is considered a high-risk failure. World-class organizations utilize AI-driven expense systems that automatically link every receipt to the recipient's <strong>National Provider Identifier (NPI)</strong> number, ensuring that the aggregate total is monitored in real-time to prevent accidental non-compliance.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Individual items < $13.82 are exempt unless the annual total exceeds $138.13.</li><li>All payments must be linked to the recipient's NPI for accurate aggregate tracking.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Natures of Payment: Categorizing Value',
                    'content': """
                        <p>CMS requires that every transfer of value be assigned a specific "Nature of Payment." In 2026, there are 18 mandatory categories. The most common include: <strong>Consulting Fees</strong>, <strong>Food and Beverage</strong>, <strong>Travel and Lodging</strong>, <strong>Honoraria</strong>, and <strong>Education</strong>. A 2026 update includes the mandatory reporting of "Debt Forgiveness," "Long-term medical supply or device loans," and "Acquisitions." Correct categorization is vital because the public and regulators use this data to look for patterns of "Influential Spending."</p>
                        <p>Mis-categorizing a payment—for example, listing a "Gift" as "Education" or "Consulting"—is a serious compliance violation. In 2026, the <strong>"Payment Context"</strong> field is also mandatory for certain recipients like teaching hospitals. This allows the company to explain <em>why</em> the payment was made (e.g., "Grant for Robotic Surgery Simulation"). For research-related payments, CMS allows for a "Delayed Publication" if the payment is tied to a product still seeking FDA approval, protecting the company's trade secrets while maintaining transparency.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Every transfer must be assigned one of 18 "Nature of Payment" categories.</li><li>Research payments can be delayed from public view until FDA approval or 4 years pass.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Indirect and Third-Party Payments',
                    'content': """
                        <p>A common misconception in 2026 is that if a company doesn't pay a doctor "directly," it isn't reportable. This is false. The Sunshine Act captures <strong>Indirect Payments</strong>—transfers of value made through a third party (like a medical society, a travel agency, or a Contract Research Organization) where the manufacturer "knows or should know" the identity of the covered recipient. For example, if a company pays a medical society $10,000 to cover the travel expenses of five specific surgeons, the company must report $2,000 as an indirect payment to each surgeon.</p>
                        <p>The "Request or Behalf" rule also applies. If a surgeon asks a company to make a <strong>Charitable Contribution</strong> to their private foundation in lieu of a speaking fee, that payment is still reportable as a "Transfer of Value" to that surgeon. In 2026, we also monitor "Immediate Family" interests. If a company provides a consulting contract to the spouse of a hospital's Chief of Surgery, it must be disclosed. These "Hidden Transfers" are a primary focus of 2026 enforcement, as they are often used to bypass standard transparency limits.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Indirect payments made through third parties are fully reportable.</li><li>Payments made to a charity "at the request" of a doctor are reportable.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS('SUCCESS: Sunshine Act Part 1 (Stable) Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
