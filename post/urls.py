from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'posts?slug=(?P<slug>[\w-]+)/$', views.post_list),
]
