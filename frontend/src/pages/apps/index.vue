<template>
  <div>
    <nav class="secondary-nav">
      <NavLink :to="{name:'pdf-merge'}">PDF Merge</NavLink>
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: "index",
}
</script>

<style scoped>
.secondary-nav {
  display: flex;
  justify-content: center;
}

</style>