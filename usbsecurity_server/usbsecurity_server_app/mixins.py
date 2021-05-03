import django.contrib.auth as auth

from django.contrib.auth.mixins import AccessMixin
from django.http import Http404
from django.utils import translation

from usbsecurity_server.usbsecurity_server_app.models import AccountSession, Account
from usbsecurity_server.usbsecurity_server_app.utils import set_language


class LanguageCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if 'language_code' in request.session:
            return super().dispatch(request, *args, **kwargs)

        lang_client = request.META.get('LANGUAGE')
        if lang_client:
            lang_client_code = lang_client.split(':')[-1]
            if lang_client_code == 'en' or lang_client_code == 'es':
                lang_server_code = translation.get_language()
                if lang_client_code != lang_server_code:
                    try:
                        account = Account.objects.get_account(request.user)
                        set_language(account, lang_client_code)
                    except Account.DoesNotExist:
                        pass
        return super().dispatch(request, *args, **kwargs)


class AccountRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            Account.objects.get_account(request.user)
        except Account.DoesNotExist:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class AccountPersonalRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.account.is_for_all:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class CheckLoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        opened_sessions = AccountSession.objects.opened_sessions(ip_address=request.META['REMOTE_ADDR'])
        if not opened_sessions.exists():
            appearance = request.session.get('appearance')
            appearance_auto = request.session.get('appearance_auto')
            language_code = request.session.get('language_code')

            auth.logout(request)

            request.session['appearance'] = appearance
            request.session['appearance_auto'] = appearance_auto
            request.session['language_code'] = language_code
        return super().dispatch(request, *args, **kwargs)
