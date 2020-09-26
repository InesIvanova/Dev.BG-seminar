import graphene


class Phone(graphene.ObjectType):
    type = graphene.String()
    country_code = graphene.String()
    number = graphene.Int()
    extension = graphene.Int()
    is_primary = graphene.Boolean()


class Email(graphene.ObjectType):
    type = graphene.String()
    email = graphene.String()
    is_primary = graphene.Boolean()


class User(graphene.ObjectType):
    pk = graphene.Int()
    title = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    phones = graphene.List(Phone)
    emails = graphene.List(Email)
