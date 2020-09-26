from flask_graphql import GraphQLView

from blog.blog_post import app
from blog.graph.schemas import schema


app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()
