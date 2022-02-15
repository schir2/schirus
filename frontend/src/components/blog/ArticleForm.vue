<template>
  <form>
    <QuillEditor v-model="article.text" theme="snow"/>
  </form>

</template>

<script>
export default {
  name: "ArticleForm",
  props: ["article"],
  computed: {}
}
</script>

<style scoped>

</style>