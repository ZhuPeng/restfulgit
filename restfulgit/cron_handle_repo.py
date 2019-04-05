# coding=utf-8
from __future__ import absolute_import, unicode_literals, print_function, division

from restfulgit.app_factory import create_app
import sys 
import os
from flask import safe_join
reload(sys) 
sys.setdefaultencoding('utf-8') 

application = create_app()
LOADED_CONFIG = application.config.from_envvar('RESTFULGIT_CONFIG', silent=True)
LOADED_CONFIG = LOADED_CONFIG or application.config.from_pyfile('/etc/restfulgit.conf.py', silent=True)
if not LOADED_CONFIG:
    raise SystemExit("Failed to load any RestfulGit configuration!")

parent = application.config['RESTFULGIT_REPO_BASE_PATH']
for d in os.listdir(parent):
    real = safe_join(parent, d)
    os.system('cd %s && git pull' % real)

if __name__ == '__main__':
    pass

