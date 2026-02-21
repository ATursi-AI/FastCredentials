# FastCredentials
### AI-Powered Healthcare Compliance Credentialing Platform

🌐 **Live Site:** [fastcredentials.com](https://fastcredentials.com)

---

## What Is FastCredentials?

FastCredentials is a fully commercial web application that delivers healthcare compliance training and issues legally valid certificates — at a fraction of the cost of legacy credentialing platforms.

The platform was designed around a simple belief: **healthcare workers deserve world-class compliance training without being penalized for needing it.**

- **Free to study. Free to test. Pay only for your certificate.**
- Single certificate: **$19.99**
- Annual all-access pass: **$49.99** (unlimited certificates for 1 year)

---

## The Problem We Solve

The healthcare credentialing industry charges $50–$150+ per certificate. Most platforms are outdated, slow, and built to extract maximum revenue from workers who have no choice but to comply. When regulations change, credentials go stale with no notification.

FastCredentials fixes all of this.

---

## Key Features

### 🤖 AI Regulatory Monitoring
A live AI system pings the CDC, OSHA, and HHS APIs every 60 seconds. When federal regulations change, the platform automatically updates affected course content and notifies credentialed users by email. This is the first credentialing platform to offer real-time regulatory sync.

### 📜 Instant Certificate Generation
Users pass the exam and receive a professionally designed PDF certificate immediately. Each certificate includes a unique ID, QR code, and a public verification URL — allowing employers to verify credentials in seconds.

### 🔒 Stripe Payment Processing
Secure payment flow built with Stripe Checkout. Supports single course purchases and annual all-access passes. Includes upgrade pricing logic ($30 upgrade path for existing single-cert holders).

### 👤 Full User Authentication
Custom signup, login, password reset, and dashboard. Guest users can study and test before creating an account — reducing friction in the conversion funnel.

### ✅ Public Certificate Verification
Every certificate is publicly verifiable at `fastcredentials.com/verify/<cert_id>`. Employers can scan the QR code on any certificate to confirm authenticity instantly.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python / Django |
| Database | SQLite (production-ready for PostgreSQL migration) |
| Payments | Stripe Checkout API |
| PDF Generation | WeasyPrint |
| AI Monitoring | Feedparser + Federal Register API |
| Frontend | Bootstrap 5, custom CSS |
| Deployment | Ubuntu VPS, Nginx, Gunicorn |
| Version Control | Git / GitHub |

---

## Course Catalog

The platform currently offers 20+ courses across three compliance categories:

**Medical & Healthcare**
HIPAA Patient Confidentiality, Bloodborne Pathogens, Healthcare BLS, O.R. Protocols, Radiation Safety, Aseptic Technique, and more.

**Workplace Compliance**
Sexual Harassment Prevention, DEI in the Workplace, Cybersecurity Awareness, Active Shooter Response, Conflict Resolution, and more.

**Safety & Trade**
Forklift Safety, Food Handler Certification, Alcohol Awareness, Fire Safety, Electrical Safety, Lockout/Tagout, GHS/HazCom, and more.

---

## Certificate Validity Periods

Certificates are issued with legally accurate expiration dates per regulatory standards:

- **CPR / BLS / Basic Life Support** → 2 Years (AHA Guidelines)
- **Forklift / Food Handler / Alcohol Awareness** → 3 Years
- **All other courses** → 1 Year (OSHA/JCAHO standard)

---

## Business Model

```
User studies course       → Free
User takes exam           → Free  
User passes (100% required) → Certificate preview generated
User pays                 → Official PDF unlocked instantly
```

The 100% pass requirement ensures every credential issued represents genuine mastery — not participation.

---

## Architecture Highlights

- **Guest-to-paid funnel** — users can study and test without an account; name and course progress are preserved through signup via Django sessions
- **Annual pass logic** — single payment holders are offered a $30 upgrade path to annual access
- **Fraud prevention** — certificate names are locked at the time of exam completion; post-payment edits require support intervention
- **QR verification** — every certificate links to a live public verification endpoint

---

## Developer Note

This project was built by a non-traditional developer — a 20-year medical device sales professional who leveraged AI as a development partner to bring a genuine industry problem to market. Every product decision, business logic choice, and UX flow was driven by deep domain expertise in the healthcare compliance space.

The repository reflects a real commercial product in active development, not a tutorial or portfolio exercise.

---

## Contact

**Andrew Tursi** — Founder, FastCredentials  
📧 atursi@gmail.com  
🌐 fastcredentials.com
