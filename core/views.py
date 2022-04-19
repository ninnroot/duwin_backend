from duwin_backend.views import BaseView
from .serializers import serializers

views = {
    i: type(
        f"{i}View",
        (BaseView, ),
        {
            "serializer": serializers[i],
            "path": i.lower()+"s"
        }
    ) for i in serializers
}

