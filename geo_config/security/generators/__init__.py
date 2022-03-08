# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from .roles import (
    GeoCommunity,
    GeoSecretariat,
    GeoKnowledgeProvider,
)

from .conditional import (
    BaseConditionalGenerator,
    IfIsEqual,
)

__all__ = (
    "GeoCommunity",
    "GeoSecretariat",
    "GeoKnowledgeProvider",
    "BaseConditionalGenerator",
    "IfIsEqual",
)
