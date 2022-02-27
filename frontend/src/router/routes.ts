const routes = [
  {
    path: "/",
    name: "home",
    component: () => import(/* webpackChunkName: "home" */ "@/pages/Home.vue"),
    meta: {
      title: "Home",
      auth: false,
    },
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/pages/Login.vue"),
    meta: {
      title: "Login",
      auth: false,
    },
  },
  {
    path: "/blog",
    name: "blog",
    redirect: { name: "article-list" },
    meta: {
      title: "Blog",
      auth: false,
    },
    component: () =>
      import(/* webpackChunkName: "blog" */ "@/pages/blog/index.vue"),
    children: [
      {
        path: "articles",
        name: "article-list",
        meta: {
          title: "Articles",
          auth: false,
        },
        component: () =>
          import(
            /* webpackChunkName: "articles" */ "@/pages/blog/ArticleListPage.vue"
          ),
      },
      {
        path: "articles/:id",
        name: "article-detail",
        meta: {
          title: "Articles",
          auth: false,
        },
        component: () =>
          import(
            /* webpackChunkName: "article-detail" */ "@/pages/blog/ArticleDetailPage.vue"
          ),
      },
      {
        path: "articles/add",
        name: "article-add",
        meta: {
          title: "Add Article",
          auth: true,
        },
        component: () =>
          import(
            /* webpackChunkName: "article-add" */ "@/pages/blog/ArticleAddPage.vue"
          ),
      },
    ],
  },
  {
    path: "/apps",
    name: "apps",
    meta: {
      title: "Apps",
      auth: false,
    },
    component: () =>
      import(/* webpackChunkName: "apps" */ "@/pages/apps/index.vue"),
    children: [
      {
        path: "pdf-merge",
        name: "pdf-merge",
        meta: {
          title: "PDF Merge",
          auth: false,
        },
        component: () =>
          import(
            /* webpackChunkName: "pdf-merge" */ "@/pages/apps/PDFMerge.vue"
          ),
      },
    ],
  },
  {
    path: "/about",
    name: "about",
    meta: {
      title: "About",
      auth: false,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "@/pages/About.vue"),
  },
];

export default routes;
