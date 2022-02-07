import {AuthUser} from "@/models/AuthUser";
import LocalAuthStorage from "@/storage/auth/LocalAuthStorage";

class AuthState {
    authUser: AuthUser = LocalAuthStorage.getAuthUser()
}
export default AuthState
