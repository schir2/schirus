<template>
  <div>
    <router-link :to="{name:'articleAdd'}">Add</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "ArticleIndex",
  data() {
    return {
      articles: []
    }
  },
}
</script>

<style scoped>

</style>
