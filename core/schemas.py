import graphene
from duwin_backend.schemas import BaseType
from django.apps import apps


Query = type("Query", (graphene.ObjectType,), {
    i.query_name: graphene.List(
        i, resolver=i.resolve, **i.get_filter_fields()
    ) for i in [
        type(f"{j.__name__}Query", (BaseType,), {
            "Meta": type("Meta", (), {"model": j, "exclude": j.excluded_fields}),
            "__doc__": j.__doc__,
            "query_name": f"{j.__name__.lower()}s",
        }) for j in apps.get_app_config("core").get_models()
    ]
})



