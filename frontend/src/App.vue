<template>
  <div>
    <PrimaryNav></PrimaryNav>
    <div class="content">
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
.content{
  max-width: 70rem;
  margin:0 auto;
  padding: .5rem;
}

</style>