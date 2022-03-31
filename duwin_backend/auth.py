from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class JWTBackend:
    authenticator = JWTAuthentication()

    def authenticate(self, request=None, **kwargs):
        if request is None:
            return None

        tuple_user = self.authenticator.authenticate(request)

        if type(tuple_user) is tuple:
            return tuple_user[0]

        return None


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user = authenticate(request)
            if user is not None and user.is_authenticated:
                request.user = user

        except Exception as e:
            pass

        response = self.get_response(request)

        return response

