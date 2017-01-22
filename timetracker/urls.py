from django.conf.urls import url, include

from . import views

app_name = 'timetracker'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^date/(?P<date_given>[0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/$', views.givenDate, name="date"),
]
