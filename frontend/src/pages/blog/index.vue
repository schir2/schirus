<template>
  <div>
    <router-link :to="{name:'articleAdd'}">Add</router-link>

    <ArticleList :articles="articles"></ArticleList>
  </div>
</template>

<script>
import ArticleList from "@/components/blog/ArticleList";
import {mapState} from "vuex";

export default {
  name: "ArticleIndex",
  components: {ArticleList},
  computed: mapState({
    articles: state => state.blog.articles
  }),
  async mounted() {
    await this.$store.dispatch('blog/getListTop')
  }
}
</script>

<style scoped>

</style>
