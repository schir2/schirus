<script setup>
import {computed, onMounted} from "vue"
import {useStore} from "vuex"
import ArticleList from "@/components/blog/ArticleList.vue";

const store = useStore()
onMounted(async () => {
  await store.dispatch('blog/getArticlesTop')
})
const articles = computed(() => store.state.blog.articles)

</script>
<template>
  <div>
    <VLink :to="{name:'article-add'}">
      Add Article
    </VLink>

    <ArticleList :articles="articles"/>

  </div>
</template>