from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twitterApp.views.index'),
    url(r'^(?P<screenName>\w{1,15})$', 'twitterApp.views.loginByScreenName'),
    url(r'^(?P<screenName>\w{1,15})/$', 'twitterApp.views.loginByScreenName'),
    # url(r'^TwitterWebApp/', include('TwitterWebApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
