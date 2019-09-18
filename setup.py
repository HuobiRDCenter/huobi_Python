#!/usr/bin/env python3
from setuptools import setup

setup(
    name="huobi-client",
    version="1.0.1",
    packages=['huobi', 'huobi.impl', 'huobi.impl.utils', 'huobi.exception', 'huobi.model', 'huobi.base'],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3']
)

