from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades DEI Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Diversity, Equity & Inclusion (DEI)')
            course.questions.all().delete()

            qs = [
                ('What is the difference between "Equality" and "Equity" in 2026?', 
                 ['They are the same thing', 'Equality is giving everyone the same; Equity is giving everyone what they need to succeed', 'Equality is for HR; Equity is for finance', 'Equity is only for remote workers'], 2),
                
                ('What is "Cognitive Diversity" and why is it a business advantage?', 
                 ['Diversity of age', 'Diversity of how people think and solve problems', 'Having different job titles', 'Diversity of clothing styles'], 2),
                
                ('In the context of Unconscious Bias, what are "Heuristics"?', 
                 ['Logical math formulas', 'Mental shortcuts the brain uses to process information quickly', 'Legal rules for hiring', 'Physical exercises for focus'], 2),
                
                ('What is "Psychological Safety"?', 
                 ['Having a secure office building', 'The belief that you can take risks and speak up without fear of punishment', 'A type of health insurance', 'The avoidance of all workplace conflict'], 2),
                
                ('Which leader behavior is most effective at building psychological safety?', 
                 ['Never admitting to a mistake', 'Demonstrating vulnerability and asking curious questions', 'Giving orders without explanation', 'Ignoring minority voices'], 2),
                
                ('What is the "Social Model" of Neurodiversity?', 
                 ['Viewing ADHD and Autism as deficits to be cured', 'Viewing neurological differences as natural variations and removing environmental barriers', 'A type of social media for the workplace', 'Only hiring people who think the same way'], 2),
                
                ('What is a "Micro-Affirmation"?', 
                 ['A small, subtle slight', 'A small act of inclusion that fosters belonging and validates others', 'A legal document for HR', 'A type of performance review'], 2),
                
                ('What is the difference between an "Upstander" and a "Bystander"?', 
                 ['An upstander watches; a bystander helps', 'An upstander actively intervenes to support others; a bystander watches without acting', 'An upstander is a manager; a bystander is a junior', 'There is no difference'], 2),
                
                ('What is "Proximity Bias" in the remote workplace?', 
                 ['Favoring people who live in the same city', 'The tendency for managers to favor employees they see in person over remote workers', 'Hiring people who work in the same time zone', 'Favoring people with the same hobbies'], 2),
                
                ('What are "Structured Interviews" designed to prevent?', 
                 ['Hiring too many people', 'Subjective bias and "gut-feeling" decisions', 'Questions about work history', 'Interviews that last too long'], 2),
                
                ('In 2026, what is "Universal Design" in accessibility?', 
                 ['Designing products for one specific group', 'Creating products and spaces that are inherently accessible to everyone by default', 'Designing only for mobile devices', 'A type of office furniture'], 2),
                
                ('What is the difference between a Mentor and a Sponsor?', 
                 ['A mentor is older; a sponsor is younger', 'A mentor talks to you; a sponsor talks about you in rooms where decisions are made', 'A mentor is for interns; a sponsor is for CEOs', 'They are identical roles'], 2),
                
                ('Which framework is used for real-time, low-stakes conflict correction?', 
                 ['The OODA Loop', 'The "Ouch/Oops" framework', 'The F.A.S.T. mnemonic', 'The SCAT6 tool'], 2),
                
                ('What is the benefit of "Blind Resume Screening"?', 
                 ['It makes hiring faster', 'It removes identifying details to prevent affinity bias during initial review', 'It helps verify education', 'It is only used for remote jobs'], 2),
                
                ('How do you maintain a "DEI Sustainability" culture?', 
                 ['Do one training session per year', 'By tying DEI metrics to leadership performance reviews and business KPIs', 'By only hiring one type of person', 'By ignoring workplace culture'], 2)
            ]

            for text, options, correct in qs:
                Question.objects.create(
                    course=course,
                    text=text,
                    option_1=options[0],
                    option_2=options[1],
                    option_3=options[2],
                    option_4=options[3],
                    correct_option=correct
                )

            self.stdout.write(self.style.SUCCESS('SUCCESS: DEI Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
