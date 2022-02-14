<template>
  <ArticleList :articles="articles"></ArticleList>
</template>

<script>
import ArticleList from "@/components/blog/ArticleList";

export default {
  name: "ArticleListPage",
  components: {ArticleList},
  data() {
    return {
      articles: []
    }
  }
}
</script>

<style scoped>

</style>