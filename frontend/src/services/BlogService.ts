import {apolloClient} from "@/main";
import gql from "graphql-tag";


const blogService = {
    async getList() {
        const response = await apolloClient.query(
            {
                query: gql`
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
            }
        )
        console.log(response)
        return Promise.resolve(response)
    },
}

export default blogService