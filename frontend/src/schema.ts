import gql from "graphql-tag";

export const typeDefs = gql`
type User {
    id: ID!
    username: String!
    firstName: String
    lastName: String
    likes: [Like]
}

type Category {
    id: ID!
    slug: String!
    name: String!
}

type Like {
    user: User!
    article: Article!
    createdOn: String!
    
}

type Article {
    id: ID!
    slug: String!
    title: String!
    content: String!
    user: User!
    categories: [Category]
    likes: [Like]
    createdOn: String!
    updatedOn: String!
}

type Error {
    message: String
    locations: [ErrorLocations]
    path: [String]
}

type ErrorLocations {
    line: Int
    column: Int
}

type TokenAuthResponse {
    success: Boolean
    token: String
    refreshToken: String
    refreshExpiresIn: Int
    errors: [String]
}

type Mutation {
    tokenAuth(username: String!, password: String!): TokenAuthResponse
}

type Query {
    articles: [Article]
}
`
