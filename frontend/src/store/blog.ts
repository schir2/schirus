import {ActionTree, GetterTree, MutationTree} from "vuex";
import Article from "@/models/Article";
import {apolloClient} from "@/main";
import {GET_ARTICLE_BY_ID, GET_ARTICLE_LIST} from "@/services/apollo/queries";
import {plainToClass} from "class-transformer";

export class BlogState {
    article: Article = new Article()
    articles: Article[] = []
}

const actions = <ActionTree<BlogState, BlogState>>{

    async getArticlesTop({commit}) {
        return apolloClient.query(
            {
                query: GET_ARTICLE_LIST
            }
        ).then(response => {
            console.log(response)
            if (response?.data?.articles)
                commit("setArticles", plainToClass(Article, response.data.articles))
        })

    },

    async getArticle({commit}, id) {
        return apolloClient.query(
            {
                query: GET_ARTICLE_BY_ID,
                variables: {id: id}
            }
        ).then(response => {
            if (response?.data?.article) {
                commit("setArticle", plainToClass(Article, response.data.article))
            }
        })
    }

}
const getters = <GetterTree<BlogState, Article>>{
    getArticle: (state: BlogState) => {
        return state.article
    }
}
const mutations = <MutationTree<BlogState>>{
    setArticles(state, articles: Article[]) {
        state.articles = articles
    },
    setArticle(state, article: Article) {
        state.article = article
    }
}
const blogStore = {
    namespaced: true,
    state: new BlogState(),
    actions: actions,
    mutations: mutations,
    getters: getters
};

export default blogStore;
