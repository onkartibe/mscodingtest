from django.conf.urls import url
from post import views

urlpatterns = [
    url('posts/', views.post_list),
    url(r'post/(?P<slug>[\w-]+)/$', views.post_details),
]