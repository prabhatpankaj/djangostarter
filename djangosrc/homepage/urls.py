from django.conf.urls import include, url

from homepage.views import HomeView

urlpatterns = [
    url(r'^$',HomeView,name='home'),
]
