from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from UserApp.views import *
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Project.views.home', name='home'),
    # url(r'^Django_Project/', include('Django_Project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^users/$',users_list),
     (r'^users/(\d+)/$',users_search),
     (r'^users/edit/(\d+)/$',users_edit),
     (r'^search-form/$', search_form),
     (r'^search/$', search),
     (r'^creacion/$', creacion),
     (r'^create/$', create_u),
     (r'^login/$', login),
     (r'^session/$', session),
     (r'^login_u/$', login_u),
     (r'^crear_post/$', crear_post),
     (r'^logout/$', logout),
     (r'^siguiendo/$', siguiendo),
     (r'^seguido/$', seguido),
     (r'^borrar_siguiendo/$', borrar_siguiendo),
     (r'^borrar_seguido/$', borrar_seguido),
     (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
		'django.views.static.serve',
		{'document_root' : settings.STATIC_ROOT })
)
