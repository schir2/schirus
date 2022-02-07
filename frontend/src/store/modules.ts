import {ModuleTree} from "vuex";
import {RootState} from "@/store/state";
import authStore from "@/store/auth";

export const modules: ModuleTree<RootState> = {
    auth: authStore
}

export default modules
