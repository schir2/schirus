<template>
<nav>
  <router-link :to="{name:'home'}">Home</router-link>
  <router-link :to="{name:'blog'}">Blog</router-link>
  <router-link :to="{name:'about'}">About</router-link>
</nav>
</template>

<script>
export default {
  name: "TheNavbar"
}
</script>

<style scoped>

</style>
