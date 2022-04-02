from duwin_backend.mutations import BaseMutation
from django.apps import apps
from .serializers import serializers
import graphene

Mutation = type("Mutation", (graphene.ObjectType,), {
    i.query_name: i.Field() for i in [
        type(
            f"{j.__name__}Mutation",
            (BaseMutation, ),
            {
                "Meta": type("Meta", (), {
                    "serializer_class": serializers[f"{j.__name__}"]
                }),
                "query_name": f"{j.__name__.lower()}s"
            }
        ) for j in apps.get_app_config("core").get_models()

    ]
})


