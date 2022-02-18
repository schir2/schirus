<template>
  <div v-if="article">
    <TheHeader><h1>{{ article.title }}</h1></TheHeader>
    <ul class="categories"><VBadge v-for="category in article.categories" :key="category.id" :category="category">{{category.name}}</VBadge></ul>
    <span v-if="article.user">Written by <span class="author">{{ article.user.username }}</span></span>
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

<style scoped lang="scss">
.categories{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: .25rem;
  margin-bottom:1.5rem;

}
.author{
  font-weight: bold;
}


</style>
