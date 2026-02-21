from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Harassment Exam to 15 World-Class Scenario Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Sexual Harassment Prevention')
            course.questions.all().delete()

            qs = [
                ('What is the 2026 standard for harassment in states like New York?', 
                 ['Conduct must be "Severe and Pervasive"', 'Conduct must be "Not Petty or Trivial"', 'Harassment is only illegal if it is physical', 'Only supervisors can harass'], 2),
                
                ('Which statement about the "Hostile Work Environment" is true?', 
                 ['It is defined by the harasser\'s intent', 'It is defined by the impact on the victim and the "Reasonable Person" standard', 'It only happens in physical offices', 'It requires at least five witnesses'], 2),
                
                ('What is "Quid Pro Quo" harassment?', 
                 ['Exchanging "this for that" (e.g., a promotion for a date)', 'Working overtime for a bonus', 'Helping a coworker with a project', 'A type of performance review'], 1),
                
                ('Under "Strict Liability," when is a company responsible for a supervisor\'s actions?', 
                 ['Only if the CEO knew', 'Automatically, if the supervisor uses their power to harass (Quid Pro Quo)', 'Only if the victim has a video', 'Only if the company has no policy'], 2),
                
                ('If a manager hears a "confidential" report of harassment, what is their duty?', 
                 ['Keep it secret as requested', 'They have a "Duty to Act" and must report it to HR immediately', 'Wait for the victim to file a formal lawsuit', 'Tell other coworkers'], 2),
                
                ('Which is an example of "Retaliation" in 2026?', 
                 ['Giving a fair but critical review for poor work', 'Excluding a whistleblower from important meetings ("Social Freezing")', 'Hiring a new employee', 'Asking an employee to work their regular shift'], 2),
                
                ('Does an employer have to protect employees from harassment by CLIENTS or VENDORS?', 
                 ['No, only employees are covered', 'Yes, employers must protect staff from third-party harassment in the workplace', 'Only if the client spends a lot of money', 'Only in California'], 2),
                
                ('Which "D" in Bystander Intervention involves checking in with the victim later?', 
                 ['Direct', 'Distract', 'Delay', 'Delegate'], 3),
                
                ('Is a "Private Message" on Slack or social media considered part of the workplace?', 
                 ['No, it is private', 'Yes, digital harassment creates a permanent legal record for the organization', 'Only if sent during work hours', 'Only if sent from a company laptop'], 2),
                
                ('What is "Intersectionality" in harassment?', 
                 ['Working in two different offices', 'Harassment based on a combination of protected traits (e.g., race and sex)', 'Being harassed by two people at once', 'A type of traffic accident'], 2),
                
                ('If a harassment claim is found to be "unsubstantiated," is the reporter still protected from retaliation?', 
                 ['No, only if they win', 'Yes, as long as the report was made in "Good Faith"', 'Only if they have a lawyer', 'Only if they are a supervisor'], 2),
                
                ('What is "Deadnaming" in the context of gender identity harassment?', 
                 ['Using a person\'s old name from before their transition', 'Forgetting someone\'s name', 'Using a nickname', 'Calling someone by their last name'], 1),
                
                ('During an investigation, what is the rule for "Interim Protections"?', 
                 ['The victim should be moved to a worse shift', 'The employer should ensure the victim is not further traumatized while the process is ongoing', 'The accused should be fired immediately without a trial', 'There are no protections'], 2),
                
                ('What is the "Ouch/Oops" framework used for?', 
                 ['Reporting a fire', 'Low-stakes, real-time correction of exclusionary behavior', 'A type of medical first aid', 'Filing a formal lawsuit'], 2),
                
                ('What is the standard for a "Prompt and Thorough" investigation?', 
                 ['It must take at least one year', 'It must be impartial, include all digital evidence, and follow-up with all witnesses', 'It only requires talking to the manager', 'It must be kept 100% secret from everyone'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Harassment Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
