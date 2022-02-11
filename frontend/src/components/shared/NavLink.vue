<template>
  <router-link class="link" :to="to"><slot></slot></router-link>

</template>

<script>
export default {
  name: "NavLink",
  props: ["to"]
}
</script>

<style scoped lang="scss">
  .link {
    padding: .25rem .5rem;
    transition: all .1s ease-in;

    &:hover {
      box-shadow: 0 0 0 2px $color-blue;
    }
  }

  .active {
    border-bottom: .2rem solid $color-kobe;
  }

</style>