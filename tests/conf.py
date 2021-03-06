#!/usr/bin/env python
# -*- encoding: utf-8 -*-

############################
# Private test server config
############################
try:
    from .conf_private import caldav_servers
except ImportError:
    caldav_servers = []

try:
    from .conf_private import only_private
except ImportError:
    only_private = False

#####################
# Public test servers
#####################
if not only_private:
    # This one will eventually go the way of the dodo at some future point
    # newer version of baikal, running under openshift.
    caldav_servers.append({
        "url": "http://baikal-test.caldav-servers.tobixen.no/cal.php/",
        "username": "testuser",
        "password": "123"})
    caldav_servers.append({
        "url": "https://baikal-test.caldav-servers.tobixen.no/cal.php/",
        "username": "testuser",
        "password": "123",
        "ssl_verify_cert": False})

    # radicale - too many problems, postponing
    # caldav_servers.append({
    #     "url": "http://radicale.caldav-servers.tobixen.no/testuser/",
    #     "username": "testuser",
    #     "password": "123"})

    # bedework:
    # * todos and journals are not properly supported -
    #   ref https://github.com/Bedework/bedework/issues/5
    # * propfind fails to return resourcetype,
    #   ref https://github.com/Bedework/bedework/issues/110
    # * date search on recurrences of recurring events doesn't work
    #   (not reported yet - TODO)
    caldav_servers.append({
        "url": "http://bedework.caldav-servers.tobixen.no/ucaldav/",
        "username": "vbede",
        "password": "bedework",
        "nojournal": True,
        "notodo": True,
        "nopropfind": True,
        "norecurring": True})

proxy = "127.0.0.1:8080"
proxy_noport = "127.0.0.1"
