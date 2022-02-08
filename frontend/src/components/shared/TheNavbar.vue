<template>
<nav>
  <router-link class="link" :to="{name:'home'}">Home</router-link>
  <router-link class="link" :to="{name:'blog'}">Blog</router-link>
  <router-link class="link" :to="{name:'about'}">About</router-link>
</nav>
</template>

<script>
export default {
  name: "TheNavbar"
}
</script>

<style scoped lang="scss">
nav{
  display: flex;
  justify-content: center;
}
</style>
