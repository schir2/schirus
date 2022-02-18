<template>
  <form>
    <h1>{{article.title ? article.title : 'Enter Article Title'}}</h1>
    <input v-model="article.title">
    <QuillEditor v-model="article.content" theme="snow"/>
  </form>

</template>

<script>
import {mapState} from "vuex";

export default {
  name: "ArticleForm",
  computed: {
    ...mapState({
      article: state => state.blog.article
    })
  }
}
</script>

<style scoped>

</style>