from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Alcohol Exam to 15 World-Class Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Alcohol Server Training')
            course.questions.all().delete()

            qs = [
                ('What is "Dram Shop Liability" in 2026?', 
                 ['The cost of a drink', 'The legal responsibility of a server/venue for damages caused by an intoxicated patron', 'A type of tax on alcohol', 'A rule about bar snacks'], 2),
                
                ('What is the only factor that lowers Blood Alcohol Concentration (BAC)?', 
                 ['Drinking black coffee', 'A cold shower', 'Time', 'Vigorous exercise'], 3),
                
                ('How many "Standard Drinks" are in a 16oz craft beer with 10% ABV?', 
                 ['One drink', 'Approximately two to three standard drinks', 'It doesn\'t count if it\'s a beer', 'Half a drink'], 2),
                
                ('Which is an example of "Visible Intoxication" (VIP)?', 
                 ['Ordering a water', 'A change in behavior, such as becoming overly loud or fumbling with money', 'Paying with a credit card', 'Wearing a hat'], 2),
                
                ('What is the "Synergistic Effect" in 2026?', 
                 ['The taste of a cocktail', 'When alcohol is combined with other substances, making the impairment much worse (1+1=5)', 'A type of sparkling wine', 'Mixing different types of beer'], 2),
                
                ('What does the "R" stand for in the F.E.A.R. ID verification method?', 
                 ['Read the name', 'Return or Refuse', 'Report to police', 'Run the card'], 2),
                
                ('How should you verify a 2026 Digital ID (mDL)?', 
                 ['Look at a screenshot on the phone', 'Use a verified mDL Reader terminal', 'Ask the patron to recite their address', 'Digital IDs are not legal'], 2),
                
                ('What is an "I Statement" in tactical communication?', 
                 ['"I think you are too drunk"', '"I feel that I have served you enough for tonight"', '"I am going to call the cops"', '"I hate my job"'], 2),
                
                ('Why should you document a refusal of service in the digital logbook?', 
                 ['To show the boss how much you work', 'To provide a "Reasonable Efforts" defense in a future Dram Shop lawsuit', 'To track tips', 'It is not necessary'], 2),
                
                ('What is an "Angel Shot" protocol used for?', 
                 ['A free drink for regulars', 'A safe-word signal for a patron who feels threatened or harassed', 'A type of high-alcohol shooter', 'A way to order water'], 2),
                
                ('Which food type is BEST for slowing the absorption of alcohol?', 
                 ['High-protein and high-fat items (burgers, cheese)', 'Salty snacks (pretzels, peanuts)', 'Sugary desserts', 'Soup'], 1),
                
                ('In a law enforcement "Sting" operation, what is "Strict Liability"?', 
                 ['You only get in trouble if you meant to break the law', 'You are guilty if you serve a minor, regardless of your intent or "guess"', 'The manager is the only one responsible', 'The minor is the only one in trouble'], 2),
                
                ('What is a "Unified Front" in a house policy?', 
                 ['The way the bar is decorated', 'Ensuring no staff member serves a patron who has already been cut off by another staff member', 'Wearing the same uniform', 'All staff members taking lunch at the same time'], 2),
                
                ('Who is liable if an alcohol delivery is handed to a minor at their house?', 
                 ['Only the delivery driver', 'Only the restaurant', 'Liability is shared between the venue and the driver', 'No one is liable'], 3),
                
                ('What is "Thermal Runaway" in the context of a 2026 bar (e.g., mobile POS systems)?', 
                 ['A patron running away without paying', 'A Lithium-Ion battery fire chain-reaction', 'The refrigerator breaking', 'A heated cocktail'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Alcohol Server Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
