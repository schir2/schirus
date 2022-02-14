<template>
  <form>
    <QuillEditor v-model="article.text" theme="snow"/>
  </form>

</template>

<script>
export default {
  name: "ArticleForm",
  computed: {}
}
</script>

<style scoped>

</style>