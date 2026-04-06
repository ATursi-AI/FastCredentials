from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from core.models import Course, BlogPost

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'support', 'login', 'signup', 'faq', 'pricing', 'ai_monitoring', 'ai_transparency', 'terms']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Return current date for static pages - update this when pages change
        return timezone.now()

class CourseSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return Course.objects.all()

    def location(self, obj):
        return reverse('course_detail', args=[obj.id])

    def lastmod(self, obj):
        # Courses are updated frequently due to AI monitoring
        return timezone.now()

class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return BlogPost.objects.filter(published=True)

    def location(self, obj):
        return reverse('blog_post', args=[obj.slug])

    def lastmod(self, obj):
        return obj.updated_at
