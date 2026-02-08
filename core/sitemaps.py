from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # The names inside reverse() must match the 'name=' in your urls.py
        return ['home']

    def location(self, item):
        return reverse(item)
