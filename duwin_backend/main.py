import graphene
from core.schemas import Query as q
from core.mutations import Mutation as m


class Query(q, graphene.ObjectType):
    pass


class Mutation(m, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query)
