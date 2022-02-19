<template>
  <div>
    <VLink :to="{name:'article-add'}">Add Article</VLink>
    <Suspense>
      <template #default>
        <ArticleList :articles="articles"></ArticleList>
      </template>
      <template #fallback>
        <div>Loading</div>
      </template>
    </Suspense>
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