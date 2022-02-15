<template>
  <div class="article-list">
    <ArticleListItem v-for="article in articles" :key="article.id" :article="article"></ArticleListItem>
  </div>
</template>

<script>
import ArticleListItem from "@/components/blog/ArticleListItem";

export default {
  name: "ArticleList",
  components: {ArticleListItem},
  props: ["articles"]
}
</script>

<style scoped>

</style>