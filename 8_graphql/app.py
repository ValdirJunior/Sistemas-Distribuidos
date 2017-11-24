import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.String(default_value="stranger"),
        age=graphene.Int()
    )

    def resolve_hello(self, info, name, age):
        return 'Hello ' + name + ', você tem ' + str(age) + ' anos'

def main():
    schema = graphene.Schema(query=Query)
    result = schema.execute('{ hello(name: "Valdir" age: 20) }')
    print(result.data['hello'])

if __name__ == '__main__':
    main()
