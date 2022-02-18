<template>
  <div>
    <PrimaryNav></PrimaryNav>
    <div class="content">
      <TheHeader></TheHeader>
      <router-view/>
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

</style>