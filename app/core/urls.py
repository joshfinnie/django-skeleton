from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^about/$', direct_to_template, {
        'template': 'core/about.html'
    }),
    url(r'^privacy/$', direct_to_template, {
        'template': 'core/privacy.html'
    }),
    url(r'^terms/$', direct_to_template, {
        'template': 'core/terms.html'
    }),
    url(r'^contact/$', direct_to_template, {
        'template': 'core/contact.html'
    }),
)
