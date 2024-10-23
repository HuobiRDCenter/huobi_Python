#!/usr/bin/env python3
from setuptools import setup

setup(
    name="huobi-client",
    version="2.0.0",
    packages=['huobi',
              'huobi.exception', 'huobi.constant',
              'huobi.utils',
              'huobi.client',
              'huobi.service', 'huobi.service.account', 'huobi.service.margin', 'huobi.service.market',
              'huobi.service.trade', 'huobi.service.wallet', 'huobi.service.generic', 'huobi.service.etf',
              'huobi.service.subuser', 'huobi.service.algo',
              'huobi.model', 'huobi.model.account', 'huobi.model.margin', 'huobi.model.market', 'huobi.model.trade',
              'huobi.model.wallet', 'huobi.model.generic', 'huobi.model.etf', 'huobi.model.subuser', 'huobi.model.algo',
              'huobi.connection', 'huobi.connection.impl', "performance", "tests"
              ],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3']
)
