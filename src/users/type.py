from graphene import ObjectType, String, ID, JSONString, Field



class User(ObjectType):
    id = ID()
    email = String()
    password = String()
    form = JSONString()

