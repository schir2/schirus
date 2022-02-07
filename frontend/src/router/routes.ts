const routes = [

    {
        path: '/',
        name: 'home',
        component: () => import(/* webpackChunkName: "home" */ "@/pages/Home.vue"),
        meta: {
            title: "Home",
            auth: false,
        }
    },
    {
        path: '/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "login" */ "@/pages/Login.vue"),
        meta: {
            title: "Login",
            auth: false,
        }
    },
    {
        path: '/blog',
        name: 'blog',
        meta: {
            title: "Blog",
            auth: false,
        },
        component: () => import(/* webpackChunkName: "blog" */ "@/pages/blog/index.vue")
    },
    {
        path: '/about',
        name: 'about',
        meta: {
            title: "About",
            auth: false,
        },
        component: () => import(/* webpackChunkName: "blog" */ "@/pages/About.vue")
    }
]

export default routes
