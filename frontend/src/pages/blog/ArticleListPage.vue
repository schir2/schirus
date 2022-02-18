<template>
  <div>
    <VLink :to="{name:'article-add'}">Add Article</VLink>
    <ArticleList :articles="articles"></ArticleList>
  </div>
</template>

<script>
import ArticleList from "@/components/blog/ArticleList";
import {mapState} from "vuex";

export default {
  name: "ArticleListPage",
  components: {ArticleList},
  computed: {
    ...mapState({
      articles: state => state.blog.articles
    })
  },
}
</script>

<style scoped>

</style>