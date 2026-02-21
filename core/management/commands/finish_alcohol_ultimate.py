from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Alcohol Server Training with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Alcohol Server Training')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: The Art of Refusal: Tactical Communication',
                    'content': """
                        <p>Refusing service to an intoxicated patron is the most challenging part of the job. In 2026, we utilize <strong>De-escalation Communication</strong> to maintain safety. The goal is to be "Firm but Fair." When cutting someone off, never use accusatory language like "You're drunk." Instead, use "I" statements: "I feel that I've served you enough for tonight," or "I'm concerned about your safety, so I'm going to stop serving you alcohol." By making it about your professional responsibility and the law, you depersonalize the conflict.</p>
                        <p>Timing and teamwork are essential. Always notify your manager and security <em>before</em> you approach the patron to ensure you have "Backup." Once you have refused service, you must remove the glass from the patron's reach. In 2026, we also emphasize <strong>Alternative Service</strong>: offering the patron food, water, or a non-alcoholic beverage on the house. This transition helps move the patron toward leaving the establishment without a confrontation. If the patron becomes aggressive, do not engage; step back and let security handle the physical removal while you document the incident.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use "I" statements to depersonalize the refusal of service.</li><li>Always have a manager or security as backup before "cutting off" a patron.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: 2026 Incident Documentation: The Digital Log',
                    'content': """
                        <p>In a 2026 Dram Shop lawsuit, your best defense is a contemporaneous <strong>Incident Log</strong>. If you cannot prove what happened, the court will assume the worst. Every time you refuse service, check a suspicious ID, or handle a physical altercation, you must record it in the establishment's digital logbook. This record must include: 1. The Date and Time. 2. A description of the patron (and their name if known). 3. The specific "Visible Signs of Intoxication" you observed. 4. The names of witnesses or staff involved. 5. The final outcome (e.g., "Patron left in an Uber").</p>
                        <p>Why is this critical? Most lawsuits occur 1-2 years after the event. You will not remember the details of "that one Tuesday night" unless it is written down. In 2026, many Point of Sale (POS) systems have integrated <strong>Incident Triggers</strong> that prompt you to fill out a digital form if you void a drink for intoxication. These logs are legal documents that prove you were exercising "Reasonable Efforts" to follow the law. Failing to document a refusal is a major liability gap that can lead to a "Default Judgment" against the establishment.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Document every refusal of service immediately in the digital logbook.</li><li>Detail specific behaviors (staggering, slurring) rather than just saying "they were drunk."</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Bystander Intervention and Drink Spiking',
                    'content': """
                        <p>In 2026, the role of the alcohol server includes <strong>Active Bystander Intervention</strong> for sexual assault prevention. Establishments are now legally and ethically responsible for the safety of their patrons from third-party predators. This includes monitoring for <strong>Drink Spiking</strong> (using substances like GHB or Ketamine). Signs of a "spiked" drink include a patron becoming suddenly and disproportionately incapacitated after a small amount of alcohol. If you see an unattended drink, or if a patron appears to be "targeting" someone who is clearly impaired, you have a professional <strong>Duty to Intervene</strong>.</p>
                        <p>Many 2026 venues utilize the <strong>"Angel Shot"</strong> or similar "Safe Word" protocols. If a patron asks for a specific drink name that doesn't exist, it is a signal that they feel unsafe. Your response should be to move the patron to a secure area (the office or kitchen) and call them a ride or notify the police. Training your staff to recognize "Predatory Grooming" behavior—such as a patron isolating someone or buying multiple rounds for a stranger who is already VIP—is the mark of a world-class, safe establishment. Safety is the primary product you sell, not just the beverage.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Monitor for signs of "spiking": sudden, extreme impairment.</li><li>Implement "Safe Word" protocols (like the Angel Shot) to help patrons in danger.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Tactical Service: Food and Water',
                    'content': """
                        <p>As a server, you can influence the rate of a patron's intoxication through <strong>Tactical Service</strong>. Because 80% of alcohol is absorbed in the small intestine, anything that keeps alcohol in the stomach longer will slow down the BAC rise. <strong>Food</strong>—especially high-fat and high-protein items—slows the "gastric emptying" process. In 2026, offering "Appetizer Specials" to a fast-drinking table is a legal defense strategy. Avoid salty snacks (peanuts, pretzels), as these increase thirst and lead to faster alcohol consumption.</p>
                        <p><strong>Hydration</strong> is the second pillar of tactical service. For every alcoholic drink served, you should provide a glass of water. This not only slows the pace of drinking but also helps prevent the severe dehydration that contributes to "blackouts." In 2026, "Auto-Refill Water" is a standard house policy in responsible venues. If a patron is nearing the "Impairment" zone, you should slow down your service frequency—checking the table less often or taking longer to return with the next round. This is a subtle, non-confrontational way to manage the room's safety.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Fatty/Protein-rich foods slow alcohol absorption; salty foods increase it.</li><li>Always provide water with every alcoholic drink to slow the rate of consumption.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Minors and "Sting" Operations',
                    'content': """
                        <p>Selling alcohol to a minor is a "Strict Liability" offense. This means it doesn't matter if you "thought" they were 21; if they are 20, you have broken the law. In 2026, local law enforcement and the ABC/LCB conduct frequent <strong>"Sting" Operations</strong> using "Minor Decals"—underage individuals who look 21 but carry their real (underage) ID. If you fail to check the ID or misread the birthdate during a sting, the consequences are immediate: a criminal citation for you and a "Notice of Violation" for the house.</p>
                        <p>To survive a 2026 sting, you must follow the <strong>"Calculate, Don't Guess"</strong> rule. Use the "Born On or Before" date posted at your station. In 2026, many IDs are "Vertical" for minors and "Horizontal" for adults. However, you must still check the date, as a minor may have recently turned 21 but hasn't updated their physical card yet. Be aware of <strong>Third-Party Sales</strong> (shoulder-tapping): if an adult buys two drinks and hands one to a person who looks underage at a table, you must intervene and check the second person's ID immediately. Ignorance is never a legal defense.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Selling to a minor is a "Strict Liability" crime; your intent does not matter.</li><li>Watch for "Third-Party Sales" where an adult passes a drink to a minor.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: House Policies and the "Unified Front"',
                    'content': """
                        <p>A "House Policy" is a set of rules that goes beyond the law to ensure the safety of the venue. In 2026, world-class venues have written policies on <strong>Drink Limits</strong> (e.g., no more than two doubles per hour) and <strong>Last Call</strong> procedures. For a policy to be effective, there must be a <strong>Unified Front</strong>. If a server cuts off a patron, but a different server (or the manager) serves them ten minutes later, the establishment has just created a massive legal liability. This "Second Service" proves that the house was aware of the intoxication and chose to ignore it for profit.</p>
                        <p>Effective 2026 house policies also include <strong>Transportation Assistance</strong>. If a patron is too impaired to drive, the house should facilitate a ride-share (Uber/Lyft). In some jurisdictions, the house may even be required to pay for the ride to ensure the patron doesn't get behind the wheel. You must never "force" an intoxicated person to drive away just to get them off the property; this is legally considered "Increasing the Risk." By having a clear, written policy that every staff member follows, you protect the license and the lives of the community.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A "Unified Front" means no staff member overrules a refusal of service by another.</li><li>Never force an intoxicated person to drive; facilitate a safe ride home.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: 2026 Third-Party Delivery Liability',
                    'content': """
                        <p>The 2026 alcohol market is dominated by <strong>Third-Party Delivery</strong> (UberEats, DoorDash, etc.). This has created a "Secondary Liability" zone. When you hand a "to-go" margarita or a bottle of wine to a delivery driver, who is responsible if the end-customer is a minor or already intoxicated? In 2026, the law is clear: <strong>The liability is shared</strong>. The establishment must ensure the container is "Tamper-Evident" (sealed with a specialized sticker), and the delivery driver must be trained to perform an ID check at the door.</p>
                        <p>As a server, you must also check the <strong>Driver's Sobriety</strong>. If a DoorDash driver arrives and appears intoxicated, you must refuse to hand over the alcohol and report the driver to the platform. In 2026, "Ghost Kitchens" and restaurants are being sued for "Negligent Fulfillment" if they send alcohol out with a driver who is clearly impaired. You are the "Gatekeeper" of the alcohol from the moment it leaves the bar until it is handed to a verified, sober adult. This module covers the specific documentation required for "To-Go" alcohol sales to maintain compliance.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Liability for delivery alcohol is shared between the venue and the driver.</li><li>Refuse to hand alcohol to a delivery driver who appears intoxicated.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: Professionalism and Alcohol Mental Health',
                    'content': """
                        <p>The final module addresses the <strong>Human Element</strong> of the industry. In 2026, we recognize that the hospitality industry has high rates of substance use disorders. Being a "Responsible Server" starts with your own relationship with alcohol. Professionalism means maintaining a clear boundary between "Work" and "Socializing." In 2026, "Shift Drinks" are being phased out in many elite venues to ensure that staff remain sharp and capable of handling emergencies until the moment they clock out.</p>
                        <p>We conclude with <strong>Personal Resilience</strong>. Dealing with intoxicated, sometimes aggressive patrons is emotionally taxing. A world-class professional knows how to "leave it at the door" and utilizes the establishment's Employee Assistance Programs (EAP) if needed. By completing this certification, you have proven that you are not just a "pourer" of drinks, but a trained professional with the technical, legal, and social skills to manage a high-risk environment safely. Your vigilance saves lives. Stay professional, stay legal, and stay safe.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Professionalism requires clear boundaries between work and personal alcohol use.</li><li>Completing this training makes you a certified guardian of the public safety.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Alcohol Server Training is now World-Class.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
