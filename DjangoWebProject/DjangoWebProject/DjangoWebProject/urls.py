﻿"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()


 
urlpatterns = patterns('',
    
    # Examples :
    # app index
    url(r'^$', 'app.views.index', name='home'),# Notice this line
    
    # calc add
    url(r'^add/&', 'calc.views.add', name='add'),

    # calc::index
    url(r'^index', 'calc.views.home', name='home'),

    #url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
 
    #url(r'^admin/', include(admin.site.urls)),
)

'''

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
'''