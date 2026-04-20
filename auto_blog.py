import os
import django
import anthropic
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import BlogPost

TOPICS = [
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
    
    import json
    response_text = message.content[0].text
    clean = response_text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean)

def create_blog_post(topic):
    data = generate_post(topic)
    slug = slugify(data['title'])
    
    if BlogPost.objects.filter(slug=slug).exists():
        print(f"Post already exists: {data['title']}")
        return
    
    post = BlogPost.objects.create(
        title=data['title'],
        slug=slug,
        meta_description=data['meta_description'],
        content=data['content'],
        published=True
    )
    print(f"Created: {post.title}")

if __name__ == '__main__':
    import random
    topic = random.choice(TOPICS)
    print(f"Generating post about: {topic}")
    create_blog_post(topic)