<template>
  <div>
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
