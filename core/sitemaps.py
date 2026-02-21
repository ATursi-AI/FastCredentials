from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Course  # <--- Crucial: Import your database model

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # We added 'about', 'support', 'login' to the list
        return ['home', 'about', 'support', 'login', 'signup']

    def location(self, item):
        return reverse(item)

class CourseSitemap(Sitemap):
    priority = 0.9      # Higher priority because these are your money pages
    changefreq = 'daily'

    def items(self):
        # This grabs every course from the database automatically
        return Course.objects.all()

    def location(self, obj):
        # This tells Google the exact URL for each course
        return reverse('course_detail', args=[obj.id])
