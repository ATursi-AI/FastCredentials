import os
import django
import anthropic
import random
import json
from django.utils.text import slugify
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from core.models import BlogPost

TOPICS = [
    # Original 16
    "What is HIPAA compliance and who needs it",
    "OSHA bloodborne pathogen standards explained",
    "Why CPR certification matters in the workplace",
    "How to stay compliant with changing healthcare regulations",
    "The importance of fire safety training in healthcare",
    "What is OSHA and why does it matter for employers",
    "Healthcare worker safety training requirements 2026",
    "How AI is changing compliance training forever",
    "Why annual compliance training is not enough anymore",
    "The cost of non-compliance for healthcare organizations",
    "The tattoo shop mistake that could end your career overnight",
    "Why forklift operators are getting fired for skipping this one certification",
    "HIPAA violations that cost healthcare workers their jobs in 2026",
    "The 10-minute safety training that saved a nurse's career",
    "What happens when OSHA shows up unannounced at your facility",
    "Food handler certification: the $10,000 mistake restaurants keep making",
    # Expanded — medical and healthcare
    "BLS vs ACLS vs PALS: which certification does your healthcare role actually need",
    "Why aseptic technique training is non-negotiable for surgical staff",
    "Radiation safety in healthcare: what every tech and nurse needs to know",
    "Operating room protocols that prevent never-events",
    "The Sunshine Act explained for medical device reps",
    "AdvaMed code of ethics: what field reps get wrong",
    "How often do you really need to renew your BLS certification",
    "Why HIPAA training fails and how to fix it",
    "Bloodborne pathogens: the exposure incident no one talks about",
    "What hospitals look for in a compliant new hire",
    # Expanded — workplace compliance
    "Cybersecurity awareness for healthcare: what HICP 405(d) requires",
    "Sexual harassment prevention training: what is actually mandatory in your state",
    "DEI training that actually works versus checkbox compliance",
    "Active shooter response: the 3 steps every employee must know",
    "Conflict resolution in high-stress healthcare environments",
    "How to handle a workplace compliance audit without panicking",
    "The difference between training records that pass audits and those that fail",
    "Why your workplace compliance program is probably out of date",
    # Expanded — safety and trade
    "Lockout tagout (LOTO): the procedure that saves lives",
    "GHS and HazCom: what every worker handling chemicals must know",
    "Electrical safety: NFPA 70E and why it matters beyond electricians",
    "Slips, trips, and falls: the #1 preventable workplace injury",
    "Fire extinguisher training: PASS method explained",
    "Alcohol awareness certification: bartender's guide to avoiding liability",
    "Food handler card requirements by state: a 2026 guide",
    "Forklift certification myths that could cost you your job",
    # Expanded — business and industry
    "The real ROI of compliance training for small healthcare practices",
    "Why buying compliance certificates online is not a shortcut",
    "How credentialing platforms are disrupting a broken industry",
    "The hidden cost of outdated compliance content",
    "Why AI-monitored regulatory updates are the future of compliance",
]

def generate_post(topic):
    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    prompt = f"""Write a professional SEO-optimized blog post for FastCredentials.com about: {topic}
Requirements:
- Title: compelling, under 60 characters, includes primary keyword
- Meta description: under 160 characters, includes call to action
- Content: 400-600 words, use <h2> and <h2> tags, use <p> tags
- Tone: authoritative, professional, helpful
- End with a call to action mentioning FastCredentials
- Return ONLY valid JSON in this exact format:
{{"title": "...", "meta_description": "...", "content": "..."}}"""
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    response_text = message.content[0].text
    clean = response_text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean)

def create_blog_post(topic):
    data = generate_post(topic)
    slug = slugify(data['title'])
    if BlogPost.objects.filter(slug=slug).exists():
        print(f"Post already exists (by slug): {data['title']}")
        return False
    post = BlogPost.objects.create(
        title=data['title'],
        slug=slug,
        meta_description=data['meta_description'],
        content=data['content'],
        published=True
    )
    print(f"Created: {post.title}")
    return True

if __name__ == '__main__':
    # Shuffle topics and try each until we find one that creates a new post
    topics = TOPICS.copy()
    random.shuffle(topics)
    max_attempts = 5
    for i, topic in enumerate(topics[:max_attempts]):
        print(f"Attempt {i+1}: Generating post about: {topic}")
        try:
            if create_blog_post(topic):
                print("Success — new post created.")
                break
        except Exception as e:
            print(f"Error on attempt {i+1}: {e}")
            continue
    else:
        print(f"No new post created after {max_attempts} attempts. Topic list may be exhausted.")