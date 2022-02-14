import {ActionTree, GetterTree, MutationTree} from "vuex";
import Article from "@/models/Article";

export class BlogState {
    article: Article = new Article()
}

const actions = <ActionTree<BlogState, any>>{}
const getters = <GetterTree<BlogState, any>>{
    getArticle: (state: BlogState) => {
        return state.article
    }
}
const mutations = <MutationTree<BlogState>>{}
const blogStore = {
    namespaced: true,
    state: new BlogState(),
    actions: actions,
    mutations: mutations,
    getters: getters
};

export default blogStore;
