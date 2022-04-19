import requests
from rest_framework.views import APIView, Response, status

from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User
from core.serializers import BaseSerializer


class BaseView(APIView):

    permission_classes = []
    authentication_classes = []
    serializer = None

    def post(self, request, **kwargs):
        if not isinstance(self.serializer, BaseSerializer):
            raise TypeError(self.__name__ + "'s serializer attribute must be of type " + type(BaseSerializer))

        seri = self.serializer(
            data=request.data,
        )

        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)

        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):

    def post(self, request):
        token = request.data.get("token")

        if token is None:
            return Response(
                {"error": "A Microsoft identity token must be provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        res = request.get(
            "https://graph.microsoft.com/v1.0/me",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            )

        if res.status not in range(199,300):
            return Response({"MS_error": res.json()}, status=res.status)

        res = res.json()
        user = User.objects.filter(ms_id=res["id"]).first()

        if user is None:
            user = User.objects.create(email=res["email"], ms_id=res["id"])
            user.save()

        access = RefreshToken.for_user(user).access_token
        return Response({"access": str(access)}, status=status.HTTP_200_OK)







