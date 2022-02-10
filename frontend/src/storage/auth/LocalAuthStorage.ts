import {AuthUser} from "@/models/AuthUser";
import AuthStorage from "@/storage/auth/types";
import {plainToClass} from "class-transformer"

class LocalAuthStorage implements AuthStorage{
    storageObjectName: string = 'authUser'

    getAuthUser() :AuthUser {
        const data = localStorage.getItem(this.storageObjectName)
        if (data){
            return plainToClass(AuthUser, JSON.parse(data))
        }
        return new AuthUser()
    }

    setAuthUser(AuthUser: AuthUser) {
        localStorage.setItem(this.storageObjectName, JSON.stringify(AuthUser));
    }

    removeAuthUser() {
        localStorage.removeItem(this.storageObjectName);
    }
}

export default new LocalAuthStorage()
