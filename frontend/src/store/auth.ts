import {AuthUser} from "@/models/AuthUser";
import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";
import {ActionTree, Commit, GetterTree, MutationTree} from "vuex";
import authService from "@/services/AuthService";

export class AuthState {
    authUser: AuthUser = LocalAuthStorage.getAuthUser()
}

const actions = <ActionTree<AuthState, any>>{

    async login({commit}: { commit: Commit }, userInput) {
        authService.login(userInput.username, userInput.password).then(
            function resolve(authUser) {
                console.info("Login Successful", authUser)
                commit("loginSuccess", authUser)
            },
            function reject(error) {
                console.warn("Login Failed", error)
                commit("loginFailure", error)
            }
        ).catch((error) => {
                console.error("Login Failed due to server error")
                commit("loginFailure", error)
            }
        )
    },
    logout({commit}: { commit: Commit }) {
        authService.logout()
        commit('logout')
    },
}
const getters = <GetterTree<AuthState, any>>{
    isLoggedIn: (state: AuthState) => {
        return state.authUser.loggedIn
    }
}
const mutations = <MutationTree<AuthState>>{
    loginSuccess(state, authUser) {
        state.authUser = authUser;
    },
    loginFailure(state) {
        state.authUser = new AuthUser()
    },
    logout(state) {
        state.authUser = new AuthUser()
    },
    setAccessToken(state, accessToken) {
        state.authUser.loggedIn = true;
        state.authUser.token = accessToken
    },
}
const authStore = {
    namespaced: true,
    state: new AuthState(),
    actions: actions,
    mutations: mutations,
    getters: getters
};

export default authStore;
