import App from "@/App.vue"
import {createApp} from "vue"
import 'reflect-metadata'
import router from '@/router'
import store from "@/store"
import VueToast from 'vue-toast-notification'

import {createApolloProvider} from '@vue/apollo-option'
import {ApolloClient, InMemoryCache} from '@apollo/client/core'
import {QuillEditor} from "@vueup/vue-quill"
import AuthSmall from "@/components/shared/AuthSmall.vue"
import NavLink from "@/components/shared/NavLink.vue"
import TheHeader from "@/components/shared/TheHeader.vue"
import PrimaryNav from "@/components/shared/PrimaryNav.vue"
import VLink from "@/components/shared/VLink.vue"
import VCardSmall from "@/components/shared/VCardSmall.vue"
import VButton from "@/components/shared/VButton.vue"
import VBadge from "@/components/shared/VBadge.vue"

// CSS Imports
import "normalize.css"
import "animate.css"
import '@/scss/style.scss'
import 'vue-toast-notification/dist/theme-sugar.css'
import 'material-icons/iconfont/material-icons.css'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

const typeDefs = require("@/services/apollo/schema.ts")


const cache = new InMemoryCache()

export const apolloClient = new ApolloClient({
    cache,
    uri: 'http://localhost:8000',
    typeDefs
})

const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
})

const app = createApp(App)

app.component('QuillEditor', QuillEditor)
app.component('AuthSmall', AuthSmall)
app.component('NavLink', NavLink)
app.component('TheHeader', TheHeader)
app.component('PrimaryNav', PrimaryNav)
app.component('VCardSmall', VCardSmall)
app.component('VLink', VLink)
app.component('VButton', VButton)
app.component('VBadge', VBadge)

app.use(router)
app.use(store)
app.use(apolloProvider)
app.use(VueToast)
app.mount("#app")
