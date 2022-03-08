import Article from "@/models/Article"
import {apolloClient} from "@/main"
import {GET_ARTICLE_BY_ID, GET_ARTICLE_LIST} from "@/services/apollo/queries"
import {plainToInstance} from "class-transformer"
import {defineStore} from "pinia"

interface BlogState {
    article: Article | null
    articles: Article[]
}

export const useBlogStore = defineStore("BlogStore", {
    state: (): BlogState => {
        return {
            article: new Article(),
            articles: [],
        }
    },
    actions: {
        async getArticlesTop() {
            try {
                this.articles = plainToInstance(
                    Article,
                    (await apolloClient.query({
                        query: GET_ARTICLE_LIST,
                    })
                ).data.articles as Article[])
            } catch (error) {
                console.error(error)
            }
        },
        async getArticle(id: string) {
            try {
                this.article = plainToInstance(
                    Article,
                    (
                        await apolloClient.query({
                            query: GET_ARTICLE_BY_ID,
                            variables: {id: id},
                        })
                    ).data.article
                )
            } catch (error) {
                console.error(error)
            }
        },
    },
})
