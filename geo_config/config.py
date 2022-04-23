# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Config module configurations."""

from geo_config.security.permissions import views_permissions_factory
from geo_config.security.policies import GeoRecordPermissionPolicy

RDM_PERMISSION_POLICY = GeoRecordPermissionPolicy
"""Policy settings."""

GEO_CONFIG_VIEW_PERMISSIONS_FACTORY = views_permissions_factory
"""View permissions factory."""
