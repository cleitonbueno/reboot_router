#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2 as http


# Data Router
user_router = "user_here"
pass_router = "password_here"
ip_router   = "IP_here"
port_router = "80"


# URL with filling the fields above, URL with GET to reboot router or status main page to tests
url_get_reboot = "http://" + ip_router + ":" + port_router + "/log/in?un=" + user_router + "&pw=" + pass_router + "&rd=%2Fuir%2Frebo.htm?rc=&Nrd=0&Nsm=1"
#url_get_status = "http://" + ip_router + ":" + port_router + "/log/in?un=" + user_router + "&pw=" + pass_router + "&rd=%2Fuir%2Fstatus.htm&rd2=%2Fuir%2Fwanst.htm&Nrd=1"

# Variable global to open URL
url_root = url_get_reboot

print "Processing URL: %s" % url_root

# Handling HTTP Cookie - Session Cookie Router
cookieprocessor = http.HTTPCookieProcessor()

# Customize it Opener with CookieProcessor
opener = http.build_opener(cookieprocessor)

# Using here Opener + CookieProcessor
http.install_opener(opener)

# Open URL with Opener above
payload_router = http.urlopen(url_root)

# Print payload Request URL
print "Payload %s" % payload_router.read()
