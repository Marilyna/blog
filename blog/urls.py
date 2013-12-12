from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from blog import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.post_page, name='post_page'),
    url(r'^new/$', views.new_post, name='new'),

    url(r'^sign-in/$', views.sign_in, name='sign_in'),
    url(r'^sign-out/$', views.sign_out, name='sign_out')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
