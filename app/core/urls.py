from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'home'),
    url(r'^about/$', 'about'),
    url(r'^privacy/$', 'privacy'),
    url(r'^terms/$', 'terms'),
    url(r'^contact/$', 'contact'),
)
