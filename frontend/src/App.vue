<template>
  <div>
    <PrimaryNav />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>
<script>

import PrimaryNav from "@/components/shared/PrimaryNav";

export default {
  name: "App",
  components: {PrimaryNav},
}
</script>
<style lang="scss">
.content{
  max-width: 70rem;
  margin:0 auto;
  padding: 0 2rem;

  @media (max-width: 35rem) {
    padding: 0 .5rem;
  }
}

</style>