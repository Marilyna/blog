from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>\d+)/$', views.edit_post, name='edit_post'),

    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^sign-out/$', views.sign_out, name='sign_out')
)
