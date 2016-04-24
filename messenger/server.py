# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # noqa
from messenger import create_app, settings


# Module script

if __name__ == '__main__':

    # Create application
    app = create_app()

    # Run application
    app.run(host='0.0.0.0', port=settings.PORT, debug=settings.DEBUG)
