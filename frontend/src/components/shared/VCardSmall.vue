<template>
  <div class="card">
    <div class="heading">
      <slot name="heading" />
    </div>
    <slot />
  </div>
</template>

<script>
export default {
  name: "VCardSmall"
}
</script>

<style scoped lang="scss">
.card {
  box-shadow: $shadow-1;
  margin: .5rem;
  padding: .5rem;
  max-width: 70rem;
  display: flex;
  flex-direction: column;
  gap: .5rem;
  transition: all 1s ease;

  @media (max-width: 35rem) {
    margin: 0;
  }
}

.heading {
  border-bottom: 1px solid $color-light-gray;
  display: flex;
  justify-content: space-between;
  padding: 1rem;

  @media (max-width: 35rem) {
    flex-direction: column;
    gap: 1rem;

  }
}

</style>
