<template>
  <div>
    <TheNavbar></TheNavbar>
    <div class="content">
      <TheHeader></TheHeader>
      <router-view/>
    </div>
  </div>
</template>
<script>

import TheNavbar from "@/components/shared/TheNavbar";

export default {
  name: "App",
  components: {TheNavbar},
}
</script>
<style lang="scss">

</style>