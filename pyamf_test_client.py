# -*- coding: utf-8 -*-

import logging
from pyamf.remoting.client import RemotingService

client = RemotingService('http://localhost:8080/gateway')
service = client.getService('service')

print service.echo('pyamf test')
