from django.core.exceptions import ObjectDoesNotExist


class AuthenticationError(ObjectDoesNotExist):
    pass


class UserDoesNotExist(ObjectDoesNotExist):
    pass


class UserDisabled(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class PasswordsNotMatch(Exception):
    pass
