from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Cybersecurity Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Cybersecurity & Ransomware')
            course.questions.all().delete()

            qs = [
                ('What is "Zero Trust Architecture"?', 
                 ['A network with no security', 'The assumption that the threat is already inside; "Never Trust, Always Verify"', 'Only trusting managers', 'A network that never fails'], 2),
                
                ('How has AI changed phishing in 2026?', 
                 ['It made phishing easier to spot due to typos', 'It allows for hyper-personalized "spear-phishing" that mimics colleague tone perfectly', 'It has completely stopped phishing', 'It only targets personal emails'], 2),
                
                ('What is "Quishing"?', 
                 ['Phishing via phone call', 'Phishing via malicious QR codes', 'Phishing via physical mail', 'A type of network virus'], 2),
                
                ('What is the best defense against a Deepfake Voice Clone of your CEO?', 
                 ['Hanging up immediately', 'Using a "Shared Secret" or verbal challenge-response protocol', 'Trusting the caller ID', 'Asking for an email confirmation'], 2),
                
                ('What are "Immutable Backups" (WORM) and why are they used?', 
                 ['Backups that are easy to edit', 'Backups that cannot be altered or encrypted, preventing ransomware from locking them', 'Backups stored on paper', 'Backups that are updated every minute'], 2),
                
                ('Why are "Passkeys" more secure than traditional passwords?', 
                 ['They are longer', 'They use local biometrics and are mathematically immune to phishing', 'They are easier to remember', 'They are stored on a public server'], 2),
                
                ('What should you do if you receive an unexpected MFA push notification?', 
                 ['Approve it to clear the screen', 'Ignore it and go back to work', 'Deny the request and immediately report it to IT as a potential compromise', 'Call the bank'], 3),
                
                ('What is the risk of "Shadow AI" (unauthorized AI use)?', 
                 ['It makes work too fast', 'It can lead to irreversible confidential data leaks into public AI training sets', 'It uses too much internet bandwidth', 'It is not a real security risk'], 2),
                
                ('If you suspect your computer is breached, what is the first physical step you should take?', 
                 ['Turn off the power immediately', 'Disconnect from the network (Wi-Fi/Ethernet) but leave the power on', 'Run a virus scan', 'Call your manager on Slack'], 2),
                
                ('What is the "Principle of Least Privilege" (PoLP)?', 
                 ['Giving everyone admin access', 'Providing only the minimum access required for a person to do their job', 'A type of password policy', 'Only hiring people with low clearance'], 2),
                
                ('Why is "Tailgating" a security risk?', 
                 ['It causes traffic jams', 'It allows unauthorized physical access to secure areas by following a legitimate employee', 'It is a type of car accident', 'It only happens in parking lots'], 2),
                
                ('What is an "MFA Fatigue" attack?', 
                 ['When the user is tired of passwords', 'Spamming a user with MFA prompts until they accidentally or out of frustration click "Approve"', 'When the MFA server crashes', 'Using too many different MFA apps'], 2),
                
                ('What is "Polymorphic" malware?', 
                 ['Malware that only targets phones', 'Malware that rewrites its own code to bypass signature-based detection', 'Malware that comes from a USB drive', 'Malware that is easily deleted'], 2),
                
                ('Which part of the NIST 2.0 framework was added in 2026 to emphasize leadership responsibility?', 
                 ['Identify', 'Protect', 'Govern', 'Recover'], 3),
                
                ('What is the "Human Firewall"?', 
                 ['A physical wall in the office', 'A culture where employees are trained to own, identify, and report security anomalies', 'A team of IT experts', 'A type of software firewall'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Cybersecurity Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
