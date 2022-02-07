import {AuthUser} from "@/models/AuthUser";
import AuthStorage from "@/storage/auth/types";

class LocalAuthStorage implements AuthStorage{

    getAuthUser() :AuthUser {
        const data = localStorage.getItem("AuthUser")
        if (data){
            return JSON.parse(data)
        }
        return new AuthUser()
    }

    setAuthUser(AuthUser: AuthUser) {
        localStorage.setItem("User", JSON.stringify(AuthUser));
    }

    removeAuthUser() {
        localStorage.removeItem("AuthUser");
    }
}

export default new LocalAuthStorage()
