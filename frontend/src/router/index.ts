import {createRouter, createWebHistory} from "vue-router";
import routes from "@/router/routes";
import {useAuthStore} from "@/store/AuthStore";

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
    linkActiveClass: "active",
    linkExactActiveClass: "exact-active",
})

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore()
    if (to.meta.auth && !authStore.isLoggedIn) {
        next({name: 'login'})
    } else {
        next()
    }
});

router.afterEach((to, from, next) => {
    document.title = typeof (to.meta.title) === "string" ? to.meta.title : 'schir.us';
});

export default router
