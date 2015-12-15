#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2 as http

""" Python script to reboot modem/router Claro 3G - D-LINK DWR-922

This script use method GET to reboot router.

Example use:
$ python reboot_router_claro3G.py

"""

__author__    = "Cleiton Bueno <cleitonrbueno at gmail.com>"
__copyright__ = "Copyright (C) 2015 Cleiton Bueno"
__license__   = "The Apache License 2.0 (ASL)"
__version__   = "1.0"


# Data Router
user_router = "user_here"
pass_router = "password_here"
ip_router   = "IP_here"
port_router = "80"



# URL with filling the fields above, URL with GET to reboot router or status main page to tests
url_get_reboot = "http://" + ip_router + ":" + port_router + "/log/in?un=" + user_router + "&pw=" + pass_router + "&rd=%2Fuir%2Frebo.htm?rc=&Nrd=0&Nsm=1"
url_get_status = "http://" + ip_router + ":" + port_router + "/log/in?un=" + user_router + "&pw=" + pass_router + "&rd=%2Fuir%2Fstatus.htm&rd2=%2Fuir%2Fwanst.htm&Nrd=1"

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
try:
  payload_router = http.urlopen(url_root)

  if payload_router.getcode() == 200:
    print "\t Rebooting router, waiting..."
  else:
    print "\t Fail reboot router!"
    print "\t  * Check parameters [user_route e pass_router]"
except http.HTTPError as http_err:
  print "\tHTTP Error -> %s" % http_err.read()

except http.URLError as url_err:
  print "\tRouter offline ou IP/Port incorrect!"
  print "\t\tError -> %s " % url_err.reason
