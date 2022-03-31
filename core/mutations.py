from duwin_backend.mutations import BaseMutation
from django.apps import apps
from .serializers import serializers
import graphene

models = apps.get_app_config("core").get_models()

mutations = {
    f"{i.__name__}":
        type(
            f"{i.__name__}Mutation",
            (BaseMutation, ),
            {
                "Meta": type("Meta", (), {
                    "serializer_class": serializers[f"{i.__name__}"]
                })
            }
        ) for i in models
}

Mutation = type("Mutation", (graphene.ObjectType,), {
    f"{i.lower()}s": mutations[i].Field() for i in mutations
})
