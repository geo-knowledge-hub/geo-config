# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Knowledge Hub Base Security Policies."""

from invenio_rdm_records.services.generators import RecordOwners
from invenio_rdm_records.services.permissions import RDMRecordPermissionPolicy
from invenio_records_permissions.generators import SystemProcess

from geo_config.security.generators import GeoKnowledgeProvider, GeoSecretariat


class GeoRecordPermissionPolicy(RDMRecordPermissionPolicy):
    """Access control configuration for records."""

    #
    # Records
    #
    can_manage = [RecordOwners(), GeoSecretariat(), SystemProcess()]

    can_create = [GeoKnowledgeProvider(), GeoSecretariat(), SystemProcess()]


__all__ = "GeoRecordPermissionPolicy"
