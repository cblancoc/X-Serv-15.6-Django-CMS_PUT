from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogs/$', "cms_put.views.all"),
    url(r'^blogs$', "cms_put.views.all"),
    url(r'^$', "cms_put.views.all"),
    url(r'^blogs/(.*)$', "cms_put.views.urls"),
    url(r'^(.*)$', "cms_put.views.notfound"),
)
