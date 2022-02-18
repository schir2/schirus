<template>
  <header class="header">
    <slot></slot>
  </header>
</template>

<script>
export default {
  name: "TheHeader"
}
</script>

<style scoped>
.header {
  text-align: center;
  margin-bottom: 2rem;
}
</style>
