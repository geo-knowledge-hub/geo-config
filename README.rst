..
    Copyright (C) 2022 GEO Secretariat.

    geo-config is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

===========
 GEO Config
===========

.. .. image:: https://img.shields.io/pypi/dm/geo-config.svg
..         :target: https://pypi.python.org/pypi/geo-config

.. image:: https://github.com/geo-knowledge-hub/geo-config/workflows/CI/badge.svg
        :target: https://github.com/geo-knowledge-hub/geo-config/actions?query=workflow%3ACI

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/github/license/geo-knowledge-hub/geo-config.svg
        :target: https://github.com/geo-knowledge-hub/geo-config/blob/master/LICENSE

.. image:: https://img.shields.io/github/tag/geo-knowledge-hub/geo-config.svg
        :target: https://github.com/geo-knowledge-hub/geo-config/releases

GEO Knowledge Hub Configuration module to manage security definitions, environment, and other stuff.

Development
===========

Install
-------

Install the package with the `docs`, `elasticsearch`, and a `database` dependencies:

.. code-block:: console

    pip install -e .[docs, <[mysql|postgresql|sqlite]>, elasticsearch7]


Tests
-----

After installing the package and its dependencies, if you want to test the code, install the `tests` dependencies:

.. code-block:: console

    pip install -e .[tests]

Now, you can run the tests:

.. code-block:: console

    ./run-tests.sh
