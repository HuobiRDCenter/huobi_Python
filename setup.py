#!/usr/bin/env python3
from setuptools import setup

setup(
    name="huobi-client",
    version="0.1",
    packages=['huobi'],
    install_requires=['requests', 'apscheduler', 'websocket', 'websocket-client', 'urllib3']
)
