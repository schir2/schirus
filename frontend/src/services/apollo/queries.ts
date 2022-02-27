import gql from "graphql-tag";

export const GET_ARTICLE_LIST = gql`
  query {
    articles {
      id
      slug
      title
      content
      categories {
        id
        slug
        name
      }
      createdOn
      updatedOn
      likes {
        user {
          id
          username
        }
        createdOn
      }
      user {
        username
        firstName
        lastName
      }
    }
  }
`;
export const GET_ARTICLE_BY_ID = gql`
  query ($id: String!) {
    article(id: $id) {
      id
      slug
      title
      content
      categories {
        id
        slug
        name
      }
      createdOn
      updatedOn
      likes {
        user {
          id
          username
        }
        createdOn
      }
      user {
        username
        firstName
        lastName
      }
    }
  }
`;
