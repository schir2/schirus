import User from "@/models/User";
import Category from "@/models/Category";

export class Article {

    id?: number
    slug?: string
    title: string = ""
    content: string = ""
    user?: User
    categories: Category[] = []
    likes: User[] = []
    createdOn?: string
    updatedOn?: string

}
export default Article;