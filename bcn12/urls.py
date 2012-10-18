from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bcn12.views.home', name='home'),
    # url(r'^bcn12/', include('bcn12.foo.urls')),

    url(r'^crimes.json$', 'demo.views.crime_dots', name='crime-dots'),
    url(r'^point-map/$', direct_to_template, {'template': 'point_map.html' }),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
