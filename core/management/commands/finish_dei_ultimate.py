from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes DEI with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Diversity, Equity & Inclusion (DEI)')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Microaggressions and Micro-Affirmations',
                    'content': """
                        <p>Microaggressions are subtle, everyday slights—verbal, nonverbal, or environmental—that communicate hostile or derogatory messages to marginalized groups. In 2026, we categorize these into <strong>Micro-insults</strong> (subtle snubs) and <strong>Micro-invalidations</strong> (denying a person’s experience). While often unintentional, their "death by a thousand cuts" effect creates a toxic environment that leads to high turnover and burnout. The inclusive professional learns to recognize these behaviors—like commenting on someone’s "accent" or assuming a person of color is in a junior role—and takes accountability for the impact, regardless of their intent.</p>
                        <p>To counter this, we use <strong>Micro-Affirmations</strong>. These are small acts of inclusion that foster belonging, such as giving credit for an idea, making eye contact during a presentation, or using a person’s correct name and pronouns. Micro-affirmations are contagious; they signal to the rest of the team that everyone is valued. By consciously practicing micro-affirmations, you build "social capital" and reinforce the psychological safety of the entire group. It is the practice of "noticing" excellence in places where it is traditionally overlooked.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Impact matters more than intent in microaggressions.</li><li>Use Micro-Affirmations to proactively build a culture of belonging.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Allyship and the "Upstander" Mindset',
                    'content': """
                        <p>In 2026, Allyship is defined as a <strong>verb, not a noun</strong>. It is not an identity you claim; it is a consistent practice of using your privilege to support others. A true ally moves from "Bystander" to "Upstander." When you witness an exclusionary behavior, you have a responsibility to intervene. This can be done through "Calling In" (a private conversation to educate) or "Calling Out" (a public correction when the behavior is harmful). Allyship requires you to listen more than you speak and to center the voices of those you are supporting rather than your own comfort.</p>
                        <p>Being an <strong>Upstander</strong> involves systemic advocacy. It means looking at who is missing from the meeting or who isn't being considered for the high-visibility project and speaking up. It is about "passing the mic"—creating opportunities for others to lead rather than speaking for them. In 2026, we emphasize that allyship is not a "rescue mission"; it is a partnership. By consistently acting as an upstander, you help dismantle the structural barriers that prevent diversity from becoming true inclusion.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Allyship is an ongoing practice, not a one-time label.</li><li>Move from "Bystander" to "Upstander" by actively intervening in exclusion.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Gender Identity and Expression in 2026',
                    'content': """
                        <p>The 2026 landscape of gender in the workplace is built on the principle of <strong>Self-Identification</strong>. This module distinguishes between Sex (assigned at birth), Gender Identity (one’s internal sense of being), and Gender Expression (how one presents to the world). Modern inclusive organizations respect all identities, including non-binary and gender-fluid individuals. The use of <strong>Correct Pronouns</strong> is a fundamental sign of respect and professional competence. Misgendering someone, especially after being corrected, is a violation of the "Not Petty or Trivial" harassment standard in many jurisdictions.</p>
                        <p>Structural inclusion for gender diversity includes the implementation of gender-neutral facilities and inclusive administrative systems. In 2026, "Gender-Neutral" is the design standard for new office spaces. Furthermore, HR systems must allow for preferred names and pronouns to be displayed in directories and email signatures. By removing the "gender binary" as a default, you create a space where every employee can bring their authentic self to work without the exhausting burden of "covering" or hiding their identity to fit in.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Gender identity is an internal sense of self; always respect chosen pronouns.</li><li>Inclusive infrastructure (neutral restrooms) is a 2026 workplace standard.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Culturally Responsive Conflict Resolution',
                    'content': """
                        <p>Conflict is inevitable in a diverse workplace, but it is not inherently negative. In 2026, we utilize <strong>Culturally Responsive Conflict Resolution</strong> to navigate disagreements. This recognizes that different cultures have different "Conflict Styles"—some are direct and high-emotion, while others are indirect and prioritize "saving face." An inclusive leader does not force everyone into a Western, corporate conflict model. Instead, they seek to understand the underlying cultural values and communication norms driving the disagreement.</p>
                        <p>The <strong>"Ouch/Oops" Framework</strong> is a 2026 tool for immediate resolution. If someone says something that hurts, the victim (or an upstander) says "Ouch." This is a signal to pause. The speaker then says "Oops," acknowledging the impact and opening a space for learning. This prevents small slights from escalating into formal HR grievances. By normalizing the "Oops," you maintain psychological safety while ensuring that exclusionary behavior is addressed in real-time before it hardens into a toxic cultural norm.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Conflict styles vary by culture; seek to understand norms before judging.</li><li>Use the "Ouch/Oops" framework for low-stakes, real-time correction.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: The Global Remote Workplace',
                    'content': """
                        <p>In 2026, inclusion must transcend physical office walls. The <strong>Global Remote Workplace</strong> introduces "Time Zone Equity" and "Digital Inclusion." Inclusive teams do not always force the same group of people (usually those in the "fringe" time zones) to wake up at 3 AM for meetings. Instead, they rotate meeting times and utilize asynchronous communication tools. Digital inclusion also means ensuring that remote workers have the same access to high-visibility "water cooler" conversations and mentorship opportunities as their in-office peers.</p>
                        <p>Countering <strong>"Proximity Bias"</strong>—the tendency for managers to favor employees they see in person—is a core 2026 leadership skill. This requires intentional "Virtual Drop-ins" and ensuring that promotions are based on objective outcomes rather than "desk time." In a remote world, inclusion is about the "Digital Presence." Leaders must ensure that Zoom/Teams meetings are accessible, using closed-captioning for neurodivergent or hard-of-hearing staff and ensuring that the "hand-raise" feature is used to prevent louder voices from dominating the digital space.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Practice "Time Zone Equity" by rotating meeting schedules.</li><li>Actively combat "Proximity Bias" to ensure remote workers aren't overlooked.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Inclusive Recruitment and Retention',
                    'content': """
                        <p>Inclusive recruitment in 2026 moves beyond "posting to a diverse job board." It involves a total audit of the <strong>Candidate Journey</strong>. This begins with "Gender-Neutral" job descriptions—removing aggressive language (e.g., "Rockstar," "Ninja") that has been shown to discourage female applicants. It continues through "Blind Screening," where names and identifying details are removed from resumes to prevent affinity bias. Finally, all interviews should be "Structured," meaning every candidate is asked the same questions in the same order, with a pre-set scoring rubric.</p>
                        <p>Retention is the true measure of a DEI program’s success. It is not enough to hire diverse talent; you must create a "Culture of Advancement." This involves <strong>Transparency in Promotion</strong>—clearly stating the metrics required for the next level—and "Sponsorship" (not just mentorship). A mentor talks <em>to</em> you; a sponsor talks <em>about</em> you in rooms where decisions are made. By formalizing sponsorship programs for underrepresented talent, you ensure that your leadership pipeline reflects the diversity of your entry-level workforce.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use structured interviews and blind screening to remove bias from hiring.</li><li>Sponsorship is the key to advancing underrepresented talent into leadership.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Disability, Accessibility, and Accommodations',
                    'content': """
                        <p>In 2026, accessibility is a <strong>Baseline Right</strong>, not an "extra" request. This module focuses on the "Social Model of Disability," which states that people are disabled by environmental barriers, not their medical conditions. Inclusion means practicing "Universal Design"—creating products and workspaces that are inherently accessible to everyone without the need for adaptation. This includes digital accessibility (WCAG 3.0 standards), ensuring all company software is compatible with screen readers and provides high-contrast options.</p>
                        <p>The <strong>Accommodations Process</strong> should be collaborative and non-adversarial. In an inclusive culture, an employee asking for an adjustable desk or a modified schedule is met with "How can we make this work?" rather than "Prove you need this." 2026 standards encourage "Quiet Accommodations"—changes that are made seamlessly without drawing unwanted attention to the employee’s disability. By normalizing these adjustments, you foster an environment where health and productivity are seen as synergistic rather than in conflict.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Universal Design makes the workplace accessible by default.</li><li>Accommodations should be a collaborative, supportive process, not a legal battle.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Sustaining a Culture of Belonging',
                    'content': """
                        <p>The final module focuses on <strong>DEI Sustainability</strong>. Culture is not a "project" with an end date; it is the sum of daily habits. Sustaining a culture of belonging requires "Inclusive Accountability." This means that DEI metrics—such as team belonging scores or diversity in the hiring pipeline—are tied to leadership performance reviews. When inclusion is a "business KPI," it remains a priority even during economic downturns or leadership changes. It is the transition from "Doing DEI" to "Being Inclusive."</p>
                        <p>We conclude with the <strong>"Belonging Audit."</strong> Individuals are encouraged to look at their own "Inner Circle"—who do you go to for advice? Who do you grab coffee with? If your personal and professional networks are monolithic, your perspective is limited. True inclusion ends with <strong>Humility and Growth</strong>. It is the recognition that you will make mistakes, you will have blind spots, and that the "work" is never truly finished. By staying curious and committed to the dignity of every individual, you contribute to a 2026 workplace that is not only more productive but more human.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Tie DEI metrics to leadership accountability and performance reviews.</li><li>Sustaining culture requires personal humility and a commitment to lifelong growth.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: DEI World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
