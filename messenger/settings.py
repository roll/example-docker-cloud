# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from dotenv import load_dotenv; load_dotenv('.env')  # noqa


# General

PORT = int(os.environ.get('PORT', '8080'))
DEBUG = os.environ.get('DEBUG', False)
MESSAGE = os.environ.get('MESSAGE', 'Hello World!')
