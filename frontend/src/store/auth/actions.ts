import {ActionTree, Commit} from "vuex";
import {AuthState} from "@/store/auth/state";
import authService from "@/services/AuthService";

export const actions = <ActionTree<AuthState, any>>{

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
    },
    setAccessToken({commit}, accessToken) {
    },
}