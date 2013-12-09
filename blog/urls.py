from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>\d+)/$', views.post, name='post')
)
