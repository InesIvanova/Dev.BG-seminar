import graphene

from blog.graph.input import IUser
from blog.graph.objects import User


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = IUser(required=True)

    person = graphene.Field(User)

    def mutate(root, info, user_data=None):
        user = User(first_name=user_data.first_name, last_name=user_data.last_name)
        return CreateUser(user)
