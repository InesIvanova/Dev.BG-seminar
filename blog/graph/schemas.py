import graphene

from blog.graph.util import CreateUser
from blog.graph.objects import User


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    user = graphene.Field(User)


schema = graphene.Schema(query=Query, mutation=Mutations)
