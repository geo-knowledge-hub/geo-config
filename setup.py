# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-config is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Knowledge Hub module that provides configuration options about security, environment, and other stuff"""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

# Should follow inveniosoftware/invenio versions
invenio_db_version = ">=1.0.11,<2.0.0"
invenio_search_version = ">=1.4.0,<2.0.0"

tests_require = [
    "pytest-mock>=1.6.0",
    "pytest-invenio>=1.4.0",
    "invenio-app>=1.3.1,<2.0.0"
]

extras_require = {
    "docs": ["sphinx>=4.2.0,<5"],
    # Elasticsearch version
    "elasticsearch7": [
        "invenio-search[elasticsearch7]{}".format(invenio_search_version),
    ],
    # Databases
    "mysql": [
        "invenio-db[mysql,versioning]{}".format(invenio_db_version),
    ],
    "postgresql": [
        "invenio-db[postgresql,versioning]{}".format(invenio_db_version),
    ],
    "sqlite": [
        "invenio-db[versioning]{}".format(invenio_db_version),
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    if name[0] == ":" or name in (
            "elasticsearch7",
            "mysql",
            "postgresql",
            "sqlite"
    ):
        continue
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=2.8",
    "pytest-runner>=3.0.0,<5",
]

install_requires = [
    "invenio-i18n>=1.2.0",
    "geo-rdm-records @ git+https://github.com/geo-knowledge-hub/geo-rdm-records@v0.2.0",
]
packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("geo_config", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="geo-config",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=["GEO Knowledge Hub", "Invenio Module", "Configuration"],
    license="MIT",
    author="GEO Secretariat",
    author_email="geokhub@geosec.org",
    url="https://github.com/geo-knowledge-hub/geo-config",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "geo_config = geo_config:GEOConfig",
        ],
        "invenio_base.api_apps": [
            "geo_config = geo_config:GEOConfig",
        ],
        "invenio_access.actions": [
            "geo-community-access"
            " = geo_config.security.permissions:geo_community_access_action",
            "geo-provider-access"
            " = geo_config.security.permissions:geo_provider_access_action",
            "geo-secretariat-access"
            " = geo_config.security.permissions:geo_secretariat_access_action",
        ],
        "invenio_i18n.translations": [
            "messages = geo_config",
        ],
        # TODO: Edit these entry points to fit your needs.
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        # 'invenio_base.api_blueprints': [],
        # 'invenio_base.blueprints': [],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
