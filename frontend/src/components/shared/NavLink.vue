<template>
  <router-link class="link" :to="to">
    <slot />
  </router-link>
</template>

<script>
export default {
  name: "NavLink",
  props: ["to"],
};
</script>

<style scoped lang="scss">
.link {
  padding: 0.25rem 0.5rem;
  transition: all 0.1s ease-in;

  &:hover {
    box-shadow: 0 0 0 2px $color-blue;
  }
}

.active {
  border-bottom: 0.2rem solid $color-kobe;
}
</style>
