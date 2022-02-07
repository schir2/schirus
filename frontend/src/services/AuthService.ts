import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";



const authService = {
    AuthStorage: LocalAuthStorage,
    BASE_URL: process.env('BASE_URL'),

    getAccessToken(): string {
        return this.AuthStorage.getAuthUser().access
    },

    getRefreshToken(): string {
        return this.AuthStorage.getAuthUser().refresh
    },

    setAccessToken(access: string) {
        const authUser = this.AuthStorage.getAuthUser()
        authUser.access = access;
        this.AuthStorage.setAuthUser(authUser)
    },

    async login(username: string, password: string) {
    },
    async logout() {
        //TODO Implement server logout
        this.AuthStorage.removeAuthUser()
    },

    async refresh() {

    }
}

export default authService