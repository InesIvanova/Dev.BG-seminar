import graphene

from blog.blog_post import db
from blog.graph.input import IUser
from blog.graph.objects import User
from blog.utils.exceptions import InvalidInput
from blog.utils.validation_helpers import validate_email
from blog.utils.db_helpers import save_user, save_email


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = IUser(required=True)

    person = graphene.Field(User)

    @validate_email
    def mutate(root, info, user_data=None):
        user = User(first_name=user_data.first_name, last_name=user_data.last_name)
        user_pk = save_user(user)
        save_email(user_data.email, user_pk)
        db.session.commit()
        return CreateUser(user)
