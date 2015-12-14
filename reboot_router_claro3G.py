#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2 as http

# URL with GET to reboot router
url_get_reboot = 'http://10.11.12.254/log/in?un=admin&pw=admin12&rd=%2Fuir%2Frebo.htm?rc=&Nrd=0&Nsm=1'


# Handling HTTP Cookie - Session Cookie Router
cookieprocessor = http.HTTPCookieProcessor()

# Customize it Opener with CookieProcessor
opener = http.build_opener(cookieprocessor)

# Using here Opener + CookieProcessor
http.install_opener(opener)

# Open URL with Opener above
payload_router = http.urlopen(url_get_reboot)

# Print payload Request URL
print "Payload %s" % payload_router.read()
