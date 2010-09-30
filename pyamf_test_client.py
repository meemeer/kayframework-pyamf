# -*- coding: utf-8 -*-

import logging
from pyamf.remoting.client import RemotingService

client = RemotingService('http://localhost:8080/gateway')
#client = RemotingService('http://meemeer-lab.appspot.com/gateway')
service = client.getService('service')

#print service.echo('pyamf test')
print service.echo('pyamf test')
