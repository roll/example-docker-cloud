# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest

import messenger


# Tests

def test_hello(app):
    res = app.get('/')
    assert res.status == '200 OK'
    assert 'Message:' in res.data.decode('utf-8')


# Fixtures

@pytest.fixture
def app():
    app = messenger.create_app()
    app = app.test_client()
    return app
