import {createStore, ModuleTree} from "vuex";
import authStore, {AuthState} from "@/store/auth";
import blogStore, {BlogState} from "@/store/blog";


export interface RootState {
    auth: AuthState
    blog: BlogState
}

const modules: ModuleTree<RootState> = {
    auth: authStore,
    blog: blogStore
}
export const store = createStore<RootState>({
    modules: modules
})

export default store