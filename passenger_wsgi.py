import os
import sys

project_home = '/home/ethereal/proj'
if project_home not in sys.path:
    sys.path.append(project_home)
    
os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# sys.path.insert(0, os.path.dirname(__file__))


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]
