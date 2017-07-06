#!/usr/bin/env python
# encoding: utf-8

from cherrypy import wsgiserver

from website.wsgi import application

server = wsgiserver.CherryPyWSGIServer(
    ('0.0.0.0', 8888), application, numthreads=10)
try:
    server.start()
except KeyboardInterrupt:
    server.stop()
