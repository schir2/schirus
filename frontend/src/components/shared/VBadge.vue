<template>
  <span class="badge"><slot></slot></span>
</template>

<script>
export default {
  name: "VBadge"
}
</script>

<style scoped lang="scss">
.badge {
  color: $color-light;
  background-color: $color-blue;
  padding: .25rem;
}

</style>