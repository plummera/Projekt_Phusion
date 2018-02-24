"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url, include
from link.forms import BootstrapAuthenticationForm
from django.contrib.auth.views import *
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from link.views import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^$', home, name='home'),
    url(r'^Staging_Area/$', staging, name='staging'),
    url(r'^Blockchain/$', blockchain, name='blockchain'),
    url(r'^Links_AutoBot/$', link, name='link'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^login/$', login, {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.date.year,
            }
        },
        name='login'),
    url(r'^logout/$', logout, {  'next_page': '/'  },        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),

    #Browsable RESTful framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
