<template>
  <div>
    <input v-model="username" type="text" />
    <input v-model="password" type="password" />
    <button @click.prevent="login">Login</button>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {},
};
</script>

<style scoped></style>
