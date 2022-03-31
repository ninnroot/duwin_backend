from graphene_django.rest_framework.mutation import SerializerMutation


class BaseMutation(SerializerMutation):
    class Meta:
        abstract = True
