from flask import Flask, request, jsonify
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.String(default_value="stranger"),
        age=graphene.Int()
    )

    def resolve_hello(self, info, name, age):
        return 'Hello ' + name + ', você tem ' + str(age) + ' anos'

schema = graphene.Schema(query=Query)

@app.route("/", methods=['POST'])
def graphql():
    query = request.json['query']
    # data = json.loads(request.data)
    # return json.dumps(schema.execute(data['query']).data)
    return jsonify({'pessoa':schema.execute(query).data})

if __name__ == '__main__':
    app.run(debug=True)

# def main():
#     result = schema.execute('{ hello(name: "Valdir", age: 20) }')
#     print(result.data['hello'])
#
# if __name__ == '__main__':
#     main()
