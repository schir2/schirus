import {GetterTree} from "vuex";
import {AuthState} from "@/store/auth/state";

export const getters = <GetterTree<AuthState, any>>{
    isLoggedIn: (state: AuthState) => {
        return state.authUser.loggedIn
    }
}