<template>
  <form v-if="!authUser?.loggedIn" class="auth-small">
    <input v-model="username" type="text" />
    <input v-model="password" type="password" />
    <button type="submit" @click.prevent="login" @keyup.enter="login">
      Login
    </button>
  </form>
  <form v-else>
    <a>{{ authUser.username }}</a>
    <button @click="logout">Logout</button>
  </form>
</template>

<script setup lang="ts">
import { computed, ref } from "vue"
import { useAuthStore, AuthUserInput } from "@/store/AuthStore"

const authStore = useAuthStore()
const authUser = computed(() => {
  return authStore.authUser
})
const username = ref("")
const password = ref("")

const login = () => {
  const userInput: AuthUserInput = {username: username.value, password: password.value}
  authStore.login(userInput)
}

function logout() {
  authStore.logout()
}
</script>

<style scoped></style>
