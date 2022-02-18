<template>
  <div v-if="article">
    <TheHeader><h1>{{ article.title }}</h1></TheHeader>
    <h2 v-if="article.user">Written by {{ article.user.username }}</h2>
    <article v-if="article.content" v-html="article.content">
    </article>

  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "ArticleDetailPage",
  computed: {
    ...mapState({
      article: state => state.blog.article
    })
  },
  mounted() {
    this.$store.dispatch("blog/getArticle", this.$route.params.id)
  }
}
</script>

<style scoped>

</style>
