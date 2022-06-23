# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from invenio_rest.csrf import CSRFProtectMiddleware


def csrf_protect_middleware_factory(app):
    """Configure the CSRF Project Middleware.

    In the `invenio-rest`, the extension creates the `CSRFProtectMiddleware`
    instance. However, the exported extension object (`invenio-rest`) is an
    instance of `CSRFTokenMiddleware` (Called in a `super` context). So, to
    use methods like `exempt`, this function creates a new instance and
    registers it in the `invenio-rest` extension.
    """
    csrf = CSRFProtectMiddleware()
    csrf.init_app(app)

    app.extensions["invenio-csrf"] = csrf
