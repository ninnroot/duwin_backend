# WARNING
# this is written as an experiment and should probably never put into practice. 
# Such a piece of code would be very difficult to read and hard to maintain in a real-world scenario.
# (quite flexible though if you know enough Python and Django)

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



