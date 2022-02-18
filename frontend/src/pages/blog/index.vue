<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "ArticleIndex",
  computed: mapState({
    articles: state => state.blog.articles
  }),
  async mounted() {
    await this.$store.dispatch('blog/getArticlesTop')
  }
}
</script>

<style scoped>

</style>
