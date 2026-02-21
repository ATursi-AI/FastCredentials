from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Forklift Safety to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Forklift Safety (Theory)')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: OSHA Classifications and 2026 Regulations',
                    'content': """
                        <p>Powered Industrial Trucks (PITs), commonly known as forklifts, are categorized by OSHA into seven distinct classes based on their power source and application. In 2026, understanding these classifications is vital because an operator certified on a Class I Electric Motor Rider is not legally "qualified" to operate a Class VII Rough Terrain Forklift without additional specific training. Class I-V are the most common in warehouse and industrial settings, ranging from electric sit-down riders to internal combustion trucks with pneumatic tires. OSHA 1910.178 mandates a three-part training process: Formal Instruction (this course), Practical Training (hands-on), and Evaluation of Performance. Only after all three are completed and documented can an operator be legally authorized to drive.</p>
                        <p>The 2026 regulatory environment emphasizes <strong>Telematics and Accountability</strong>. Modern forklifts are equipped with digital monitoring systems that require a unique operator badge to start. These systems track "impact events," speed violations, and the completion of pre-operational checklists. In the event of an accident, OSHA inspectors will immediately pull the telematics data to see if the operator was skipping safety steps. Furthermore, 2026 standards require a "Recertification Evaluation" every three years, or immediately following a near-miss, a workplace accident, or a change in the type of equipment being used. Safety is not a one-time badge; it is a continuous legal obligation of competence.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>OSHA divides PITs into 7 classes; certification is specific to the class of truck.</li><li>Formal training must be followed by hands-on evaluation for full certification.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: The Physics of the Stability Triangle',
                    'content': """
                        <p>A forklift is fundamentally different from an automobile; it uses a <strong>Three-Point Suspension System</strong>. Even on a four-wheel forklift, the steer axle is attached to the frame by a pivot pin in the center, creating the <strong>Stability Triangle</strong>. The three points of the triangle are the two front drive wheels and the pivot pin on the rear axle. As long as the forklift's Center of Gravity (CG) remains within this triangle, the truck will stay upright. However, once the CG shifts outside the triangle—due to a load being too heavy, too high, or the truck moving too fast during a turn—the forklift will tip over. In 2026, tip-overs remain the #1 cause of forklift-related fatalities.</p>
                        
                        <p>Load dynamics are governed by the <strong>Fulcrum Principle</strong>. The front wheels act as the fulcrum (pivot point). The weight of the truck behind the front wheels must always counter-balance the weight of the load on the forks. This is why "Load Center" is critical. Most forklifts are rated for a 24-inch load center (the distance from the face of the forks to the center of the load). If you pick up a long load that pushes the center of gravity further away from the fulcrum, the truck's lifting capacity drops significantly. In 2026, operators must be able to read the <strong>Data Plate</strong> and calculate "Capacity Deratement" when using attachments like side-shifters or carpet poles, which move the load further forward.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Stability Triangle is formed by the front wheels and the rear axle pivot pin.</li><li>The front wheels act as a fulcrum; moving the load forward reduces the truck's capacity.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Pre-Operational Inspections',
                    'content': """
                        <p>OSHA requires that every forklift be inspected at least daily, or at the beginning of every shift if the truck is used around the clock. In 2026, many of these checklists are now digital and integrated into the truck's dashboard. A pre-operational inspection is divided into two parts: <strong>The Visual (Static) Check</strong> and <strong>The Operational (Dynamic) Check</strong>. During the visual check, you are looking for structural integrity: hydraulic leaks, frayed hoses, cracked fork blades, and tire condition (looking for "chunking" or flat spots). You must also check fluid levels (coolant, oil, hydraulic) and ensure the battery cables are not frayed or corroded.</p>
                        <p>The operational check involves starting the engine (or powering on the motor) and testing the mechanical functions. This includes the lift and tilt mechanisms, the steering (checking for "play"), the horn, and most importantly, the <strong>Braking and Inching Systems</strong>. If any safety-critical item is found to be defective—such as a non-functioning horn, a hydraulic leak, or a missing data plate—the truck must be "Red Tagged" and removed from service immediately. It is illegal and highly dangerous to operate a forklift with a known safety deficiency. In 2026, "I thought it was fine for one more move" is the most common quote found in accident reports.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Inspections must be performed before every shift; report all defects immediately.</li><li>A forklift with a safety-critical defect must be "Red Tagged" and taken out of service.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Load Handling and Mast Mechanics',
                    'content': """
                        <p>Handling a load safely requires a precise sequence of actions. When approaching a load, ensure the forks are level and spaced wide enough to support the weight evenly. Drive into the pallet until the load is flush against the backrest (carriage). Before lifting, ensure the path above is clear of obstructions like fire sprinklers or overhead lights. Once the load is cleared from the rack or stack, <strong>Tilt the Mast Back</strong>. Tilting the mast back moves the Center of Gravity toward the center of the Stability Triangle, increasing the truck's stability. Never travel with a load raised higher than 4 to 6 inches from the floor.</p>
                        
                        <p>High-tier racking in 2026 requires specialized awareness of <strong>"Visibility and Mast Drift."</strong> When a load is 20-30 feet in the air, a small movement at the base is magnified. You must never turn the forklift while the load is elevated. This is because the centrifugal force of the turn will easily pull the Center of Gravity outside the Stability Triangle, causing a lateral tip-over. When placing a load, use the "Inching Pedal" (on internal combustion trucks) to control speed precisely while keeping the engine RPMs high enough to power the hydraulics. Once the load is securely in the rack, level the forks and back out straight before lowering the mast to the travel position.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Always tilt the load back before traveling to stabilize the Center of Gravity.</li><li>Never turn the forklift while the load is elevated; this causes lateral tip-overs.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Forklift Part 1 pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
