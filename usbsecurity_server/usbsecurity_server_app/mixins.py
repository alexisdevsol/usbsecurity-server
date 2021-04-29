import django.contrib.auth as auth

from django.contrib.auth.mixins import AccessMixin
from django.http import Http404

from usbsecurity_server.usbsecurity_server_app.models import AccountSession


class AccountPersonalRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.account.is_for_all:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class CheckLoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        opened_sessions = AccountSession.objects.opened_sessions(ip_address=request.META['REMOTE_ADDR'])
        if not opened_sessions.exists():
            auth.logout(request)
        return super().dispatch(request, *args, **kwargs)
