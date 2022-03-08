<script setup type="ts" async>
import ArticleList from "@/components/blog/ArticleList.vue";
import {useBlogStore} from "@/store/BlogStore";

const blogStore = useBlogStore()
await blogStore.getArticlesTop()
const articles = blogStore.articles
</script>
<template>
  <div>
    <VLink :to="{ name: 'article-add' }"> Add Article</VLink>
    <suspense>
      <ArticleList :articles="articles"/>
    </suspense>
  </div>
</template>
