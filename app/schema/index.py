import strawberry
from strawberry.fastapi import  GraphQLRouter
from schema.query import Query
from schema.mutation import Mutation

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)