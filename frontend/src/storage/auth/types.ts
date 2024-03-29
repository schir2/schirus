import { AuthUser } from "@/models/AuthUser";

export interface AuthStorage {
  storageObjectName: string;
  getAuthUser(): AuthUser;
  setAuthUser(authUser: AuthUser): void;
  removeAuthUser(authUser: AuthUser): void;
}

export default AuthStorage;
