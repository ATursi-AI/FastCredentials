from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Course, BlogPost

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    def items(self):
        return ['home', 'about', 'support', 'login', 'signup']
    def location(self, item):
        return reverse(item)

class CourseSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'
    def items(self):
        return Course.objects.all()
    def location(self, obj):
        return reverse('course_detail', args=[obj.id])

class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    def items(self):
        return BlogPost.objects.all()
    def location(self, obj):
        return reverse('blog_post', args=[obj.slug])