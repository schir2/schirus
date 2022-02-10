import {AuthState} from "@/store/auth/state";
import {mutations} from "@/store/auth/mutations";
import {actions} from "@/store/auth/actions";
import {getters} from "@/store/auth/getters";

const authStore = {
    namespaced: true,
    state: new AuthState(),
    actions: actions,
    mutations: mutations,
    getters: getters
};

export default authStore;
