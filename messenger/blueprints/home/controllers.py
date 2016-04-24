# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ... import settings


# Module API

class MessageController(object):
    """Say message from settings.
    """

    # Public

    def __call__(self):
        return 'Message: %s' % settings.MESSAGE
