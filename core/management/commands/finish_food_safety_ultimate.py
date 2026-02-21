from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Food Handler Safety with Modules 5-12'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Food Handler Safety')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: Receiving and Storage: The FIFO Rule',
                    'content': """
                        <p>Food safety begins at the back door. In 2026, the <strong>Receiving Protocol</strong> mandates that all TCS foods be inspected immediately upon arrival. Cold TCS foods must be received at 41°F or lower, while hot TCS foods must be 135°F or higher. A critical 2026 focus is <strong>Shellstock Tags</strong>: for clams, oysters, and mussels, you must keep the original source tag on the container until the last one is sold, and then keep that tag on file for 90 days. This allows for rapid traceability in the event of a <i>Vibrio</i> or Hepatitis A outbreak.</p>
                        <p>Once accepted, food must be stored using the <strong>First-In, First-Out (FIFO)</strong> method to ensure older inventory is used before newer stock, minimizing spoilage. Storage order in the cooler is strictly regulated by internal cooking temperatures to prevent cross-contamination from drips. The 2026 Vertical Storage Standard (Top to Bottom) is: 1. Ready-to-Eat (RTE) food. 2. Seafood. 3. Whole cuts of Beef/Pork. 4. Ground meats. 5. Whole and ground Poultry. By placing poultry at the bottom, you ensure that high-risk <i>Salmonella</i> runoff cannot contaminate lower-temperature foods.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Keep shellstock tags on file for 90 days after the last item is sold.</li><li>Store food vertically based on minimum internal cooking temperatures (Poultry on bottom).</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: Safe Thawing and Preparation',
                    'content': """
                        <p>Thawing is a high-risk activity because the exterior of the food can reach the Temperature Danger Zone while the interior is still frozen. In 2026, the FDA recognizes only <strong>Four Safe Thawing Methods</strong>: 1. In the refrigerator at 41°F or lower (the safest method). 2. Submerged under running potable water at 70°F or lower. 3. In a microwave (only if the food is cooked immediately after). 4. As part of the continuous cooking process. Thawing food on the counter at room temperature is a critical violation that allows for the rapid multiplication of pathogens.</p>
                        <p>During preparation, "Batch Prepping" is the 2026 standard for high-volume kitchens. Only take out as much food as you can prep in a short period (e.g., 30 minutes) to minimize the time food spends in the Danger Zone. For salads containing TCS ingredients (like tuna or chicken salad), the ingredients must be pre-chilled to 41°F before mixing. In 2026, we also utilize <strong>Single-Use Squeeze Bottles</strong> for condiments and dressings to prevent "Cross-Contact" during the assembly phase. Every step of preparation must be documented to prove that the "Cumulative Time" in the Danger Zone never exceeds 4 hours.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never thaw food at room temperature; use the refrigerator or running water (<70°F).</li><li>Use "Batch Prepping" to limit the time TCS foods spend in the Danger Zone.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: 2026 Internal Cooking Temperatures',
                    'content': """
                        <p>Cooking is a "Critical Control Point" because it is the stage where we use heat to reduce pathogens to safe levels. In 2026, the <strong>Minimum Internal Temperatures</strong> (maintained for 15 seconds) are: <strong>165°F</strong> for Poultry, Stuffing, and Reheated foods. <strong>155°F</strong> for Ground meats (Beef, Pork) and Injected meats. <strong>145°F</strong> for Seafood, Steaks, and Chops. <strong>135°F</strong> for Fruit, Vegetables, and Grains held for hot service. You must use a calibrated bimetallic stemmed thermometer or a digital thermocouple, inserting it into the thickest part of the food to get an accurate reading.</p>
                        
                        <p>A specific 2026 update involves <strong>Non-Continuous Cooking</strong> (Partial Cooking). If you partially cook meat to finish it later, you must have a written plan approved by the health department. The food must be heated for no more than 60 minutes initially, cooled immediately, and then cooked to its required minimum internal temperature before service. For "Highly Susceptible Populations" (the elderly, children, or those with compromised immune systems), you must never serve raw or undercooked animal proteins like rare steak or raw oysters. 165°F is the "Universal Safety" temperature that kills the most resilient 2026 pathogens.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Poultry and Reheated foods must reach 165°F. Ground meats must reach 155°F.</li><li>Use a calibrated thermometer; "visual checks" (color of juice) are not acceptable.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Holding, Service, and AI Monitoring',
                    'content': """
                        <p>Once food is cooked, it must be held at temperatures that prevent bacterial regrowth. <strong>Hot Holding</strong> must be 135°F or higher, and <strong>Cold Holding</strong> must be 41°F or lower. In 2026, many "Smart Kitchens" utilize AI-driven sensors that provide real-time alerts to the manager’s phone if a steam table or reach-in cooler fails. You must check holding temperatures at least every 4 hours; however, checking every 2 hours is recommended because it allows for "Corrective Action"—if the temperature is wrong at 2 hours, you can reheat the food and save it. If it is wrong at 4 hours, it must be thrown away.</p>
                        <p>During service, the 2026 "No-Touch" protocol protects the customer. Servers must never touch the "food-contact" surfaces of plates, glasses, or silverware. Carry plates by the bottom or edge, and carry glasses by the base or stem. Self-service areas (buffets) must be protected by <strong>Sneeze Guards</strong> and require dedicated utensils for every item to prevent cross-contamination. Customers must use a "Fresh Plate" for every return trip to the buffet. In 2026, we also emphasize "Off-Site Service" (catering) logistics, requiring insulated, food-grade containers that can maintain internal temperatures for the duration of transport.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Hold Hot food at 135°F+ and Cold food at 41°F-.</li><li>Check temperatures every 2 hours to allow for corrective action; every 4 hours is the legal limit.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Cleaning vs. Sanitizing: The 5-Step Process',
                    'content': """
                        <p>There is a technical difference between <strong>Cleaning</strong> (removing visible dirt) and <strong>Sanitizing</strong> (reducing pathogens to safe levels). You cannot sanitize a surface that is not first clean. In 2026, the <strong>5-Step Warewashing Process</strong> is the mandatory standard: 1. Scrape/Remove food bits. 2. Wash (at least 110°F). 3. Rinse. 4. Sanitize (using Heat or Chemical). 5. Air-Dry. Never use a towel to dry dishes, as this re-introduces bacteria to the sanitized surface. Food-contact surfaces must be cleaned and sanitized at least every 4 hours if they are in constant use.</p>
                        
                        <p>Chemical sanitizers in 2026 typically involve Chlorine (Bleach), Quaternary Ammonium (Quats), or Iodine. You must use a <strong>Test Kit</strong> to verify the concentration of the sanitizer. If the concentration is too low, it won't kill pathogens; if it is too high, it becomes a chemical hazard and can be toxic to customers. For high-temperature dish machines, the final sanitizing rinse must reach at least 180°F (or 165°F for stationary rack machines). By ensuring the "Time and Concentration" are correct, you maintain a "Bio-Safe" environment for food production.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Follow the 5-step process: Scrape, Wash, Rinse, Sanitize, Air-Dry.</li><li>Sanitize food-contact surfaces at least every 4 hours of continuous use.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Integrated Pest Management (IPM)',
                    'content': """
                        <p>Pests—including rodents, cockroaches, and flies—are more than a nuisance; they are biological vectors that carry <i>Salmonella</i> and other pathogens on their bodies. In 2026, we utilize <strong>Integrated Pest Management (IPM)</strong>, which focuses on prevention rather than just "spraying chemicals." The three pillars of IPM are: 1. Deny access (seal cracks, install air curtains). 2. Deny food and shelter (cleanliness, proper waste disposal). 3. Work with a licensed PCO (Pest Control Operator). If you see signs of an infestation, such as "droppings," gnaw marks, or "pepper-like" spots (roach eggs), you must report it immediately.</p>
                        <p>Waste management is a core part of IPM. Outdoor dumpsters must be kept on non-absorbent surfaces (concrete or asphalt), must have tight-fitting lids that remain closed, and must be cleaned regularly to remove "leakage" that attracts flies. Inside the kitchen, trash cans must be emptied frequently and never allowed to overflow. In 2026, "Electronic Fly Traps" (non-zapping) are the standard; they must be placed away from food prep areas to prevent dead insects from falling into the food. A single pest sighting during a 2026 health inspection can result in an immediate "Grade Pending" or closure.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>IPM focuses on denying pests access, food, and shelter.</li><li>Work only with licensed Pest Control Operators; never apply "home-use" pesticides in a kitchen.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Facility Design and "Air Gaps"',
                    'content': """
                        <p>A safe facility is built with <strong>Non-Porous, Durable Materials</strong>. In 2026, kitchen surfaces must be "Smooth and Easily Cleanable," typically using stainless steel or NSF-certified plastics. "Coving"—the curved, sealed edge between the floor and the wall—is required to prevent dirt and pathogens from hiding in sharp corners. Lighting must be bright enough to see dirt and must have "Shatter-Resistant" covers to prevent glass fragments from falling into food. Every handwashing station must be equipped with hot and cold water, soap, a waste container, and a "Signage" reminder for staff.</p>
                        <p>The most critical facility safety feature is the <strong>Air Gap</strong> in the plumbing system. An air gap is a physical space between a water outlet and the flood-level rim of a sink or drain. This prevents "Backflow"—the reverse flow of contaminated water (sewage) into the clean water supply. If a sink is "direct-connected" to a sewer line without an air gap or a backflow prevention device (like a vacuum breaker), a change in water pressure can "siphon" sewage into your prep sink. In 2026, if a "Backflow Event" occurs, the facility must be closed immediately until the water supply is tested and cleared.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Facilities must use non-porous materials and "coving" for easy cleaning.</li><li>An "Air Gap" is the only 100% reliable way to prevent sewage backflow.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: HACCP Foundations and Food Defense',
                    'content': """
                        <p>The final module focuses on <strong>HACCP (Hazard Analysis Critical Control Point)</strong>—a systematic approach to food safety. HACCP involves identifying "Critical Control Points" (CCPs) where a hazard can be prevented, eliminated, or reduced to safe levels. For example, "Cooking Poultry to 165°F" is a CCP. You must also establish "Critical Limits" (the 165°F temperature) and "Monitoring Procedures" (using a thermometer). If a critical limit is not met, you must take "Corrective Action" (e.g., continue cooking or discard). HACCP is the "Scientific Standard" for 2026 food safety.</p>
                        <p>We conclude with <strong>Food Defense</strong>. This involves protecting the food supply from intentional contamination or "bioterrorism." In 2026, the A.L.E.R.T. system is the industry standard: <strong>Assure</strong> (know your sources), <strong>Look</strong> (monitor facility security), <strong>Employees</strong> (know who is in your kitchen), <strong>Reports</strong> (keep records), and <strong>Threat</strong> (know what to do if there is a suspicion). Food safety is a team effort. By completing this training, you are now a certified guardian of the public health. Your vigilance ensures that every meal served is a safe one. Stay sharp, stay clean, and stay professional.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HACCP uses Critical Control Points (CCPs) to manage safety scientifically.</li><li>Food Defense (A.L.E.R.T.) protects the kitchen from intentional contamination.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Food Handler Safety is now World-Class.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
