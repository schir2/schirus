<template>
  <div v-if="!auth.authUser?.loggedIn" class="auth-small">
    <input type="text" v-model="username">
    <input type="password" v-model="password">
    <button @click.prevent="onClickLogin">Login</button>
  </div>
  <div v-else>
    {{auth.authUser}}
  </div>

</template>

<script>
import {mapGetters, mapState} from "vuex";

export default {
  name: "LoginSmall",
  data(){
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
    onClickLogin(){
      this.$store.dispatch('auth/login', {username: this.username, password: this.password})
    }
  }
}
</script>

<style scoped>

</style>