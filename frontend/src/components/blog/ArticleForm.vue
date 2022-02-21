<template>
  <form>
    <h1>{{ article.title ? article.title : 'Enter Article Title' }}</h1>
    <input v-model="article.title">
    <QuillEditor
        v-model="article.content"
        theme="snow"
    />
    <VButton @click.prevent="save">
      Save
    </VButton>
  </form>
</template>

<script setup>
import {useStore} from "vuex";
import {computed} from "vue";

const store = useStore()
const article = computed(() => store.state.blog.article)

</script>

<style scoped>

</style>