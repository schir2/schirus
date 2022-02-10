<template>
<header class="header">
  <h1 v-if="$route.meta.title">{{$route.meta.title}}</h1>
</header>
</template>

<script>
export default {
  name: "TheHeader"
}
</script>

<style scoped>

</style>
