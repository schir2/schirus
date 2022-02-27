<template>
  <span class="badge"><slot /></span>
</template>

<script>
export default {
  name: "VBadge",
};
</script>

<style scoped lang="scss">
.badge {
  color: $color-light;
  background-color: $color-red;
  padding: 0.25rem 0.5rem;
  margin-inline: 0.1rem;
}
</style>
