from django.core.management.base import BaseCommand
from core.models import Course, Lesson

class Command(BaseCommand):
    help = 'Completes Cybersecurity with Modules 5-12 at BBP-level depth'

    def handle(self, *args, **options):
        try:
            course = Course.objects.get(title='Cybersecurity & Ransomware')
            
            lessons = [
                {
                    'order': 5,
                    'title': 'Module 5: The Death of the Password: Passkeys and Biometrics',
                    'content': """
                        <p>In 2026, the traditional password is considered a "legacy vulnerability." Because humans naturally choose weak, predictable passwords or reuse the same credentials across multiple sites, attackers can use "Credential Stuffing" to breach thousands of accounts in seconds. The industry standard has shifted to <strong>Passkeys</strong>. Passkeys are a replacement for passwords that allow you to sign in to accounts using your device\'s local authentication—such as FaceID, TouchID, or a hardware security key. Unlike a password, a passkey is never stored on a server; it consists of a private key that remains on your device and a public key stored by the website. This architecture makes "phishing" a passkey mathematically impossible.</p>
                        <p>If you must still use passwords for legacy systems, you must follow 2026 <strong>Entropy Standards</strong>. A password is only as strong as its randomness. You should use a Password Manager to generate and store long (16+ characters), complex strings that are unique for every single account. Avoid "password aging" (forcing changes every 90 days), as this practice leads employees to create predictable patterns (e.g., Summer2026!). Instead, only change a password if there is evidence of a compromise. In 2026, a single reused password on a non-critical site (like a fitness app) is often the "Pivot Point" an attacker uses to access a corporate VPN.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Passkeys use device-level biometrics and are immune to traditional phishing attacks.</li><li>Use a Password Manager to ensure unique, high-entropy passwords for all legacy accounts.</li></ul></div>"""
                },
                {
                    'order': 6,
                    'title': 'Module 6: MFA Fatigue and Modern Bypass Tactics',
                    'content': """
                        <p>Multi-Factor Authentication (MFA) is no longer a silver bullet. In 2026, attackers utilize <strong>MFA Fatigue Attacks</strong> (also known as MFA Bombing). This involves sending dozens of push notifications to a victim\'s phone in a short period, often in the middle of the night. The attacker hopes the victim will eventually click "Approve" just to stop the noise or out of confusion. If you receive an MFA prompt that you did not personally initiate, it is a sign that your password has already been compromised. You must deny the request and immediately report the incident to IT.</p>
                        
                        <p>Another 2026 threat is <strong>AiTM (Adversary-in-the-Middle)</strong> phishing. Attackers set up a fake login page that sits between the user and the real website. When the user enters their credentials and MFA code into the fake page, the attacker captures them in real-time and uses them to log in to the real site, effectively "proxing" the session. To defend against this, organizations are moving toward <strong>Phishing-Resistant MFA</strong>, such as FIDO2 hardware keys (YubiKeys) or certificate-based authentication. These methods verify that the MFA code is only being sent to the legitimate, intended website, preventing the attacker from intercepting the token.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Never approve an MFA prompt you did not initiate; this is "MFA Fatigue."</li><li>Phishing-resistant MFA (like hardware keys) is the 2026 standard for high-security roles.</li></ul></div>"""
                },
                {
                    'order': 7,
                    'title': 'Module 7: Remote Work: Home Networks and VPNs',
                    'content': """
                        <p>The home office is the weakest link in the 2026 corporate perimeter. Most home networks utilize consumer-grade routers with "out-of-the-box" settings that are easily exploitable. To secure your remote environment, you must practice <strong>Network Segmentation</strong>. This means keeping your work laptop on a separate "Guest" Wi-Fi network, isolated from "Smart Home" devices like IoT lightbulbs, cameras, and gaming consoles, which often have poor security protocols. If an attacker breaches a vulnerable IoT device on your main network, they can use it as a "lateral move" platform to scan your work computer for vulnerabilities.</p>
                        <p>A <strong>Virtual Private Network (VPN)</strong> is mandatory for any remote work over public or home Wi-Fi. In 2026, we utilize "Always-On" VPNs that encrypt your data from the moment your computer boots. This prevents "Packet Sniffing" and "Man-in-the-Middle" attacks on untrusted networks. However, a VPN only protects the "tunnel"; it does not protect the data if your computer is already infected. You must also ensure that your home router\'s firmware is updated and that you have changed the default administrator password (often "admin/admin") to a unique, strong password to prevent unauthorized remote configuration.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Isolate work devices on a separate Guest Wi-Fi network from IoT devices.</li><li>Use an "Always-On" VPN to encrypt data when working outside the office.</li></ul></div>"""
                },
                {
                    'order': 8,
                    'title': 'Module 8: Physical Security: The Hardware Attack Surface',
                    'content': """
                        <p>Cybersecurity is not just about software; it is about the physical control of hardware. In 2026, <strong>USB-Based Attacks</strong> (Rubber Ducky/O.MG cables) have become highly sophisticated. A seemingly harmless USB cable or "lost" thumb drive can contain a hidden microprocessor that, when plugged in, emulates a keyboard and injects malicious code at 1,000 words per minute. This can disable your antivirus, install a back-door, and exfiltrate data before you even realize the device has been recognized by the computer. The rule is absolute: <strong>Never plug an untrusted device into your machine.</strong></p>
                        <p><strong>Tailgating and Piggybacking</strong> remain the primary methods for unauthorized physical access to secure facilities. This occurs when an unauthorized person follows a legitimate employee through a secure door before it closes. In 2026, attackers often dress as delivery drivers, maintenance workers, or emergency responders to exploit your natural "helper" instinct. Maintaining a professional "Badge-In" culture—where every individual must swipe their own card regardless of their role—is the only way to prevent a physical breach that could lead to direct access to servers or workstations.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Untrusted USB devices can inject malicious code instantly; never plug them in.</li><li>Stop "Tailgating" by ensuring every person swipes their own badge at every door.</li></ul></div>"""
                },
                {
                    'order': 9,
                    'title': 'Module 9: Incident Response: The First 60 Minutes',
                    'content': """
                        <p>If you suspect a breach—your mouse moves on its own, your computer is suddenly slow, or files are being renamed—your actions in the <strong>First 60 Minutes</strong> determine the severity of the loss. The most important step is to <strong>Isolate the System</strong>. In 2026, the standard advice is to disconnect from Wi-Fi or unplug the ethernet cable immediately. Do NOT turn off or "hard reboot" the computer unless instructed by IT. Shutting down the machine can wipe "volatile memory" (RAM) which contains critical forensic evidence about how the attacker got in and what they were doing.</p>
                        <p>Reporting must be immediate. Most organizations have a 24/7 Security Operations Center (SOC). You must report the "Indicator of Compromise" (IOC) through an <strong>Out-of-Band Channel</strong> (like a personal phone) because if your computer is compromised, the attacker may be watching your emails or Slack messages. Provide factual details: What did you see? When did it start? Did you click any links? An honest, fast report can allow IT to "Kill the Session" and lock down the rest of the network before the attacker can exfiltrate sensitive data or deploy ransomware.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>Disconnect from the network (Wi-Fi/Ethernet) but do not turn off the power.</li><li>Report breaches via an out-of-band channel (phone) to prevent attacker monitoring.</li></ul></div>"""
                },
                {
                    'order': 10,
                    'title': 'Module 10: Data Privacy and NIST 2.0 Governance',
                    'content': """
                        <p>Data privacy is no longer just a "best practice"; it is a legal requirement under frameworks like the GDPR, CCPA, and the <strong>2026 NIST Cybersecurity Framework 2.0</strong>. The NIST 2.0 update adds a sixth core function: <strong>Govern</strong>. This means that cybersecurity is now a "top-down" responsibility where leadership must prove they have a strategy for data lifecycle management. You must understand the <strong>Principle of Least Privilege (PoLP)</strong>: you should only have access to the specific data and systems required to perform your job. Excessive "Read/Write" access for employees who don't need it is a major risk factor during a breach.</p>
                        <p>Data must be classified based on its sensitivity: <strong>Public, Internal, Confidential, and Restricted</strong>. Personally Identifiable Information (PII)—such as social security numbers, health records, or financial data—falls under the Restricted category and must be encrypted both "At Rest" (on the hard drive) and "In Transit" (when sent via email). In 2026, sending PII via unencrypted email is a violation of federal privacy standards. Understanding these classifications ensures that the most sensitive data is protected by the strongest "Zero Trust" layers of security.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>The Principle of Least Privilege (PoLP) limits access to only what is necessary for your role.</li><li>Restricted data (PII) must always be encrypted both at rest and in transit.</li></ul></div>"""
                },
                {
                    'order': 11,
                    'title': 'Module 11: Secure Web Browsing and "Shadow AI"',
                    'content': """
                        <p>The web browser is the most targeted application in the 2026 workplace. Attackers use "Malvertising" (malicious ads on legitimate sites) and "Typosquatting" (registering a site like <i>gogle.com</i>) to infect users. You must look for the <strong>Padlock Icon (HTTPS)</strong>, but understand that in 2026, many malicious sites also use HTTPS to look "safe." Use <strong>Browser Isolation</strong> or "Sandboxing" if provided by your company, which runs the website in a separate, secure environment where it cannot touch your local files. Never save your corporate passwords in the browser\'s built-in password manager, as these are often the first targets of info-stealing malware.</p>
                        <p>A major 2026 risk is <strong>Shadow AI</strong>—the use of unauthorized AI tools (like ChatGPT, Claude, or Gemini) to process sensitive company data. If you paste a confidential client contract or a proprietary code block into a public AI tool, that data is now part of the AI\'s training set and is no longer under your company\'s control. This is a massive "Data Leakage" event. Only use AI tools that have been formally vetted and approved by IT, ensuring they have "Enterprise Privacy" settings enabled where your data is not used for training and is deleted after the session.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>HTTPS encrypts the connection but doesn't guarantee the site itself is safe.</li><li>Shadow AI (unauthorized AI use) can cause irreversible confidential data leaks.</li></ul></div>"""
                },
                {
                    'order': 12,
                    'title': 'Module 12: The Human Firewall: A Culture of Security',
                    'content': """
                        <p>The final module focuses on the transition from "Awareness" to <strong>"Ownership."</strong> A world-class cybersecurity culture is one where every employee sees themselves as a security officer. Technology will always have vulnerabilities, and attackers will always find new ways to use AI for deception, but a <strong>"Human Firewall"</strong> that is trained to spot "the unexpected" is the ultimate defense. This means having the courage to report a suspicious email even if you accidentally clicked the link. An early report is a professional act that saves the company; a hidden mistake is a disaster waiting to happen.</p>
                        <p>Cybersecurity is a <strong>Shared Responsibility</strong>. It requires "Digital Hygiene" in both your professional and personal life, as the lines between them are increasingly blurred. By maintaining the principles learned in this course—Zero Trust, MFA vigilance, Passkey adoption, and Shadow AI awareness—you protect not only the company\'s data but also the jobs and privacy of your colleagues. Security is not a "department"; it is a mindset of professional excellence. By completing this training, you are now a certified guardian of the organization\'s digital future.</p>
                        <div class="alert alert-info"><strong>Key Takeaways:</strong><ul><li>A "Human Firewall" is the most effective defense against AI-driven social engineering.</li><li>Ownership means reporting mistakes immediately to allow for rapid containment.</li></ul></div>"""
                }
            ]

            for l_data in lessons:
                Lesson.objects.create(course=course, **l_data)
            
            self.stdout.write(self.style.SUCCESS(f'SUCCESS: Cybersecurity World-Class Completion Pushed.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
