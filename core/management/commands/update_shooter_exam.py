from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Active Shooter Exam to 15-Question Tactical Standard'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Active Shooter Preparedness')
            course.questions.all().delete()

            qs = [
                ('What is the "OODA Loop" and why is it critical in a crisis?', 
                 ['A type of police siren', 'A decision-making framework (Observe, Orient, Decide, Act) to break through normalcy bias', 'A method for locking doors', 'A way to signal for help'], 2),
                
                ('When choosing to "RUN," what is the difference between Cover and Concealment?', 
                 ['There is no difference', 'Concealment stops bullets; Cover only hides you', 'Cover stops bullets (e.g., brick wall); Concealment only hides you (e.g., a bush)', 'Cover is for police; Concealment is for civilians'], 3),
                
                ('How do you effectively secure a door that opens OUTWARD?', 
                 ['Stack heavy furniture against it', 'Lock it and hope for the best', 'Tether the handle to a fixed object using a belt, cord, or wedge', 'Leave it open to see who is coming'], 3),
                
                ('What is "Normalcy Bias" in an active threat situation?', 
                 ['The tendency to stay calm', 'The brain attempting to rationalize gunshots as harmless noises like fireworks', 'Following the crowd during an evacuation', 'A psychological state of total aggression'], 2),
                
                ('When Law Enforcement arrives, what is the most important rule for your hands?', 
                 ['Keep them in your pockets for warmth', 'Keep them visible, empty, and with fingers spread wide', 'Use them to point at the shooter', 'Hold your ID card out'], 2),
                
                ('Why will the first responding officers move past injured victims without stopping?', 
                 ['They are not trained in first aid', 'They are cold and uncaring', 'Their sole priority is to neutralize the shooter to prevent more casualties', 'They are waiting for a supervisor'], 3),
                
                ('What is the primary medical intervention for a life-threatening gunshot wound to a limb?', 
                 ['Apply a vented chest seal', 'Perform CPR', 'Apply a tourniquet "High and Tight" on the limb', 'Wash the wound with soap'], 3),
                
                ('What is the purpose of a "Vented Chest Seal" for a torso wound?', 
                 ['To stop the bleeding', 'To allow air to escape the chest cavity while preventing it from entering (preventing lung collapse)', 'To keep the wound clean', 'To numb the pain'], 2),
                
                ('As a last resort, when choosing to "FIGHT," how should you act?', 
                 ['Attempt to negotiate with the attacker', 'Hide behind a desk and wait', 'Act with absolute aggression and use improvised weapons to disrupt the attacker’s OODA Loop', 'Only fight if you have a weapon'], 3),
                
                ('What is "Leakage" in the context of threat assessment?', 
                 ['A water leak in the building', 'The communication of intent to harm through social media, diaries, or verbal threats', 'Information shared by the police', 'A door left propped open'], 2),
                
                ('During a high-risk termination, when should an employee\'s digital and physical access be revoked?', 
                 ['At the end of the day', 'One week later', 'Immediately, at the exact moment the termination meeting begins', 'Only if they act angry'], 3),
                
                ('What does an "IFAK" stand for and why should you carry one?', 
                 ['Individual First Aid Kit; it contains tactical gear like tourniquets and chest seals', 'International Food and Kitchen; for emergencies', 'Instant Fire Alarm Kit; for fires', 'It is not a real term'], 1),
                
                ('Why should you NOT huddle in large groups while hiding in a room?', 
                 ['It is too loud', 'It makes it easier for a shooter to hit multiple people if they fire through a door or window', 'The police won\'t see you', 'It is better to be alone'], 2),
                
                ('In 2026, what is the "Immediate Entry" doctrine for law enforcement?', 
                 ['Officers wait for SWAT before entering', 'The first officers on the scene enter immediately to stop the threat', 'Officers surround the building and negotiate', 'Police only enter if they have a map'], 2),
                
                ('What is "Psychological First Aid" (PFA) in the aftermath of an event?', 
                 ['A formal psychiatric evaluation', 'A method of stabilizing survivors by ensuring basic needs are met and providing a calm presence', 'Forcing survivors to tell their story', 'Prescribing medication'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Active Shooter Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
