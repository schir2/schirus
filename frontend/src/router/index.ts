import {createRouter, createWebHistory} from "vue-router";
import routes from "@/router/routes";
import store from "@/store";

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
    linkActiveClass: "active",
    linkExactActiveClass: "exact-active",
})

router.beforeEach((to, from, next) => {

    if (to.meta.auth && !store.state.auth.authUser.loggedIn) {
        next({name: 'login'})
    } else {
        next()
    }
});

router.afterEach((to, from, next) => {
    document.title = typeof (to.meta.title) === "string" ? to.meta.title : 'schir.us';
});

export default router
