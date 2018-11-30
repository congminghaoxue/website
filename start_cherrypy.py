#!/usr/bin/env python
# encoding: utf-8

from cheroot import wsgi

from app import application

server = wsgi.Server(
    ('0.0.0.0', 8888), application, numthreads=10)
try:
    server.start()
except KeyboardInterrupt:
    server.stop()
