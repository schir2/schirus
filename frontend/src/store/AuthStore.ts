import { AuthUser } from "@/models/AuthUser";
import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";
import authService from "@/services/AuthService";
import { defineStore } from "pinia";

export interface AuthUserInput {
  username: string;
  password: string;
}

export const useAuthStore = defineStore("AuthStore", {
  state: () => {
    return {
      authUser: LocalAuthStorage.getAuthUser(),
    };
  },
  actions: {
    async login(userInput: AuthUserInput) {
      try {
        this.authUser = await authService.login(
          userInput.username,
          userInput.password
        );
      } catch (error) {
        return error;
      }
    },
    logout() {
      authService.logout();
      this.authUser = new AuthUser();
    },
  },
  getters: {
    isLoggedIn: (state) => {
      return state.authUser.loggedIn;
    },
  },
});
