import requests
from rest_framework.views import APIView, Response, status

from rest_framework_simplejwt.tokens import RefreshToken
from core.models import User



class SignIn(APIView):

    def post(self, request):
        token = request.data.get("token")

        if token is None:
            return Response(
                {"error": "A Microsoft identity token must be provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        res = request.get(
            "https://graph.microsoft.com/v1.0/"+"me",
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







