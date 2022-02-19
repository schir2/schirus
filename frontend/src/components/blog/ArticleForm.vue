<template>
  <form>
    <h1>{{article.title ? article.title : 'Enter Article Title'}}</h1>
    <input v-model="article.title">
    <QuillEditor v-model="article.content" theme="snow"/>
    <VButton @click.prevent="save">Save</VButton>
  </form>

</template>

<script>
import Article from "@/models/Article";

export default {
  name: "ArticleForm",
  props: {article: Article},
  computed: {
  },
  methods:{
    save(){
      console.log("Saving Article")
    }
  }
}
</script>

<style scoped>

</style>