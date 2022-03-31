import msal
from decouple import config


def get_token():
    app = msal.ConfidentialClientApplication(
        config("APP_ID", cast=str),
        authority="https://login.microsoftonline.com/trsuedu.onmicrosoft.com",
        client_credential={
            "thumbprint": config("THUMBPRINT", cast=str),
            "private_key": open("key.pem").read()
        })
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    return result

