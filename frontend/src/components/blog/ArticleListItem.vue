<template>
  <ul class="article-list-item">
    <li class="title">{{article.title}}</li>
    <li class="user">{{article.user.username}}</li>
    <li class="likes">{{article.likes.length}}</li>
    <li class="created-on">{{article.createdOn}}</li>
    <li class="categories">
      <span class="category" v-for="category in article.categories" :key="category.id">
        {{category.name}}
      </span>
    </li>
    <li class="actions"></li>
  </ul>

</template>

<script>
export default {
  name: "ArticleListItem",
  props: ["article"]
}
</script>

<style scoped lang="scss">
.article-list-item{
  display: grid;
  grid-template-areas:
      "title title title actions"
      "categories categories categories actions"
      "user created-on likes actions"
;
  background-color: red;
}
.title{grid-area:title}
.user{grid-area:user}
.likes{grid-area:likes}
.created-on{grid-area:created-on}
.categories{grid-area:categories}
.actions{grid-area:actions}

</style>