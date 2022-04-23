# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Config extension definition."""

from . import config


class GEOConfig(object):
    """geo-config extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["geo-config"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "GEO_CONFIG_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"],
            )
        for k in dir(config):
            if k.startswith("GEO_CONFIG_") or k.startswith("RDM_PERMISSION_POLICY"):
                app.config.setdefault(k, getattr(config, k))
