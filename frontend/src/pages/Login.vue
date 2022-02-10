<template>
  <div>
    <input type="text" v-model="username">
    <input type="password" v-model="password">
    <button @click.prevent="login">Login</button>
  </div>

</template>

<script>

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
