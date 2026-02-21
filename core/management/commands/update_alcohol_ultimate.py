from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Alcohol Server Training to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Alcohol Server Training')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Legal Landscape: Dram Shop Liability',
                    'content': """
                        <p>In 2026, the legal responsibility of an alcohol server is defined by the principle of <strong>Duty of Care</strong>. This isn't just a professional suggestion; it is a legal mandate backed by "Dram Shop" laws. Under these statutes, a server and the establishment can be held civilly liable for damages, injuries, or deaths caused by an intoxicated patron. If you serve a "Visible Intoxicated Person" (VIP) and they later cause a fatal car accident, you—the server—can be personally sued. In 2026, courts are increasingly using "Social Host" precedents to hold even small venues to the highest standard of oversight.</p>
                        <p>Criminal liability is also at an all-time high. Serving a minor or an intoxicated person can result in heavy fines, jail time, and the immediate revocation of the establishment's liquor license. The 2026 standard for a legal defense is <strong>"Reasonable Efforts."</strong> This means you must prove that you did everything a "reasonable person" would do to prevent illegal service: you checked a valid ID, you monitored the rate of consumption, and you refused service when signs of intoxication appeared. This module establishes the technical and legal framework for these efforts, ensuring you understand that you are the first and last line of defense against alcohol-related tragedies.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Dram Shop laws hold servers personally liable for the actions of intoxicated patrons.</li><li>"Reasonable Efforts" is your primary legal defense in a liability lawsuit.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The Physiology of Alcohol and BAC Physics',
                    'content': """
                        <p>Alcohol is a central nervous system depressant that is absorbed directly into the bloodstream through the stomach (20%) and small intestine (80%). In 2026, we focus on the physics of <strong>Blood Alcohol Concentration (BAC)</strong>. A person is legally intoxicated at 0.08% BAC in most states, but impairment begins at 0.02%. Factors affecting BAC include Body Size, Gender, Food Intake, and Rate of Consumption. Because women typically have a higher percentage of body fat and less of the enzyme <i>alcohol dehydrogenase</i>, they will generally reach a higher BAC than a man of the same weight drinking the same amount.</p>
                        
                        <p>A critical 2026 focus is the <strong>"Liver Limitation."</strong> The human liver can only process approximately one "Standard Drink" per hour (about 0.015% BAC reduction). There is no way to speed this up—coffee, cold showers, and exercise do not lower BAC; only time does. One "Standard Drink" is defined as 12oz of 5% beer, 5oz of 12% wine, or 1.5oz of 80-proof spirits. In 2026, the prevalence of high-ABV (Alcohol by Volume) craft beers and cocktails means that a single pint can actually contain 2 or 3 "standard" drinks. You must be able to calculate the "True Dose" of alcohol you are serving to prevent accidental over-service.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The liver only processes about one standard drink per hour; only time lowers BAC.</li><li>High-ABV drinks must be counted as multiple standard drinks toward a patron\'s limit.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Detecting Visible Intoxication (VIP)',
                    'content': """
                        <p>In 2026, the legal standard for refusing service is <strong>Visible Intoxication</strong>. You are not a walking Breathalyzer; you are trained to look for physical and behavioral cues. These are divided into four categories: 1. <strong>Inhibitions</strong> (becoming overly friendly or loud). 2. <strong>Judgment</strong> (ordering doubles, complaining about drink strength). 3. <strong>Reactions</strong> (glassy eyes, slow speech, fumbling with money). 4. <strong>Coordination</strong> (staggering, leaning on the bar). If you notice a change in a patron\'s baseline behavior, you must begin the "Slowing Down" or "Shutting Off" protocol immediately.</p>
                        [Image showing the 4 stages of intoxication: Relaxed, Impaired, Drunk, and Danger Zone]
                        <p>A major 2026 challenge is <strong>Poly-Substance Use</strong>. Alcohol combined with prescription drugs, cannabis, or illicit substances produces a "Synergistic Effect," where 1+1=5. This means a patron may appear dangerously intoxicated after only two drinks. You must also be aware of "Tolerance"—the fact that a regular drinker may not show physical signs of coordination loss even at a high BAC. However, their <i>judgment</i> is still impaired, and you are still legally liable if you serve them. When in doubt, always prioritize safety over sales. "If they look fine but have had 5 drinks in an hour, they are NOT fine."</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Visible intoxication includes changes in speech, coordination, and judgment.</li><li>Tolerance masks physical signs, but the legal liability for over-service remains the same.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: 2026 ID Verification: Digital and Synthetic Threats',
                    'content': """
                        <p>Checking IDs in 2026 requires more than a quick glance at a birthdate. We now face <strong>Digital IDs</strong> (stored in Apple/Google Wallets) and high-quality <strong>Synthetic Fakes</strong> that can pass standard UV and barcode scans. The 2026 protocol for physical IDs is <strong>F.E.A.R.</strong>: 1. <strong>Feel</strong> (Check for raised edges or "split" laminates). 2. <strong>Examine</strong> (Look for the ghost image and state-specific holograms). 3. <strong>Ask</strong> (Ask for their zodiac sign or middle name—a fake ID holder will often hesitate). 4. <strong>Return/Refuse</strong> (If it’s fake, you have a duty to refuse service and, in some states, confiscate the ID).</p>
                        <p>For Digital IDs, you must use a verified <strong>mDL (Mobile Driver\'s License) Reader</strong>. Never just look at a screenshot or a photo of an ID on a phone; these are easily manipulated with AI. A valid Digital ID requires a secure "handshake" between the patron\'s phone and your terminal. Furthermore, you must be aware of the 2026 <strong>"Identity Theft"</strong> trend where minors use a real ID from an older sibling or friend. You must compare the physical features—the "Triangle" of the eyes, nose, and mouth—rather than just hair color or weight, which can be easily changed. If you have any doubt, ask for a second form of identification or refuse service.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Use the F.E.A.R. method for physical IDs; use verified mDL readers for digital IDs.</li><li>Compare permanent physical features (eyes/nose) to prevent "borrowed ID" fraud.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Alcohol Training Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
