<template>
  <form v-if="!authUser?.loggedIn" class="auth-small">
    <input
        v-model="username"
        type="text"
    >
    <input
        v-model="password"
        type="password"
    >
    <button
        type="submit"
        @click.prevent="login"
        @keyup.enter="login"
    >
      Login
    </button>
  </form>
  <form v-else>
    <a>{{ authUser.username }}</a>
    <button @click="logout">
      Logout
    </button>
  </form>
</template>

<script setup>
import {computed} from "vue";
import {useAuthStore} from "@/store/AuthStore";

const authStore = useAuthStore()
const authUser = computed(() => {
  return authStore.authUser
})

function login() {
  authStore.login({username: this.username, password: this.password})
}

function logout() {
  authStore.logout()
}
</script>

<style scoped>

</style>