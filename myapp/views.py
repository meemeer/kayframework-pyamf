# -*- coding: utf-8 -*-
"""
myapp.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from kay.utils import render_to_response
from pyamf.remoting.gateway.wsgi import WSGIGateway
from myapp.services.test_pyamf import TestPyAMF


# Create your views here.

def index(request):
  return render_to_response('myapp/index.html', {'message': 'Hello'})

def gateway(request):
    return WSGIGateway({'service': TestPyAMF})

def crossdomain(request):
    return render_to_response('myapp/crossdomain.xml')
