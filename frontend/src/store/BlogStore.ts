import Article from "@/models/Article";
import {apolloClient} from "@/main";
import {GET_ARTICLE_BY_ID, GET_ARTICLE_LIST} from "@/services/apollo/queries";
import {plainToClass} from "class-transformer";
import {defineStore} from "pinia";

interface BlogState {
    article: Article
    articles: Article[]
}

export const useBlogStore = defineStore("BlogStore", {
    state: (): BlogState => {
        return {
            article: new Article(),
            articles: []
        }
    },
    actions: {
        async getArticlesTop() {
            try {
                this.articles = (await apolloClient.query(
                    {
                        query: GET_ARTICLE_LIST
                    })).data.articles
            } catch (error) {
                console.error(error)
            }
        },
        async getArticle(id: string) {
            try {
                this.article = plainToClass(Article, (await apolloClient.query(
                    {
                        query: GET_ARTICLE_BY_ID,
                        variables: {id: id}
                    }
                )).data.article)
            } catch (error) {
                console.error(error)
            }
        }
    },
    getters: {
        getArticle(): Article {
            return this.article
        }
    }
})