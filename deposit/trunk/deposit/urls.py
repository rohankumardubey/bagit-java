from django.conf.urls.defaults import *
from django.contrib import admin
from django.core.urlresolvers import reverse

from deposit.settings import MEDIA_URL, MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^admin/$', admin.site.root, name='admin_url'),
    )

# media route - only uncomment for development environments!
# should serve up with apache/lighttpd/etc in production
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}, name='media'),
    )

# Use built-in login screen.
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'},
        name='login_url'),
    )

urlpatterns += patterns('deposit.depositapp.views',
    url(r'^$', 'index', name='home_url'),
    url(r'^logout/$', 'logout', name='logout_url'),

    url(r'^overview/(?P<username>\w+)?$', 'overview', name='overview_url'),

    url(r'^user/(?P<username>\w+)$', 'user', name='user_url'),
    url(r'^user/(?P<username>\w+)/(?P<command>\w+)$', 'user', 
        name='user_command_url'),

    url(r'^transfer/$', 'transfer_list', name='transfer_list'),
    url(r'^transfer/(?P<transfer_id>\d+)$', 'transfer', 
        name='transfer_url'),
    url(r'^transfer/create(?P<transfer_type>\w+)$', 'create_transfer', 
        name='create_transfer_url'),
    url(r'^transfer/(?P<transfer_id>\d+)/received$', 'transfer_received', 
        name='transfer_received_url'),

    url(r'^project/(?P<project_id>\d+)$', 'project', name='project_url'),
    )

# FIXME: commented out for deposit_0.2_qa
#urlpatterns += patterns('deposit.sword.views',
#    url(r'^api/service$', 'service', name='sword_service_url'),    
#    url(r'^api/collection/(?P<project_id>\d+)$', 'collection', 
#        name='sword_collection_url'),
#    url(r'^api/collection/(?P<project_id>\d+)/(?P<transfer_id>\d+)$', 'entry',
#        name='sword_entry_url'),
#    url(r'^api/collection/(?P<project_id>\d+)/(?P<transfer_id>\d+)/package$', 
#        'package', name='sword_package_url')
#    )
