import App from "@/App.vue";
import {createApp} from "vue";
import 'reflect-metadata'
import router from '@/router'
import store from "@/store";
import { createApolloProvider } from '@vue/apollo-option'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import "normalize.css"
import '@/scss/style.scss'
import VueToast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

const cache = new InMemoryCache()

export const apolloClient = new ApolloClient({
  cache,
  uri: 'http://localhost:8000',
})

const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})

const app = createApp(App)

app.use(router)
app.use(store)
app.use(apolloProvider)
app.use(VueToast)
app.mount("#app")
