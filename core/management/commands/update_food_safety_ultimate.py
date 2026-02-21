from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Food Handler Safety to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Food Handler Safety')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 FDA Food Code and Regulatory Landscape',
                    'content': """
                        <p>Food safety is a public health mandate governed by the 2026 FDA Food Code and local health departments. In the United States, an estimated 48 million people suffer from foodborne illnesses annually. In 2026, the regulatory focus has shifted from "reactive" inspections to <strong>Active Managerial Control (AMC)</strong>. This means that food handlers are no longer just followers of rules; they are active participants in identifying and mitigating risks before they cause an outbreak. Understanding the "Big Six" pathogens—Norovirus, Hepatitis A, Shigella, Salmonella Typhi, Nontyphoidal Salmonella, and Shiga toxin-producing E. coli (STEC)—is the first requirement for any professional food handler.</p>
                        <p>The 2026 landscape also emphasizes <strong>Transparency and Traceability</strong>. Modern food handlers must understand the "Chain of Custody" for ingredients, especially with the rise of global supply chains. If a contaminated batch of leafy greens enters a kitchen, the handler must be able to identify the source and isolate the product within minutes. Regulatory compliance now includes digital temperature logs and AI-assisted shelf-life monitoring. As a certified food handler, you are the final barrier between a safe meal and a life-threatening illness. This module establishes the legal and ethical framework for that responsibility.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The "Big Six" pathogens are the leading causes of foodborne illness.</li><li>Active Managerial Control means proactively identifying risks before they occur.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Bio-engineered Allergens and Cross-Contact',
                    'content': """
                        <p>In 2026, the "Big Nine" allergens—Milk, Eggs, Fish, Crustacean Shellfish, Tree Nuts, Peanuts, Wheat, Soy, and Sesame—remain the primary focus, but we now address <strong>Bio-engineered and Synthetic Allergens</strong> found in lab-grown proteins. A food allergy is an immune system response to a specific protein, and in some cases, even a microscopic trace can trigger anaphylaxis. You must distinguish between a food allergy and a food intolerance (like lactose intolerance). While both are uncomfortable, only the allergy is potentially fatal. The 2026 standard for allergen safety is <strong>Zero Cross-Contact</strong>.</p>
                        
                        <p>Cross-contact occurs when allergens are transferred from one food or surface to another. This is different from cross-contamination (which involves pathogens). To prevent cross-contact, you must use purple-coded equipment (knives, cutting boards, and tongs) specifically reserved for allergen-safe preparation. In 2026, "Hidden Allergens" are a major concern; handlers must read labels for every single ingredient, as manufacturers frequently change formulations. If a customer informs you of an allergy, the "Chain of Communication" must be absolute: from the server to the chef to the individual preparer, ensuring that the meal is prepared in a sanitized "Safe Zone" of the kitchen.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Cross-contact involves the transfer of proteins/allergens; use dedicated equipment.</li><li>Always treat a food allergy as a potential medical emergency (anaphylaxis).</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Personal Hygiene and the 2026 Handwashing Science',
                    'content': """
                        <p>Personal hygiene is the #1 defense against <strong>Norovirus</strong>, which is the leading cause of foodborne illness and is almost exclusively spread by the fecal-oral route. In 2026, "Double Handwashing" is required after using the restroom: once in the restroom sink and a second time at the dedicated handwashing station in the kitchen. Handwashing must follow the 20-second rule: 1. Wet hands with warm water (at least 100°F). 2. Apply soap. 3. Scrub vigorously for 10-15 seconds (including under nails and up the forearms). 4. Rinse thoroughly. 5. Dry with a single-use paper towel. You must use the towel to turn off the faucet to avoid re-contaminating your clean hands.</p>
                        
                        <p>The "No Bare Hand Contact" rule for Ready-to-Eat (RTE) foods is strictly enforced in 2026. Handlers must use gloves, tongs, or deli paper when handling food that will not be further cooked. However, <strong>gloves are not magic</strong>; they can harbor more bacteria than skin if not changed frequently. You must change gloves if they are torn, when changing tasks (moving from raw to cooked), or every 4 hours of continuous use. Furthermore, 2026 standards prohibit jewelry (except a plain wedding band) and require hair restraints and beard nets. If you are sick with vomiting, diarrhea, jaundice, or a sore throat with fever, you have a legal <strong>Duty to Report</strong> and must be excluded from the kitchen.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Norovirus is the #1 cause of illness; handwashing is the primary defense.</li><li>Glove changes are mandatory every 4 hours or when changing tasks.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Time and Temperature Control (TCS) Physics',
                    'content': """
                        <p>Bacteria require specific conditions to grow: Food, Acidity, Temperature, Time, Oxygen, and Moisture (<strong>FAT TOM</strong>). In 2026, we focus on <strong>TCS Foods</strong> (Time/Temperature Control for Safety), which include meat, dairy, cooked plant foods, and untreated garlic-and-oil mixtures. The <strong>Temperature Danger Zone (TDZ)</strong> is between 41°F and 135°F. Within this range, bacteria like <i>Salmonella</i> can double every 20 minutes. If a TCS food remains in the danger zone for more than 4 hours, it must be discarded—no exceptions. In 2026, "High-Speed Bacteria" variants require even tighter adherence to cooling and reheating protocols.</p>
                        
                        <p>Cooling food is the most dangerous stage in the TCS cycle. You must move food through the danger zone as fast as possible using the <strong>Two-Stage Cooling Method</strong>: from 135°F to 70°F within 2 hours, and then from 70°F to 41°F within the next 4 hours (total of 6 hours). To achieve this, use ice-water baths, blast chillers, or stir food with ice paddles. Never place a large, deep pot of hot soup directly into the walk-in cooler; the "Core Temperature" will stay in the danger zone for hours, allowing for the growth of <i>Clostridium perfringens</i>. 2026 standards mandate the use of digital thermocouples to verify internal temperatures at the thickest part of the food.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Temperature Danger Zone is 41°F to 135°F.</li><li>Use the Two-Stage Cooling method to move food through the Danger Zone safely.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Food Safety Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
