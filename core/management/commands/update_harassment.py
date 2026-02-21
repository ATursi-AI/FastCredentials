from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Updates Sexual Harassment Prevention to 12 Modules / 15 Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Sexual Harassment Prevention')
            Lesson.objects.filter(course=course).delete()
            Question.objects.filter(course=course).delete()

            lessons = [
                {'order': 1, 'title': 'Legal Definitions & 2026 Standards', 'content': '<p>Harassment is sex-based discrimination. In 2026, this includes <strong>Gender Identity, Gender Expression, and Sexual Orientation</strong>. The law protects all employees, interns (paid or unpaid), and contractors.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Gender identity is a protected class.</div>'},
                {'order': 2, 'title': 'The "Not Petty or Trivial" Standard', 'content': '<p>Modern laws (like NY) have removed the "severe or pervasive" requirement. Harassment is now any conduct that rises above a "petty slight" or "trivial inconvenience."</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Conduct doesn’t have to be "severe" to be illegal.</div>'},
                {'order': 3, 'title': 'Quid Pro Quo (Strict Liability)', 'content': '<p>Exchanging "this for that." Employers are strictly liable for a supervisor’s actions in Quid Pro Quo cases.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Supervisors are agents of the company; their actions bind the company.</div>'},
                {'order': 4, 'title': 'Hostile Work Environment', 'content': '<p>A workplace where jokes, leering, or comments create an abusive atmosphere. Impact on the victim is the primary legal metric, not the harasser’s intent.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Intent does not excuse harassment.</div>'},
                {'order': 5, 'title': 'Retaliation & Whistleblower Rights', 'content': '<p>Punishing someone for reporting harassment is a separate illegal act. This includes demotions, "social freezing," or unfair shift changes.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Reporting is a protected activity.</div>'},
                {'order': 6, 'title': 'Bystander Intervention (The 5 Ds)', 'content': '<p>Direct, Distract, Delegate, Delay, and Document. Bystanders are critical in stopping a toxic culture before it scales.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Every employee has a duty to help maintain a safe workplace.</div>'},
                {'order': 7, 'title': 'Remote & Digital Harassment', 'content': '<p>Harassment via Slack, Zoom, or social media is still workplace harassment. Screenshots provide permanent evidence.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> The workplace exists wherever work is being discussed.</div>'},
                {'order': 8, 'title': 'Managerial "Duty to Act"', 'content': '<p>Managers who observe or are told about harassment <strong>must</strong> report it to HR. Ignorance is not a legal defense for leadership.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Managers cannot ignore "confidential" reports of harassment.</div>'},
                {'order': 9, 'title': 'External Legal Remedies (EEOC/State)', 'content': '<p>Employees have the right to file with the Federal EEOC or State Human Rights agencies. There are strict filing deadlines (statutes of limitations).</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Administrative remedies exist outside of company HR.</div>'},
                {'order': 10, 'title': 'Scenario: The "Just Joking" Defense', 'content': '<p>If a coworker repeatedly tells sexual jokes that make you uncomfortable, and you ask them to stop but they continue—that is harassment.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Consensual banter becomes harassment once it is unwelcome.</div>'},
                {'order': 11, 'title': 'Scenario: Supervisor Social Media', 'content': '<p>A supervisor "liking" or commenting on a subordinate’s swimsuit photos on Instagram can contribute to a Hostile Work Environment.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Personal social media use can impact professional liability.</div>'},
                {'order': 12, 'title': 'Investigation & Discipline', 'content': '<p>Companies must perform a "prompt and thorough" investigation. Disciplinary actions range from warnings to immediate termination.</p><div class="alert alert-info"><strong>Key Takeaway:</strong> Investigations must be impartial and documented.</div>'},
            ]
            for l in lessons: Lesson.objects.create(course=course, **l)

            qs = [
                ('What is the primary factor in determining if behavior is harassment?', ['The intent of the person doing it', 'The impact on the victim', 'The time of day it happened', 'If it was on a company laptop'], 2),
                ('Which is an example of Quid Pro Quo?', ['A raise for good work', 'A manager offering a promotion for a date', 'A coworker asking for a pen', 'Getting a new office chair'], 2),
                ('Is a company liable if a supervisor harasses a subordinate?', ['No, only the supervisor is', 'Yes, under strict liability', 'Only if the CEO knew', 'Only in California'], 2),
                ('What does Retaliation look like?', ['Extra training', 'Unfairly changing a whistleblower’s shift', 'Giving a birthday card', 'Hiring new staff'], 2),
                ('Does harassment have to be "severe or pervasive" in all states?', ['Yes, always', 'No, some states only require it to be more than a petty slight', 'Only for men', 'Only for managers'], 2),
                ('Which "D" in Bystander Intervention involves checking in with the victim later?', ['Direct', 'Delay', 'Distract', 'Delegate'], 2),
                ('Can harassment happen on Slack or Zoom?', ['No, it must be in person', 'Yes, digital harassment is legally actionable', 'Only if recorded', 'Only on company WiFi'], 2),
                ('If a manager hears a "confidential" complaint, can they keep it secret?', ['Yes, always', 'No, they have a "Duty to Act" and must report it to HR', 'Only if the victim asks', 'Only if they aren’t sure it’s true'], 2),
                ('Which group is NOT protected by harassment laws?', ['Paid interns', 'Contractors', 'Unpaid volunteers', 'Actually, all are protected'], 4),
                ('What is the "Reasonable Person" standard?', ['How the CEO would act', 'How a typical person in the victim’s shoes would perceive the behavior', 'How the harasser’s friends feel', 'How a lawyer feels'], 2),
                ('A coworker comments on your "gender expression" daily. Is this protected?', ['No, only sex is protected', 'Yes, gender expression is a protected class in 2026', 'Only if they touch you', 'Only if they are your boss'], 2),
                ('What is "Leakage"?', ['A technical bug', 'Intent to harm shared with third parties', 'Information from HR', 'Water in the office'], 2),
                ('What should you do first if you feel safe to do so?', ['Quit', 'Tell the person the behavior is unwelcome and to stop', 'Sue immediately', 'Ignore it forever'], 2),
                ('Statutes of limitations on filing a claim usually range from:', ['1 week', '180 to 300 days', '10 years', 'There is no limit'], 2),
                ('Who can create a Hostile Work Environment?', ['Only supervisors', 'Supervisors, coworkers, or even customers/vendors', 'Only people of the opposite sex', 'Only HR'], 2),
            ]
            for q, o, c in qs:
                Question.objects.create(course=course, text=q, option_1=o[0], option_2=o[1], option_3=o[2], option_4=o[3], correct_option=c)

            self.stdout.write(self.style.SUCCESS("SUCCESS: Sexual Harassment Prevention updated to 12/15 World-Class Standard."))
        except Course.DoesNotExist:
             self.stdout.write(self.style.ERROR("Course not found."))
