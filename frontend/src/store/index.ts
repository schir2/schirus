import {createStore} from "vuex";
import {RootState} from "@/store/state";
import {modules} from "@/store/modules";


export const store = createStore<RootState>({
    modules: modules
})

export default store
