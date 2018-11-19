from django.core.exceptions import ImproperlyConfigured


class FailedPreCondition(Exception):
    def __init__(self, message, messages=None, kind=None, status='ERROR'):
        self.status = status
        if message:
            self.messages = message
        elif messages:
            self.messages = [messages]
        else:
            self.messages = []
        if kind:
            self.kind = kind
        else:
            self.kind = 'APIException'


class SystemImproperlyConfigured(ImproperlyConfigured):
    def __init__(self, message='Something went internally wrong with the API. Please contact us if you get this error.',
                 kind='FatalException', status='ERROR'):
        self.status = status
        self.message = message
        self.kind = kind


class ImproperTransactionToken(Exception):
    def __init__(self):
        pass


class AuthenticationFailure(Exception):
    def __init__(self, message='System is not able to autheticate you. Please enter valid mobile number and password.',
                 kind='AuthException', status='ERROR'):
        self.status = status
        self.message = message
        self.kind = kind


class EligibilityFailure(Exception):
    def __init__(self, message='Sorry, you are not approved for Kredivo\'s credit wallet.', kind='APIException',
                 status='ERROR', code=401, session_data={}):
        self.status = status
        self.message = message
        self.kind = kind
        self.code = code
        self.session_data = session_data


class OTPGenerationFailure(Exception):
    def __init__(self, message='Sorry, We are unable to generate OTP at the moment. Please try again after sometime.',
                 kind='APIException', status='ERROR', code=401):
        self.status = status
        self.message = message
        self.kind = kind
        self.code = code


class OTPVerificationFailure(Exception):
    def __init__(self, message='Sorry, We are unable to generate OTP at the moment. Please try again after sometime.',
                 kind='APIException', status='ERROR', code=401):
        self.status = status
        self.message = message
        self.kind = kind
        self.code = code


class MerchantNotificationFailure(Exception):
    def __init__(self, message='Sorry, We are unable to inotify merchant.',
                 kind='APIException', status='ERROR', code=401):
        self.status = status
        self.message = message
        self.kind = kind
        self.code = code


class ParamsMissing(Exception):
    def __init__(self, message='Sorry, We are unable to process this request. Parameteres are missing.',
                 kind='APIException', status='ERROR', code=401):
        self.status = status
        self.message = message
        self.kind = kind
        self.code = code