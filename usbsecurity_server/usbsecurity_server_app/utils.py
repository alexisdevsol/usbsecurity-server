from django.utils import translation


def set_language(account, code):
    """
    Establecer idioma
    :param account: Cuenta de usuario
    :param code: Code ISO
    """
    translation.activate(code)
    account.language_code = code
    account.save()
