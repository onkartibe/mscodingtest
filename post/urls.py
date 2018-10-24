from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'posts/(?P<slug>[\w-]+)/$', views.post_list),
]
