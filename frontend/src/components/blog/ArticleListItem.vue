<template>
  <VCardSmall class="article-list-item">
    <template #heading>
      <VLink :to="{name:'article-detail', params: {id: article.id}}"><h2 class="title">{{ article.title }}</h2></VLink>
      <div class="categories">
        <VBadge v-for="category in article.categories" :key="category.id">
          {{ category.name }}
        </VBadge>
      </div>
    </template>

    <div class="content">
      <div class="authored">by:<span class="author">{{ article.user.username }}</span> {{ createdOn }}</div>
      <span class="likes">
        <span>{{ article.likes.length }}</span>
        <i class="material-icons">favorite</i>
      </span>
    </div>
  </VCardSmall>

</template>

<script>
import {formatDate} from "@/helpers";

export default {
  name: "ArticleListItem",
  props: ["article"],
  computed: {
    createdOn() {
      return formatDate(this.article.createdOn)
    }
  }
}
</script>

<style scoped lang="scss">
.authored {
  display: flex;
  gap: 1ch;
}

.author {
  font-weight: bold;
}

.content {
  display: flex;
  padding: .5rem;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.likes{
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 1ch;
}

</style>