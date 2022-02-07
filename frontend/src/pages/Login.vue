<template>
  <div>
    <h1>Login</h1>
    <input type="text" v-model="username">
    <input type="password" v-model="password">
    <button @click.prevent="login">Login</button>
  </div>

</template>

<script>
import gql from 'graphql-tag'

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    async login() {
      const result = await this.$apollo.mutate({
        mutation: gql`mutation ($username: String!, $password: String!){
        tokenAuth(username: $username, password: $password){
            success,
            errors,
            token,
            refreshToken  }}`,
        variables: {
          username: this.username,
          password: this.password
        }
      })
      console.log(result)
    }
  }
}
</script>

<style scoped>

</style>
