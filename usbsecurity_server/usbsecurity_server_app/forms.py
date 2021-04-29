import django.forms as forms
import django.contrib.auth as auth

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from usbsecurity_server.usbsecurity_server_app.exceptions import IncorrectPassword, UserDisabled, AuthenticationError, UserDoesNotExist, \
    PasswordsNotMatch
from usbsecurity_server.usbsecurity_server_app.models import Device, Account


class DeviceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceAdminForm, self).__init__(*args, **kwargs)
        self.fields['ls_id'] = forms.CharField(label='Linux ID',
                                               max_length=9,
                                               required=True,
                                               validators=[
                                                   RegexValidator(
                                                       regex='^[a-fA-F0-9]{4}:[a-fA-F0-9]{4}$',
                                                       message=_('Incorrect value. The format should be "xxxx:xxxx", where x can take the following values: 0-9|a-f|A-F'),
                                                   ),
                                               ],
                                               help_text=_('Obtained by executing "lsusb".'))

    class Meta:
        model = Device
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'class': 'input', 'placeholder': 'Ingrese su nombre de usuario'}))
    password = forms.CharField(required=True,
                               max_length=255,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input', 'placeholder': 'Ingrese su contraseña'}))

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        try:
            user = User.objects.get_by_natural_key(username)

            try:
                Account.objects.get_account(user)
            except Account.DoesNotExist:
                self.add_error('username', 'No existe una cuenta para este usuario')
                raise IncorrectPassword

            if not user.check_password(password):
                self.add_error('password', 'Contraseña incorrecta')
                raise IncorrectPassword

            if not user.is_active:
                self.add_error('username', 'Usuario inactivo. Contacte a su administrador')
                raise UserDisabled

            user = auth.authenticate(username=username, password=password)
            if not user:
                self.add_error('username', 'Error de autenticacion')
                raise AuthenticationError

            return user
        except User.DoesNotExist:
            self.add_error('username', 'No existe un usuario con este nombre')
            raise UserDoesNotExist


class PasswordForm(forms.Form):
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'input',
                                                                 'placeholder': 'Ingrese su contraseña actual'}))
    new_password = forms.CharField(required=True,
                                   min_length=6,
                                   max_length=255,
                                   widget=forms.PasswordInput(attrs={'class': 'input',
                                                                     'placeholder': 'Ingrese su nueva contraseña'}))
    confirm_new_password = forms.CharField(required=True,
                                           min_length=6,
                                           max_length=255,
                                           widget=forms.PasswordInput(attrs={'class': 'input',
                                                                             'placeholder': 'Confirme su nueva contraseña'}))

    def save(self, user):
        password = self.cleaned_data['password']
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']

        if not user.check_password(password):
            self.add_error('password', 'contraseña incorrecta')
            raise IncorrectPassword

        if new_password != confirm_new_password:
            msg = 'Las contraseñas no coinciden'
            self.add_error('new_password', msg)
            self.add_error('confirm_new_password', msg)
            raise PasswordsNotMatch

        user.set_password(new_password)

        user = user.save()
        return user
