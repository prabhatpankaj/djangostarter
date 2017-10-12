from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from blog.views import view_post , view_category

urlpatterns = [
	url(r'^post/(?P<slug>[^\.]+)/$',view_post, name='blog_post'),
	url(r'^category/(?P<slug>[^\.]+)/$',view_category, name='blog_category'),
]
