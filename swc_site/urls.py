from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swc_site.views.home', name='home'),

    url(r'^$', include('swc_blog.urls')),

    url(r'^blog/', include('swc_blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^markdown/', include('django_markdown.urls')),
)
