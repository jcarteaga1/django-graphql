import graphene
from .graphql import schema

class Query(schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
