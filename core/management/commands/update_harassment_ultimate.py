from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Sexual Harassment Prevention to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Sexual Harassment Prevention')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Legal Framework: Federal vs. State Standards',
                    'content': """
                        <p>Sexual harassment is a form of workplace discrimination prohibited by both federal and state law. In 2026, the legal landscape is more complex than ever. At the federal level, Title VII of the Civil Rights Act of 1964 remains the foundational law, as interpreted by the Supreme Court in the landmark <i>Bostock v. Clayton County</i> decision. However, in January 2026, the EEOC rescinded its previous 2024 enforcement guidance regarding gender identity, creating a period of federal regulatory shift. For an organization to be truly compliant, it must understand that while federal guidance may change, state and local laws—particularly in <strong>New York, California, and Illinois</strong>—often set a much higher bar for employer liability.</p>
                        <p>In New York, for example, the law requires every employer, regardless of size, to provide <strong>annual interactive training</strong> to all employees. In California, the mandate includes specific hour requirements (1 hour for employees, 2 hours for supervisors) every two years. Furthermore, these states have removed the "Severe or Pervasive" requirement that historically protected employers. Harassment is now legally defined as any conduct that rises above a "petty slight or trivial inconvenience." This shift means that even a single incident, if it is more than a minor annoyance, can create legal liability for the organization. As a professional, you are held to the standard of the most protective law in your jurisdiction.</p>
                        <p>This module establishes the core principle of 2026 harassment prevention: <strong>Zero Tolerance is not just a policy, it is a business necessity.</strong> Beyond the legal fees and settlements, harassment destroys "Psychological Safety," leading to massive drops in productivity and high employee turnover. We will explore the technical nuances of how "Implied Liability" works—where an employer can be held responsible for a supervisor’s actions even if the company was unaware of them. By the end of this course, you will understand the legal, ethical, and professional framework required to maintain a culture of dignity and respect.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Federal laws (Title VII) and state laws (NY/CA) both prohibit sex-based harassment.</li><li>Modern laws have moved from "Severe or Pervasive" to any conduct above a "Petty Slight."</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Defining Harassment: Hostile Work Environment',
                    'content': """
                        <p>A "Hostile Work Environment" is the most common form of sexual harassment and also the most misunderstood. It occurs when unwelcome conduct based on sex—including gender identity and sexual orientation—interferes with an individual\'s work performance or creates an intimidating, offensive, or abusive atmosphere. In 2026, the "Hostile Work Environment" is not limited to physical office spaces; it extends to <strong>Digital Environments</strong> like Slack threads, Zoom calls, and social media interactions. If the conduct is sex-based and unwelcome, it can contribute to a hostile environment regardless of where the work is being performed.</p>
                        
                        <p>The technical metric for a hostile environment is the <strong>"Reasonable Person" Standard</strong>. The law asks: "Would a reasonable person in the victim’s shoes find this behavior hostile or offensive?" This removes the "intent" of the harasser from the equation. A coworker who claims they were "just joking" or "being friendly" can still be legally liable for harassment if the impact of their behavior creates a hostile environment for others. Common examples include persistent unwanted requests for dates, the display of sexually explicit materials (including digital images), and the use of demeaning or gendered language. In 2026, "Gender-Based Bullying"—where a person is targeted because they don\'t conform to traditional gender stereotypes—is a primary component of hostile environment claims.</p>
                        <p>It is important to understand that a hostile environment can be created by anyone in the workplace: a supervisor, a coworker, or even a non-employee like a client or vendor. If an employer knows (or should have known) about the behavior and fails to take <strong>immediate and appropriate corrective action</strong>, they are legally liable. This module focuses on the "cumulative effect" of behavior. While one off-hand comment might be a petty slight, a pattern of such comments across a team creates a systemic culture of hostility that the law is designed to dismantle.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Hostile environments are defined by the "impact" on the victim, not the "intent" of the harasser.</li><li>The workplace includes digital platforms, remote work, and social media interactions.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Quid Pro Quo: The Abuse of Power',
                    'content': """
                        <p>Quid Pro Quo is a Latin phrase meaning "This for That." In the legal context of sexual harassment, it refers to situations where an employment benefit is made conditional on sexual favors, or where an employment detriment is threatened for refusing them. This is the most direct form of <strong>Power-Based Harassment</strong> and usually involves a person in a position of authority, such as a manager, supervisor, or executive. Because of the inherent power imbalance, "consent" in a Quid Pro Quo situation is often legally scrutinized; even if a victim "agrees" to the behavior to save their job, it is still considered unwelcome and illegal harassment.</p>
                        <p>In 2026, the law applies <strong>Strict Liability</strong> to employers in Quid Pro Quo cases involving supervisors. This means that if a supervisor fires an employee for refusing a sexual advance, the company is automatically liable—even if the company has a perfect anti-harassment policy and even if the CEO had no idea the behavior was happening. This "Agent of the Employer" doctrine recognizes that when a company gives a manager the power to hire, fire, or promote, the company is responsible for how that manager uses (or abuses) that power. Quid Pro Quo is not limited to "sex" in the physical sense; it includes any romantic or sexualized favor exchanged for professional gain.</p>
                        <p>Common "Red Flags" for Quid Pro Quo include performance reviews that suddenly turn negative after a rejected date invitation, "exclusive" off-site meetings that feel like dates, or promises of promotions in exchange for "staying late" in a sexualized context. To prevent these incidents, world-class organizations implement <strong>"Consensual Relationship Policies"</strong> that require supervisors to disclose any romantic interest in a subordinate so that reporting lines can be moved. Transparency is the only defense against the appearance (and reality) of Quid Pro Quo harassment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Quid Pro Quo is "this for that" harassment involving an abuse of power.</li><li>Employers are "strictly liable" for supervisor-led Quid Pro Quo harassment.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Gender Identity and 2026 Protections',
                    'content': """
                        <p>The 2026 landscape of gender in the workplace is defined by a <strong>conflict between federal rescission and state mandate</strong>. On January 22, 2026, the federal EEOC rescinded guidance that previously categorized misgendering as per-se harassment. However, as an employee or manager, you must understand that the Supreme Court\'s <i>Bostock</i> ruling still prohibits discrimination based on gender identity. Furthermore, states like New York and California have explicitly codified that intentional, repeated misgendering and the denial of restroom access consistent with a person’s identity are forms of unlawful harassment. To be "World-Class" is to prioritize the highest level of respect, regardless of shifts in federal guidance.</p>
                        <p>Harassment based on <strong>Gender Identity and Expression</strong> involves targeting an individual because they are transgender, non-binary, or gender-fluid, or because they do not conform to traditional societal expectations of how a "man" or "woman" should look or act. This includes "Deadnaming" (intentionally using a person’s name from before their transition) or mocking a person’s choice of clothing or grooming. In 2026, inclusive workplaces recognize that a person’s identity is not a "debate" or a "political stance"; it is a protected characteristic that requires professional respect. Ignoring a person’s request for correct pronouns is not just "insensitive"—it is a behavior that can contribute to a Hostile Work Environment claim.</p>
                        <p>Effective 2026 policies include <strong>Gender Transition Protocols</strong>. These are structured plans that help an employee transition in the workplace while maintaining their dignity and safety. This involves updating email signatures, badges, and directories, and providing a clear "Zero Tolerance" message to the rest of the team. By proactively supporting gender diversity, an organization reduces the risk of harassment claims and builds a culture where "Cognitive Diversity" can flourish. Respecting gender identity is the 2026 benchmark for professional competence and cultural intelligence.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Intentional misgendering and deadnaming are actionable forms of harassment.</li><li>State laws (NY/CA) maintain strict protections even when federal guidance shifts.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Harassment Part 1 (1-4) pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
