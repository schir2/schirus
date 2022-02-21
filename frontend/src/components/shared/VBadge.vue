<template>
  <span class="badge"><slot /></span>
</template>

<script>
export default {
  name: "VBadge"
}
</script>

<style scoped lang="scss">
.badge {
  color: $color-light;
  background-color: $color-red;
  padding: .25rem .5rem;
  margin-inline: .1rem;
}

</style>