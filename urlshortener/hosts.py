from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),

    #for everything else apart from www call urlshortener.hostsconf.urls
    host(r'(?!www).*', 'urlshortener.hostsconf.urls', name='wildcard'),

)