<template>
  <nav class="secondary-nav">
    <NavLink :to="{name:'pdf-merge'}">PDF Merge</NavLink>
    <router-view/>
  </nav>

</template>

<script>
import NavLink from "@/components/shared/NavLink";
export default {
  name: "index",
  components: {NavLink}
}
</script>

<style scoped>
.secondary-nav{
  display: flex;
  justify-content: center;
}

</style>