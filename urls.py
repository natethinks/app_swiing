from django.conf.urls import url

from . import views

app_name = ''
urlpatterns = [
    # ex: /home/
    url(r'^$', views.home,),
    url(r'^about$', views.about,),
    url(r'^adventures$', views.adventures,),
    url(r'^contact$', views.contact,),
    url(r'^adventures/(?P<a_slug>[a-z0-9._-]+$)', views.singletrip),
    url(r'^charge', views.charge)
]
#url(r'^$', views.index, name='index'),
