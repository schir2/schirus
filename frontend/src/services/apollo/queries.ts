import gql from "graphql-tag";

export const GET_ARTICLE_LIST = gql`
    query {
        articles{
            id,
            slug,
            title,
            content,
            categories {
                id,
                slug,
                name
            },
            createdOn,
            updatedOn,
            likes {
                user {id, username}
                createdOn
            }
        }
    }
`