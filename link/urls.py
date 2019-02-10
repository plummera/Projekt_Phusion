"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import url, include
from link.forms import BootstrapAuthenticationForm, SignUpForm
from link.views import home, tos, staging, blockchain, link, contact, about, signup_form, login_form, logout_form
from .registration import *
# from django.contrib.auth.views import login
# from django.contrib.auth import logout


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^$', home, name='home'),
    url(r'^tos/$', tos, name='tos'),
    url(r'^Staging_Area/$', staging, name='staging'),
    url(r'^Blockchain/$', blockchain, name='blockchain'),
    url(r'^/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^Links_AutoBot/$', link, name='link'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^signup/$', signup_form, name ='signup'),
    url(r'^login/$', login_form, name='login'),
    url(r'^logout/$', logout_form, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
