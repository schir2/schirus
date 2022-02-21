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
import {computed} from "vue";
import {useBlogStore} from "@/store/BlogStore";
const blogStore = useBlogStore

const article = computed(() => blogStore.article)

</script>

<style scoped>

</style>