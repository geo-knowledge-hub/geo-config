# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from geo_config import GEOConfig


def test_version():
    """Test version import."""
    from geo_config import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = GEOConfig(app)
    assert 'geo-config' in app.extensions

    app = Flask('testapp')
    ext = GEOConfig()
    assert 'geo-config' not in app.extensions
    ext.init_app(app)
    assert 'geo-config' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to geo-config' in str(res.data)
