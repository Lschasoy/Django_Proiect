from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from UserApp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Project.views.home', name='home'),
    # url(r'^Django_Project/', include('Django_Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     ('^users/$',users_list),
     ('^users/(\d+)/$',users_search),
)
