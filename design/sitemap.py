from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from design.models import Post
from design.models import Comment


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'
 
    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.created_on
    
    def location(self, obj):
        return '/postlist/%s' % (obj.title)



class CommentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return Comment.objects.all()
    
    def lastmod(self, obj):
        return obj.created_on
    
    def location(self, obj):
        return '/comment/%s' % (obj.Help)



class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return ['index', 'contactus'] #returning static pages; home and contact us
 
    def location(self, item):
        return reverse(item) 