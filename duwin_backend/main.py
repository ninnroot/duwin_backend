import graphene
from core.schemas import Query as q

class Query(q,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)