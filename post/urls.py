from django.conf.urls import url
from post import views

urlpatterns = [
    url('posts/', views.post_list),
    url(r'posts?slug=(?P<slug>[\w-]+)/$', views.post_details),
]
