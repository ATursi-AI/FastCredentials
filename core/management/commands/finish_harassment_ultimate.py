from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Harassment Prevention with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Sexual Harassment Prevention')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Sexual Orientation and Intersectionality',
                    'content': """
                        <p>In 2026, harassment prevention is rooted in the understanding of <strong>Sexual Orientation</strong> as a core protected characteristic. Harassment based on sexual orientation includes any unwelcome conduct directed at an individual because they are (or are perceived to be) gay, lesbian, bisexual, or asexual. This includes derogatory comments, "jokes" about sexual preferences, or the use of slurs. Under the 2026 legal framework, it is irrelevant whether the harasser is of the same or different sex as the victim; the focus remains entirely on whether the conduct was motivated by sexual orientation or gender-based stereotypes.</p>
                        <p>We also address <strong>Intersectionality</strong>—the concept that an individual can experience harassment based on a combination of protected characteristics. For example, a woman of color may experience harassment that is both sexual and racial in nature. In 2026, courts and the EEOC analyze the "Total Circumstances" of the workplace. If a manager targets an employee with a combination of sexist and homophobic remarks, the legal liability is compounded. An inclusive culture requires the recognition that identities are layered, and harassment often targets the intersection of those identities to isolate and marginalize the victim.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Harassment based on perceived or actual sexual orientation is illegal.</li><li>Intersectionality recognizes that harassment can target multiple protected identities simultaneously.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Bystander Intervention: The 5 Ds',
                    'content': """
                        <p>Bystander intervention is the most effective tool for stopping a toxic culture before it scales into legal liability. In 2026, "Passive Observation" is no longer the professional standard; we advocate for the <strong>"Upstander" Mindset</strong>. Most harassment occurs in front of witnesses, and the silence of those witnesses is often interpreted by the harasser as approval. By intervening, you signal to the victim that they are supported and to the harasser that their behavior is unwelcome and will not be tolerated by the community.</p>
                        
                        <p>We utilize the <strong>5 Ds Framework</strong> for safe intervention: 1. <strong>Direct</strong>: Speak up in the moment ("That comment is inappropriate"). 2. <strong>Distract</strong>: Interrupt the situation by changing the subject or creating a diversion. 3. <strong>Delegate</strong>: Ask someone with more authority (a manager or HR) to intervene. 4. <strong>Delay</strong>: Check in with the victim after the fact to offer support. 5. <strong>Document</strong>: Keep a factual record of what you witnessed. You do not need to be a "hero"; you just need to be a presence that disrupts the normalized cycle of harassment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Intervention disrupts harassment and signals community disapproval.</li><li>Use the 5 Ds to intervene in a way that is safe and effective for you.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Retaliation: The #1 Source of Liability',
                    'content': """
                        <p>Retaliation is legally defined as any "Adverse Action" taken against an employee because they complained about harassment or participated in an investigation. In 2026, <strong>Retaliation is the most common claim</strong> filed with the EEOC, often resulting in higher settlements than the original harassment claim itself. An adverse action is not limited to firing or demotion; it includes "Social Freezing" (excluding the employee from meetings), unfair shift changes, or giving a "spiteful" performance review. The law protects employees even if the original harassment claim is eventually found to be unsubstantiated, as long as the report was made in "Good Faith."</p>
                        <p>To prevent retaliation, organizations must implement a <strong>"Blind Protection" Protocol</strong>. Once a report is made, HR must monitor the reporter’s career trajectory for at least 12 months to ensure no subtle punishments are occurring. Managers must be explicitly trained that "ignoring" or "avoiding" a whistleblower out of discomfort is, in itself, a form of retaliation. In 2026, the standard is clear: a victim of harassment should never feel that reporting the behavior was a "career-ending move." Protecting the whistleblower is the only way to maintain the integrity of the reporting system.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Retaliation includes any adverse action, including social exclusion or shift changes.</li><li>Reporting in "good faith" is protected even if the harassment claim is not proven.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: The Managerial "Duty to Act"',
                    'content': """
                        <p>In 2026, managers and supervisors are held to a <strong>Higher Standard of Responsibility</strong>. A manager does not have the "luxury" of being a passive bystander. If a supervisor observes harassment, or if an employee tells them about harassment "in confidence," the supervisor has a legal <strong>Duty to Act</strong>. They must report the incident to HR or the designated compliance officer immediately. A supervisor who fails to report known harassment can be held personally liable in some states and can create "Automatic Liability" for the entire organization.</p>
                        <p>Effective documentation is the manager’s primary professional tool. When a report is received, the manager must record the "Who, What, When, and Where" without including personal opinions or "editorializing" the victim’s character. This documentation must be factual and contemporaneous (written at the time of the event). 2026 standards also require managers to provide the victim with a clear explanation of the <strong>Anti-Retaliation Policy</strong> immediately. By acting as a formal conduit to HR, the manager ensures that the organization can fulfill its legal duty to perform a "Prompt and Thorough Investigation."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Managers must report harassment even if the victim asks them to keep it "secret."</li><li>Contemporaneous, factual documentation is required for all reported incidents.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Third-Party and Digital Harassment',
                    'content': """
                        <p>The workplace in 2026 is no longer a physical box; it is a <strong>Network</strong>. This means an employer’s responsibility extends to harassment committed by non-employees, such as clients, vendors, or independent contractors. If a client makes sexual advances toward your employee and you fail to intervene because "the client is always right," you have violated the law. Employers must use their economic and contractual leverage to protect their staff from third-party predators. This includes adding "Conduct Clauses" to vendor contracts and being prepared to fire a client to protect an employee’s dignity.</p>
                        <p>Digital harassment is another 2026 priority. This includes <strong>"Cyber-Leering"</strong> (inappropriate staring on Zoom), sending sexually explicit emojis, or "Doom-Scrolling" a coworker’s personal Instagram to find swimsuit photos. Because digital interactions provide a "Permanent Receipt," this is often the easiest form of harassment to prove. A "Private Message" on Slack or a "DM" on social media that is sexualized and unwelcome is just as illegal as an in-person comment. Organizations must enforce a "Professional Digital Boundary" policy that treats the virtual workspace with the same gravity as the physical boardroom.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Employers are liable for harassment by clients and vendors if they fail to act.</li><li>Digital harassment (Slack, Zoom, Social Media) creates a permanent legal record.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: The "Not Petty or Trivial" Standard',
                    'content': """
                        <p>For decades, employers relied on the "Severe or Pervasive" defense—arguing that a few comments or one incident didn't "rise to the level" of harassment. In 2026, that defense has been largely dismantled in states like New York. The new standard is <strong>"Not Petty or Trivial."</strong> If an employee can prove they were treated less well than others because of their sex, and the behavior was more than a minor annoyance, they have a valid claim. This "Low-Bar" standard is designed to catch toxic behavior *before* it becomes pervasive.</p>
                        <p>What qualifies as "More than Petty"? Repeatedly asking a subordinate about their dating life, making comments about a coworker\'s "attractiveness" in front of the team, or the persistent use of gendered nicknames (e.g., "Honey," "Sweetheart") all meet the 2026 threshold for actionable harassment. The law recognizes that these behaviors create a "stigma" that prevents the victim from feeling like an equal professional. By shifting the focus from "Severity" to "Dignity," the 2026 standard forces every employee to maintain a baseline of professional conduct that is above the level of a petty slight.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "Severe or Pervasive" defense is being replaced by the "Not Petty or Trivial" standard.</li><li>Even single incidents can be actionable if they are more than a minor annoyance.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Investigations and Victims\' Rights',
                    'content': """
                        <p>When a report is filed, the organization must initiate a <strong>Prompt, Thorough, and Impartial Investigation</strong>. In 2026, victims have the right to a process that is transparent and free from bias. This usually involves an "External Investigator" for claims involving high-level executives to ensure there is no conflict of interest. The investigation must include interviews with all parties and witnesses, and a review of all digital evidence (emails, Slack, etc.). While "Absolute Confidentiality" cannot be guaranteed (as the accused has a right to know the charges), the information must be kept on a "Need-to-Know" basis to protect all involved.</p>
                        <p>Victims also have the right to <strong>Interim Protections</strong>. While the investigation is ongoing, the employer may need to move the accused to a different shift or a different building to ensure the victim is not further traumatized. Crucially, the employer should not move the *victim* in a way that feels like a punishment (e.g., a longer commute), as this could be interpreted as retaliation. Once the investigation is complete, the employer must take "Appropriate Corrective Action," which ranges from mandatory counseling and formal warnings to immediate termination. The goal is to ensure the harassment stops and never recurs.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Investigations must be impartial and often require external experts for high-level claims.</li><li>Victims have a right to interim protections that do not negatively impact their job.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Cultivating a Culture of Consent',
                    'content': """
                        <p>The final module focuses on the <strong>Culture of the Organization</strong>. Prevention is not just about avoiding lawsuits; it is about building a workplace where every individual feels they can contribute at their highest level. This requires a "Culture of Consent"—the understanding that professional boundaries are non-negotiable and that "No" (or a lack of an enthusiastic "Yes") must be respected. In 2026, we emphasize "Social Intelligence" as a core professional skill. This means being able to read "Non-Verbal Cues" and understanding that a coworker’s polite smile does not equal a desire for romantic attention.</p>
                        <p>We conclude with <strong>Personal Accountability</strong>. Every employee, from the CEO to the intern, is a "Culture Builder." By modeling respectful behavior, using inclusive language, and acting as an upstander, you create a self-policing environment where harassers find no "cover" to operate. A world-class organization is one where the anti-harassment policy is not a document in a drawer, but a lived reality in every Slack message, every meeting, and every professional interaction. Respect is the foundation of excellence; by completing this training, you are committing to that standard.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Consent and professional boundaries are the foundation of a healthy workplace.</li><li>Every employee is a "Culture Builder" responsible for maintaining a respectful environment.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Harassment World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
