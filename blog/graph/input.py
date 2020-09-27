import graphene


class Iphone(graphene.InputObjectType):
    type = graphene.String()
    country_code = graphene.String(required=True)
    number = graphene.Int(required=True)
    extension = graphene.Int()
    is_primary = graphene.Boolean(default=True)


class IEmail(graphene.InputObjectType):
    type = graphene.String()
    email = graphene.String(required=True)
    is_primary = graphene.Boolean(default_value=True)


class IUser(graphene.InputObjectType):
    title = graphene.String()
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    phone = Iphone()
    email = IEmail()
