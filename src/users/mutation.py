import graphene

from type import User

class CreateUser(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        email = graphene.String()
        password = graphene.String()
        form = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, email, password, form):
        user = User(id=id, email=email, password=password, form=form)