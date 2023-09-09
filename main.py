from graphene import Schema, ObjectType, String

class Query(ObjectType):

    query = String(name = String(default_value = '<Need to insert a Name>'))
    hello = String(name = String(default_value = 'World'))

    def resolve_query(self, info, name):
        return f'Hello {name}'
    
    def resolve_hello(self, info, name):
        return f'Hello {name}'

schema = Schema(query= Query)

gql = '''
        {
            query(name:"Midhilesh"),
            hello
        }
      '''

if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)
    print(result.errors)
    print(result.data['hello'])
    print(result.data['query'])