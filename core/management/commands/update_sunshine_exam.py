from django.core.management.base import BaseCommand
from core.models import Course, Question

class Command(BaseCommand):
    help = 'Upgrades Sunshine Act Exam to 15 World-Class 2026 Questions'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='The Sunshine Act')
            course.questions.all().delete()

            qs = [
                ('What is the official CMS name for the program that manages Sunshine Act data?', 
                 ['Safety First', 'Open Payments', 'Clear Skies', 'The Transparency Portal'], 2),
                
                ('In 2026, which of these is considered a "Covered Recipient" under the Sunshine Act?', 
                 ['Physicians only', 'Physicians, NPs, PAs, CRNAs, and CNSs', 'Medical Students', 'Hospital Janitorial Staff'], 2),
                
                ('What is the 2026 "De Minimis" individual reporting threshold?', 
                 ['$100.00', '$13.82', '$50.00', '$5.00'], 2),
                
                ('What is the 2026 "Aggregate Rule" threshold for a single recipient?', 
                 ['$1,000.00', '$138.13', '$500.00', '$250.00'], 2),
                
                ('If you provide twenty $10 lunches to a PA in 2026, are they reportable?', 
                 ['No, because each is under $13.82', 'Yes, because the annual total exceeds $138.13', 'Only if the PA asks for them', 'Only in certain states'], 2),
                
                ('When is the 2026 "Review and Dispute" window for HCPs?', 
                 ['January 1 – February 1', 'April 1 – May 15', 'December 1 – December 31', 'Anytime during the year'], 2),
                
                ('What happens if a dispute between an HCP and a manufacturer is NOT resolved by the deadline?', 
                 ['The data is deleted', 'The data is published but marked as "Disputed"', 'The manufacturer is fined $1 million', 'The HCP is barred from the program'], 2),
                
                ('What is the 2026 maximum annual penalty for a manufacturer that "Knowingly Fails" to report?', 
                 ['$10,000', 'Over $1.45 Million', '$100,000', '$500,000'], 2),
                
                ('How are research payments for products awaiting FDA approval handled?', 
                 ['They are never reported', 'Reporting can be delayed from public view until approval or 4 years pass', 'They must be reported within 24 hours', 'They are exempt'], 2),
                
                ('What is an "Indirect Payment" under the Sunshine Act?', 
                 ['A payment made in cash', 'A transfer of value made through a third party (like a medical society) to a specific HCP', 'A payment for a generic service', 'A payment made by mistake'], 2),
                
                ('If a doctor asks you to donate their speaking fee to a charity, is it reportable?', 
                 ['No, since it is for charity', 'Yes, it is reportable as a transfer of value to that doctor (Request or Behalf)', 'Only if the charity is large', 'Only if the doctor is a surgeon'], 2),
                
                ('What specialized list does CMS publish every October for Sunshine Act reporting?', 
                 ['The Best Doctors List', 'The Mandatory Teaching Hospital List', 'The Most Expensive Devices List', 'The Whistleblower List'], 2),
                
                ('What type of interests must be reported regarding physicians and their immediate family?', 
                 ['Ownership and Investment Interests in the manufacturer', 'Their favorite vacation spots', 'Their political affiliations', 'Their home addresses'], 1),
                
                ('Are recruiting expenses (flights, meals for interviews) reportable for HCP candidates?', 
                 ['No, they are pre-employment', 'Yes, every dollar spent on a covered recipient candidate is reportable', 'Only if they are hired', 'Only if they are from out of state'], 2),
                
                ('What is the "Strictness Standard" regarding State vs. Federal laws?', 
                 ['Federal law always overrides state law completely', 'If a state law requires more data or is more restrictive than the federal act, you must follow the state law', 'You only follow federal law', 'State laws are not allowed in healthcare'], 2)
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

            self.stdout.write(self.style.SUCCESS('SUCCESS: Sunshine Act Exam upgraded to 15 World-Class questions.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
