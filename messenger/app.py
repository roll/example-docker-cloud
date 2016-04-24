# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask

from . import blueprints


# Module API

def create_app():
    """Create application.
    """

    # Create application
    app = Flask('service')

    # Register blueprints
    app.register_blueprint(blueprints.home.create_blueprint(), url_prefix='')

    # Return application
    return app
