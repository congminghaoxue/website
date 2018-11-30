#!/usr/bin/env python
from tornado import httpserver, ioloop, wsgi

from app import application

container = wsgi.WSGIContainer(application)
server = httpserver.HTTPServer(container)
server.bind(8888)
server.start(0)
ioloop.IOLoop.current().start()
