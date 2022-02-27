<script setup type="ts">
import {computed, onMounted} from "vue"
import ArticleList from "@/components/blog/ArticleList.vue";
import {useBlogStore} from "@/store/BlogStore";

const blogStore = useBlogStore()

onMounted(async () => {
  await blogStore.getArticlesTop()
})
const articles = computed(() => blogStore.articles)
</script>
<template>
  <div>
    <VLink :to="{ name: 'article-add' }"> Add Article </VLink>

    <ArticleList :articles="articles" />
  </div>
</template>
