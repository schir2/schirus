<template>
  <router-link :to="to" class="link">
    <slot />
  </router-link>
</template>

<script>
export default {
  name: "VLink",
  props: ["to"],
};
</script>

<style scoped></style>
