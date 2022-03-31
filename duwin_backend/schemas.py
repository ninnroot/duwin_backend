import graphene
from graphene_django import DjangoObjectType


model_to_graphene = {
    "CharField": {"type": graphene.String, "operators": ["icontains"]},
    "TextField": {"type": graphene.String, "operators": ["icontains"]},
    "DateField": {"type": graphene.Date, "operators": ["lt", "gt", "lte", "gte"]},
    "DateTimeField": {"type": graphene.DateTime, "operators": ["lt", "gt", "lte", "gte"]},
    "BigAutoField": {"type": graphene.Int, "operators": ["lt", "gt", "lte", "gte"]},
    "IntegerField": {"type": graphene.Int, "operators": ["lt", "gt", "lte", "gte"]},
    "URLField": {"type": graphene.String, "operators": ["icontains"]},
    "BooleanField": {"type": graphene.Boolean, "operators": []}
}

banned_fields = [
    "ImageField",
    "ForeignKey",
    "FileField",
    "ManyToManyField",
    "OneToOneField"
]


class BaseType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def resolve(cls, root, info, **kwargs):

        fields = []
        for i in cls._meta.model._meta.get_fields():
            if i.get_internal_type() not in banned_fields:
                fields.append(i.name)
                for j in model_to_graphene[i.get_internal_type()]["operators"]:
                    fields.append(f"{i.name}__{j}")

        filters = {}
        for i in kwargs:
            if i is not None and i in fields:
                filters[i] = kwargs[i]

        return cls._meta.model.objects.filter(**filters).all()

    @classmethod
    def get_filter_fields(cls) -> dict:
        dic = {}

        for i in cls._meta.model._meta.get_fields():
            t = i.get_internal_type()

            if t not in banned_fields:
                dic_result = model_to_graphene[t]
                dic[i.name] = graphene.Argument(dic_result["type"], default_value=None)

                for j in dic_result["operators"]:
                    dic[f"{i.name}__{j}"] = graphene.Argument(dic_result["type"], default_value=None)

        return dic

