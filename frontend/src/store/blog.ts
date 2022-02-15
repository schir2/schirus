import {ActionTree, GetterTree, MutationTree} from "vuex";
import Article from "@/models/Article";
import User from "@/models/User";
import {apolloClient} from "@/main";
import {GET_ARTICLE_LIST} from "@/services/apollo/queries";

export class BlogState {
    article: Article = new Article()
    articles: Article[] = []
}

const actions = <ActionTree<BlogState, any>>{

    async getListTop({commit}) {
        console.log("pre query")
        return apolloClient.query(
            {
                query: GET_ARTICLE_LIST
            }
        ).then(response => {
            console.log(response)
            commit("getList", response)
        })

    },
    async getListByUser(state, user: User) {
    },

}
const getters = <GetterTree<BlogState, any>>{
    getArticle: (state: BlogState) => {
        return state.article
    }
}
const mutations = <MutationTree<BlogState>>{
    getList(state, articles: Article[]){
        state.articles = articles
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
