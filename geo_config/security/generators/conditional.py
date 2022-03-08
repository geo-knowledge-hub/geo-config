# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from abc import ABC, abstractmethod

from invenio_records.dictutils import dict_lookup
from invenio_records_permissions.generators import Generator

from itertools import chain


class BaseConditionalGenerator(ABC, Generator):
    """Base generator to enable the creation of conditional generators."""

    @abstractmethod
    def generators(self, record):
        """Choose between 'then' or 'else' generators."""

    def needs(self, record=None, **kwargs):
        """Needs to granting permission."""

        # in the chain above is checked if the
        # ``g`` has ``needs``. In this case is assumed
        # that ``g`` is a ``Generator``. Otherwise, is
        # assumed that ``g`` is a ``flask_principal.Need``.
        return list(
            set(
                chain.from_iterable(
                    [
                        g.needs(record=record, **kwargs) if hasattr(g, "needs") else [g]
                        for g in self.generators(record)
                    ]
                )
            )
        )


class IfIsEqual(BaseConditionalGenerator):
    """IfIsEqual generator.
    This conditional generator check if a record attribute is equal a defined value:
        IfIsEqual(
            field    = 'data.status',
            equal_to = 'A',
            then_    = [<Generator>, <Generator>,],
            else_    = [<Generator>, <Generator>,]
        )
    Note:
        The ideia and base implementation of the conditional generators is presented in the
        Invenio-RDM-Records, so, thanks invenio team for this.
    """

    def __init__(self, field, equal_to, then_, else_):
        self.field = field
        self.then_ = then_
        self.else_ = else_

        self.equal_to = equal_to

    def generators(self, record):
        """Choose between 'then' or 'else' generators."""
        if record is None:
            return self.else_

        # getting the field using pydash
        # (handle properties and keys equally)
        value = dict_lookup(record, self.field)

        if value == self.equal_to:
            return self.then_
        return self.else_
