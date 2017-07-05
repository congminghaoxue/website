#!/usr/bin/env sh
#

gunicorn website.wsgi --bind localhost:8888
