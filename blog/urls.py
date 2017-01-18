from django.conf.urls import url, include

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/(?P<user>[a-zA-Z]+)/$', views.user, name="user"),
    url(r'^user/(?P<user>[a-zA-Z]+)/(?P<post_id>[0-9]+)/$', views.post, name="post"),
]
