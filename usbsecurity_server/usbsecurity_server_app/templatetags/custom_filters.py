import uuid
import os

from django import template

from usbsecurity_server.usbsecurity_server import settings

register = template.Library()


@register.simple_tag(name='cache_bust')
def cache_bust():
    statics_version = getattr(settings, 'STATICS_VERSION', None)

    if not statics_version:
        project_version = os.environ.get('PROJECT_VERSION')
        version = project_version if project_version else 1
    else:
        version = uuid.uuid1() if statics_version < 0 else statics_version

    return 'v={version}'.format(version=version)
