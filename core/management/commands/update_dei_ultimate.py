from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades DEI to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Diversity, Equity & Inclusion (DEI)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 DEI Framework: From Compliance to Excellence',
                    'content': """
                        <p>In 2026, Diversity, Equity, and Inclusion (DEI) have transitioned from a human resources "checklist" to a core business strategy. Organizations no longer view DEI as a legal requirement alone, but as a driver of <strong>Cognitive Diversity</strong>—the inclusion of people who think, solve problems, and perceive the world differently. This framework recognizes that diverse teams are 35% more likely to outperform their peers in innovation and problem-solving. True inclusion isn't about ignoring differences; it is about leveraging them to build a more resilient and creative organization.</p>
                        <p>The "E" in DEI—<strong>Equity</strong>—is the most critical 2026 evolution. While "Equality" means giving everyone the same pair of shoes, "Equity" means giving everyone a pair of shoes that actually fits. In a workplace context, this means acknowledging that different employees start from different positions and face different systemic barriers. An equitable organization proactively identifies these gaps in recruitment, promotion, and professional development to ensure that "meritocracy" is actually fair. Equity is the mechanism that allows diversity to thrive.</p>
                        <p>Finally, we must understand <strong>Inclusion</strong> as the active, daily practice of creating a culture where people feel they belong. Diversity is being invited to the party; inclusion is being asked to dance. In 2026, inclusion is measured by "Psychological Safety"—the belief that one can speak up with ideas, questions, or mistakes without fear of being punished or humiliated. This module establishes the foundation for the rest of the course: DEI is not a destination, but a continuous process of cultural evolution that benefits every single member of the team.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>DEI drives "Cognitive Diversity," which is a primary engine for innovation.</li><li>Equity is about providing specific resources to ensure everyone has a fair chance at success.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Unconscious Bias and the OODA Loop',
                    'content': """
                        <p>Unconscious bias (implicit bias) refers to the social stereotypes about certain groups of people that individuals form outside their own conscious awareness. In 2026, we recognize that having bias does not make you a "bad person"—it makes you human. Our brains are hardwired to use <strong>Heuristics</strong> (mental shortcuts) to process the massive amount of information we receive daily. However, these shortcuts often lead to "Affinity Bias" (favoring people who are like us) or "Confirmation Bias" (only noticing information that supports our existing beliefs).</p>
                        <p>To combat bias in high-stakes decisions—like hiring or performance reviews—we utilize the <strong>OODA Loop</strong> (Observe, Orient, Decide, Act). When you "Observe" a candidate or a situation, you must "Orient" yourself to your own potential biases. Ask yourself: "Am I reacting to their credentials, or to the fact that they went to the same college as me?" By slowing down the "Decide" phase, you allow your conscious, logical mind to override the knee-jerk, biased response of your subconscious. This is known as "System 2 Thinking," and it is the primary tool for objective leadership.</p>
                        <p>Bias mitigation also requires <strong>Structural Changes</strong>, not just individual awareness. In 2026, world-class organizations use "Blind Resume Screening" and "Standardized Interview Rubrics" to remove the opportunity for bias to take root. If you rely on "gut feeling" to make decisions, you are essentially relying on your biases. This module teaches you to identify the specific biases that impact your industry and provides the tactical frameworks needed to move from subjective "feelings" to objective, data-driven inclusion.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Unconscious bias is a natural byproduct of the brain's mental shortcuts (heuristics).</li><li>Mitigate bias by using the OODA loop and objective, standardized decision rubrics.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Psychological Safety: The Foundation of Inclusion',
                    'content': """
                        <p>Psychological Safety, a concept popularized by Harvard’s Amy Edmondson, is the single most important predictor of high-performing teams. It is the shared belief that the team is safe for <strong>Interpersonal Risk-Taking</strong>. In an environment with low psychological safety, employees stay silent about errors to avoid blame, leading to catastrophic organizational failures. In an inclusive 2026 workplace, psychological safety allows for "Intellectual Friction"—the ability to disagree with the boss or a colleague respectfully to reach a better outcome.</p>
                        
                        <p>Leaders build psychological safety through <strong>Vulnerability and Curiosity</strong>. When a leader admits they don't have all the answers or shares a mistake they made, it gives the rest of the team permission to be human. Inclusion means actively soliciting the "minority voice" in a meeting. If one person is dominating the conversation, an inclusive leader will pause and say, "I'd like to hear the perspective of someone who hasn't spoken yet." This ensures that the quietest person in the room—who may have the best idea—feels safe enough to contribute.</p>
                        <p>Crucially, psychological safety is not about "being nice" or lowering standards. It is about <strong>High Accountability and High Support</strong>. It creates a "fail-fast, learn-faster" culture. In 2026, we distinguish between "Blameworthy Failures" (negligence) and "Intelligent Failures" (experimental mistakes in new territory). By celebrating intelligent failures, you foster a culture of innovation where diversity of thought is not just welcomed, but required for the organization to thrive.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Psychological safety allows for "Intellectual Friction" and risk-taking without fear of punishment.</li><li>Inclusive leaders actively solicit the "minority voice" and celebrate "intelligent failures."</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Neurodiversity: The New Frontier of DEI',
                    'content': """
                        <p>Neurodiversity is the concept that neurological differences—such as ADHD, Autism, Dyslexia, and Dyspraxia—are natural variations in the human genome rather than "deficits" that need to be "cured." In 2026, neurodiversity is recognized as a <strong>Competitive Advantage</strong>. For example, individuals on the autism spectrum often possess exceptional attention to detail and pattern recognition, while those with ADHD frequently excel in hyper-focus and creative crisis management. An inclusive workplace doesn't just "accommodate" neurodivergent staff; it optimizes the environment to let their unique strengths shine.</p>
                        <p>Inclusive design for neurodiversity often benefits the entire workforce. This includes <strong>Sensory Management</strong> (providing quiet zones or noise-canceling headphones), <strong>Clear Communication</strong> (providing written instructions after verbal meetings), and <strong>Flexible Workflows</strong>. In 2026, we move away from the "One Size Fits All" management style. Instead, managers use "User Manuals for Employees," where each staff member documents how they work best, how they prefer to receive feedback, and what their specific "sensory triggers" are.</p>
                        <p>The "social model of disability" is the backbone of neuro-inclusion. It posits that people are not disabled by their conditions, but by a <strong>World that is Not Built for Them</strong>. If a dyslexic employee is forced to read long, poorly formatted memos, the memo is the problem, not the employee. By using inclusive technologies—like text-to-speech, AI-driven summaries, and visual project management tools—you remove the barriers to participation. This module explores how to build a "Neuro-Inclusive" culture that values results over rigid social or behavioral conformity.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Neurodiversity is a natural variation and a competitive advantage in innovation.</li><li>The "social model" of disability focuses on removing environmental barriers to participation.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: DEI World-Class Part 1 (1-4) pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
