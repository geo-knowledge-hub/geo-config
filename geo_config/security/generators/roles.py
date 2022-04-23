# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Knowledge Hub Permission Generators definitions."""

from invenio_records_permissions.generators import Generator

from geo_config.security.permissions import (
    geo_community_access_action,
    geo_provider_access_action,
    geo_secretariat_access_action,
)


class GeoSecretariat(Generator):
    """Secretariat Role."""

    def __init__(self):
        """Initializer."""
        super(GeoSecretariat, self).__init__()

    def needs(self, **kwargs):
        """Role needs."""
        return [geo_secretariat_access_action]


class GeoKnowledgeProvider(Generator):
    """Knowledge Provider Role."""

    def __init__(self):
        """Initializer."""
        super(GeoKnowledgeProvider, self).__init__()

    def needs(self, **kwargs):
        """Role needs."""
        return [geo_provider_access_action]


class GeoCommunity(Generator):
    """GEO Community generator."""

    def __init__(self):
        """Initializer."""
        super(GeoCommunity, self).__init__()

    def needs(self, **kwargs):
        """Role needs."""
        return [geo_community_access_action]
