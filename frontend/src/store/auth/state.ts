import {AuthUser} from "@/models/AuthUser";
import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";

export class AuthState {
    authUser: AuthUser = LocalAuthStorage.getAuthUser()
}