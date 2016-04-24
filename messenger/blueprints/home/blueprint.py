# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint

from . import controllers


# Module API

def create_blueprint():
    """Create blueprint.
    """

    # Create instase
    blueprint = Blueprint('home', 'home')

    # Register routes
    blueprint.add_url_rule('/', 'message', controllers.MessageController())

    # Return blueprint
    return blueprint
