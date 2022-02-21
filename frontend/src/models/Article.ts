import User from "@/models/User";
import Category from "@/models/Category";

export class Article {

    id?: number
    slug?: string
    title = ""
    content = ""
    user?: User
    categories: Category[] = []
    likes: User[] = []
    createdOn?: string
    updatedOn?: string

    getAuthor(): string {
        if (this.user?.firstName && this.user?.lastName) {
            return `${this.user.firstName} ${this.user.lastName}`
        }
        return this.user?.username || "No Associated Author"
    }

}

export default Article;