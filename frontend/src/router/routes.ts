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
        component: () => import(/* webpackChunkName: "blog" */ "@/pages/blog/index.vue"),
        children: [
            {
                path: 'articles',
                name: 'articleList',
                meta: {
                    title: 'Articles',
                    auth: false,
                },
                component: () => import(/* webpackChunkName: "articles" */ "@/pages/blog/ArticleListPage.vue")
            },
            {
                path: 'articles/$id',
                name: 'articleDetail',
                meta: {
                    title: 'Articles',
                    auth: false,
                },
                component: () => import(/* webpackChunkName: "articleDetail" */ "@/pages/blog/ArticleDetailPage.vue")
            }

        ]
    },
    {
        path: '/apps',
        name: 'apps',
        meta: {
            title: "Apps",
            auth: false,
        },
        component: () => import(/* webpackChunkName: "blog" */ "@/pages/apps/index.vue"),
        children: [
            {
                path: 'pdf-merge',
                name: 'pdf-merge',
                meta: {
                    title: "PDF Merge",
                    auth: false,
                },
                component: () => import(/* webpackChunkName: "blog" */ "@/pages/apps/PDFMerge.vue"),
            }
        ]


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
