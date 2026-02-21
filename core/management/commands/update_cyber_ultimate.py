from django.core.management.base import BaseCommand
from core.models import Course, Lesson, Question

class Command(BaseCommand):
    help = 'Upgrades Cybersecurity & Ransomware to 12 Deep-Dive World-Class Modules'

    def handle(self, *args, **options):
        try:
            course, created = Course.objects.get_or_create(title='Cybersecurity & Ransomware')
            course.lessons.all().delete()
            course.questions.all().delete()

            lessons = [
                {
                    'order': 1,
                    'title': 'Module 1: The 2026 Threat Landscape: AI-Driven Adversaries',
                    'content': """
                        <p>In 2026, the cybersecurity landscape has shifted from human-led attacks to <strong>Machine-Speed Adversaries</strong>. Cybercriminals now utilize Generative AI and Agentic AI to automate every phase of an attack, from initial reconnaissance to data exfiltration. Unlike traditional threats, which often contained spelling errors or generic language, 2026 attacks are hyper-personalized. AI agents can scan your social media, LinkedIn, and company website to craft a "spear-phishing" lure that perfectly mimics the tone, jargon, and specific projects of your colleagues. This has resulted in a 54% click-through rate for AI-generated phishing, compared to just 12% for traditional methods.</p>
                        <p>The "barrier to entry" for hackers has effectively vanished. Crimeware-as-a-Service (CaaS) platforms now allow low-skilled actors to deploy sophisticated, self-mutating malware that can bypass traditional antivirus software. These "Polymorphic" threats rewrite their own code every time they infect a new machine, making "signature-based" detection obsolete. To survive in this environment, an organization must transition from a "perimeter-based" security model to a <strong>Zero Trust Architecture</strong>. Zero Trust operates on the principle of "Never Trust, Always Verify," assuming that the threat is already inside the network.</p>
                        <p>This module establishes the core reality of modern cyber defense: the human is the primary attack surface. While technical firewalls are essential, the "Human Firewall"—the ability of an employee to recognize and report a sophisticated anomaly—is the only defense against AI-led social engineering. We will explore the "Cyber Kill Chain" and explain how early detection in the first 15 seconds of an interaction can prevent a multi-million dollar data breach. By the end of this course, you will have the technical intelligence to identify the invisible digital threats of 2026.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>AI-driven attacks are hyper-personalized and bypass traditional spam filters.</li><li>Zero Trust means "Never Trust, Always Verify," assuming the network is already breached.</li></ul></div>"""
                },
                {
                    'order': 2,
                    'title': 'Module 2: Social Engineering: Beyond the Email',
                    'content': """
                        <p>Social engineering is the art of manipulating people into divulging confidential information or performing actions that compromise security. In 2026, this has expanded far beyond simple email phishing. We now face a "Multi-Channel" threat landscape. <strong>Smishing</strong> (SMS Phishing) utilizes text messages that appear to be from your bank, HR department, or a delivery service, often including an "urgent" link that installs a mobile trojan. <strong>Vishing</strong> (Voice Phishing) uses AI-generated scripts to conduct fraudulent phone calls, often spoofing a known company number to build immediate trust.</p>
                        
                        <p>A rapidly growing 2026 threat is <strong>Quishing</strong> (QR Code Phishing). Attackers place malicious QR codes in public places—on restaurant menus, parking meters, or even in "safety" emails—that, when scanned, redirect your mobile browser to a credential-harvesting site. Because humans are conditioned to trust QR codes for convenience, this method bypasses the mental filters we use for emails. Another tactic is <strong>Pretexting</strong>, where an attacker creates a fabricated scenario (a fake "security audit" or "IT update") to trick you into providing your Multi-Factor Authentication (MFA) code or temporary password.</p>
                        <p>To defend against social engineering, you must recognize the <strong>Psychological Triggers</strong> used by attackers: Urgency, Authority, and Fear. If an interaction forces you to "act now or lose access," it is likely a scam. In 2026, the gold standard for defense is <strong>Out-of-Band Verification</strong>. If you receive a suspicious request from your "boss" on Slack, do not reply on Slack. Instead, call them on their known phone number or use a separate communication channel to verify the request. Never click a link or provide a code based on a single incoming message, no matter how authentic it looks.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Smishing (SMS) and Quishing (QR codes) are the fastest-growing 2026 threats.</li><li>Always use "Out-of-Band Verification" to confirm suspicious requests from authority figures.</li></ul></div>"""
                },
                {
                    'order': 3,
                    'title': 'Module 3: Deepfakes and Digital Impersonation',
                    'content': """
                        <p>Deepfake technology—the use of AI to create hyper-realistic video and audio of real people—is no longer a theoretical risk; it is a primary tool for 2026 Business Email Compromise (BEC). In <strong>Real-Time Voice Cloning</strong>, an attacker only needs a 30-second clip of your CEO’s voice (from a YouTube video or podcast) to create an AI model that can speak in their exact tone and cadence. They can then call a member of the finance team, appearing as the CEO, and authorize an "urgent" wire transfer. The realism of these clones is high enough to fool even close family members, let alone colleagues in a high-stress work environment.</p>
                        <p>Video Deepfakes are also being utilized in "Virtual Meetings." Attackers can now join Zoom or Teams calls using a real-time AI overlay that mimics a high-level executive’s face and movements. While these overlays sometimes have subtle "glitches"—such as unnatural eye blinking or blurring around the edges of the face—they are increasingly difficult to detect during standard business interactions. This technology is often used to "onboard" fake employees or to trick HR into changing the direct deposit information for a real executive. In 2026, "seeing is no longer believing" in the digital workspace.</p>
                        <p>The defense against digital impersonation is the <strong>"Shared Secret" or Challenge-Response Protocol</strong>. For high-value transactions or sensitive data access, teams must implement a non-digital verification step. This might involve a verbal password that is never stored in an email or a specific question that only the real person would know. Inclusive of this is <strong>Media Literacy</strong>: training employees to look for "AI Artifacts" like mismatched lighting, robotic speech rhythms, or a lack of emotional nuance in high-pressure requests. If a "Video Call" from your boss feels slightly "off," ask them a question that requires a specific, personal memory to verify their identity.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>AI can clone a voice or face in real-time to impersonate executives.</li><li>Use "Shared Secrets" (non-digital verbal passwords) to verify high-value requests.</li></ul></div>"""
                },
                {
                    'order': 4,
                    'title': 'Module 4: Ransomware 5.0: The Autonomous Threat',
                    'content': """
                        <p>Ransomware has evolved from a simple "lock and key" virus into <strong>Ransomware 5.0</strong>, a multi-stage extortion ecosystem. In 2026, ransomware is "Autonomous," meaning the malware can navigate your network, identify your most sensitive data, and exfiltrate it to the dark web without any human intervention. We are now seeing "Triple Extortion" tactics: 1. Your files are encrypted (locking you out), 2. Your sensitive data is threatened with public release (reputational risk), and 3. The attacker contacts your clients or investors to tell them their data has been stolen (external pressure).</p>
                        <p>A primary target of Ransomware 5.0 is your <strong>Backup Repositories</strong>. Attackers know that if you have a clean backup, you won't pay the ransom. Therefore, the malware is designed to stay "dormant" in your system for weeks, infecting your backups before it ever triggers the encryption. This is known as "Dwell Time." In 2026, the only defense against this is <strong>Immutable Backups</strong>—data backups that are "Write Once, Read Many" (WORM). Once written, these backups cannot be altered, deleted, or encrypted by the ransomware, providing a "clean room" for recovery after an attack.</p>
                        <p>If your organization is hit by ransomware, the 2026 legal and ethical standard is <strong>"Never Pay."</strong> Paying a ransom does not guarantee the return of your data, and it directly funds the development of even more sophisticated AI-driven malware. Furthermore, many insurance carriers in 2026 will no longer cover ransom payments if the organization cannot prove they had "Reasonable Security Controls" in place. Your focus must be on <strong>Resilience</strong>: the ability to detect the intrusion in the early "Reconnaissance" phase and having a practiced Incident Response Plan that allows you to restore operations from immutable backups without paying the criminals.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Ransomware 5.0 uses "Triple Extortion" to pressure organizations into paying.</li><li>Use Immutable Backups (WORM) to ensure you can recover without paying a ransom.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Cybersecurity Part 1 (1-4) pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
