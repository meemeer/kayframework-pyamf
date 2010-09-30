# -*- coding: utf-8 -*-
# myapp.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('myapp/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'myapp/index': 'myapp.views.index',
}
"""

from werkzeug.routing import EndpointPrefix, Rule
import myapp.views

def make_rules():
    return [
            EndpointPrefix('myapp/', [
                Rule('/', endpoint='index'),
                Rule('/gateway', endpoint='gateway'),
                Rule('/crossdomain.xml', endpoint='crossdomain'),
                ])
            ]

all_views = {
        'myapp/index': myapp.views.index,
        'myapp/gateway': myapp.views.gateway,
        'myapp/crossdomain': myapp.views.crossdomain,
        }
