#!/usr/bin/env bash

uwsgi --socket 127.0.0.1:8888 --protocol=http --wsgi-file app.py