import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";
import { apolloClient } from "@/main";
import gql from "graphql-tag";
import { AuthUser } from "@/models/AuthUser";
import { plainToClass } from "class-transformer";

const authService = {
  AuthStorage: LocalAuthStorage,

  getAccessToken(): string {
    return this.AuthStorage.getAuthUser().token;
  },

  getRefreshToken(): string {
    return this.AuthStorage.getAuthUser().refreshToken;
  },

  setAccessToken(access: string): void {
    const authUser = this.AuthStorage.getAuthUser();
    authUser.token = access;
    this.AuthStorage.setAuthUser(authUser);
  },

  async login(username: string, password: string): Promise<AuthUser> {
    const response = await apolloClient.mutate({
      mutation: gql`
        mutation ($username: String!, $password: String!) {
          tokenAuth(username: $username, password: $password) {
            success
            errors
            token
            refreshToken
          }
        }
      `,
      variables: {
        username: username,
        password: password,
      },
    });
    if (response.data) {
      const authUser = plainToClass(AuthUser, {
        username: username,
        loggedIn: true,
        token: response.data.tokenAuth.token,
        refreshToken: response.data.tokenAuth.refreshToken,
      });

      this.AuthStorage.setAuthUser(authUser);
      return Promise.resolve(authUser);
    }
    return Promise.reject(response.errors);
  },
  logout(): void {
    this.AuthStorage.removeAuthUser();
  },
};

export default authService;
