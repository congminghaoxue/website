#!/usr/bin/env python
# encoding: utf-8

import os
port = int(os.environ.get('PORT', 8888))

import bjoern
from website import wsgi
bjoern.run(wsgi.application, '0.0.0.0', port)
