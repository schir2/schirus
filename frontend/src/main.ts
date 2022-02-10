import App from "@/App.vue";
import {createApp} from "vue";
import router from '@/router'
import store from "@/store";
import { createApolloProvider } from '@vue/apollo-option'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import "normalize.css"
import '@/scss/style.scss'

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
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
app.mount("#app")
