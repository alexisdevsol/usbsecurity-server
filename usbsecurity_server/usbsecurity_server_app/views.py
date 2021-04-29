import django.contrib.auth as auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

from usbsecurity_server.usbsecurity_server.settings import ACTION_ADD, ACTION_REMOVE
from usbsecurity_server.usbsecurity_server_app.exceptions import UserDoesNotExist, AuthenticationError, IncorrectPassword, \
    PasswordsNotMatch
from usbsecurity_server.usbsecurity_server_app.forms import LoginForm, PasswordForm
from usbsecurity_server.usbsecurity_server_app.mixins import CheckLoginMixin, AccountPersonalRequiredMixin
from usbsecurity_server.usbsecurity_server_app.models import AccountSession, Computer, AccountComputer, Device, AccountDevice


class ActionDeviceView(TemplateView):
    def get(self, request, *args, **kwargs):
        action = kwargs.get('action')
        device_id = kwargs.get('device_id')

        data = {
            'error': None,
            'is_authorized': False
        }

        if action == ACTION_ADD:
            opened_sessions = AccountSession.objects.opened_sessions(ip_address=request.META['REMOTE_ADDR'])
            if not opened_sessions.exists():
                data['error'] = 'No session is open on the computer'
                return JsonResponse(data, safe=False)

            try:
                computer = Computer.objects.get_computer(request.META['REMOTE_ADDR'])
            except Computer.DoesNotExist:
                computer = None

            if computer:
                opened_sessions_accounts = opened_sessions.values_list('account', flat=True)
                ac_computers = AccountComputer.objects.all_computers(opened_sessions_accounts)
                if ac_computers.exists():
                    try:
                        ac_computers.get_assoc(computer)
                    except AccountComputer.DoesNotExist:
                        data['error'] = 'User not associated with the computer'
                        return JsonResponse(data, safe=False)

            try:
                device = Device.objects.get_device(device_id)
            except Device.DoesNotExist:
                device = None

            if device:
                ac_devices = AccountDevice.objects.all_devices(request.user.account)
                if ac_devices.exists():
                    try:
                        ac_devices.get_assoc(device)
                    except AccountDevice.DoesNotExist:
                        data['error'] = 'User not associated with the device'
                        return JsonResponse(data, safe=False)

            data['is_authorized'] = True
            return JsonResponse(data, safe=False)
        if action == ACTION_REMOVE:
            ip_address = request.META['REMOTE_ADDR']
            AccountSession.objects.close_sessions(ip_address)
            opened_sessions = AccountSession.objects.opened_sessions(ip_address=ip_address)
            data['is_authorized'] = opened_sessions.exists()
            return JsonResponse(data, safe=False)
        else:
            data['error'] = 'Undefined action'
            return JsonResponse(data, safe=False)


class BaseView(TemplateView):
    pass


class HomeView(CheckLoginMixin, BaseView):
    template_name = 'index.html'


class LoginView(CheckLoginMixin, BaseView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = LoginForm()
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = LoginForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context)

        try:
            user = form.save()

            if not user.is_active:
                return self.render_to_response(context)

            auth.login(request, user)
            if not user.is_authenticated:
                return redirect(reverse('login'))

            ip_address = request.META['REMOTE_ADDR']
            AccountSession.objects.close_sessions(ip_address)
            AccountSession.objects.create_session(user.account, ip_address)

            next_page = request.GET.get('next', None)
            if not next_page:
                return redirect(reverse('account'))
            return redirect(next_page)
        except (UserDoesNotExist, AuthenticationError, IncorrectPassword):
            context['form'] = form
            return self.render_to_response(context)


class AccountView(CheckLoginMixin, LoginRequiredMixin, BaseView):
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if not request.user.account.is_for_all:
            context['ac_devices'] = AccountDevice.objects.all_devices(request.user.account)

        return self.render_to_response(context)


class AccountLogoutView(CheckLoginMixin, LoginRequiredMixin, BaseView):
    template_name = 'account/logout.html'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        AccountSession.objects.close_sessions(request.META['REMOTE_ADDR'])
        auth.logout(request)
        return redirect(reverse('login'))


class AccountPasswordView(CheckLoginMixin, LoginRequiredMixin, AccountPersonalRequiredMixin, BaseView):
    template_name = 'account/password.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = PasswordForm()
        return self.render_to_response(context)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        form = PasswordForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context)

        try:
            form.save(request.user)
            return redirect(reverse('login'))
        except (IncorrectPassword, PasswordsNotMatch):
            context['form'] = form
            return self.render_to_response(context)
