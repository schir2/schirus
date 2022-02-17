<template>
  <form v-if="!auth.authUser?.loggedIn" class="auth-small">
    <input type="text" v-model="username">
    <input type="password" v-model="password">
    <button type="submit" @click.prevent="login" @keyup.enter="login">Login</button>
  </form>
  <form v-else>
    <a>{{ auth.authUser.username }}</a>
    <button @click="logout">Logout</button>
  </form>

</template>

<script>
import {mapGetters, mapState} from "vuex";

export default {
  name: "AuthSmall",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  computed: {
    ...mapState({
      auth: state => state.auth
    }),
    ...mapGetters([
      'auth/isLoggedIn',
    ])
  },
  methods: {
    login() {
      this.$store.dispatch('auth/login', {username: this.username, password: this.password})
    },
    logout() {
      this.$store.dispatch('auth/logout')
    }
  }
}
</script>

<style scoped>

</style>