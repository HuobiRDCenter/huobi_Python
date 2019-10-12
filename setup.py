#!/usr/bin/env python3
from setuptools import setup

setup(
    name="huobi-client",
    version="1.0.2",
    packages=['huobi',
              'huobi.exception', 'huobi.constant',
              'huobi.utils',
              'huobi.client',
              'huobi.service', 'huobi.service.account', 'huobi.service.margin', 'huobi.service.market', 'huobi.service.trade', 'huobi.service.wallet',
              'huobi.serialize', 'huobi.serialize.account', 'huobi.serialize.margin', 'huobi.serialize.market', 'huobi.serialize.trade', 'huobi.serialize.wallet',
              'huobi.model', 'huobi.model.account', 'huobi.model.margin', 'huobi.model.market', 'huobi.model.trade', 'huobi.model.wallet',
              'huobi.connection', 'huobi.connection.impl'
              ],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3']
)

