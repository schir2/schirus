<template>
  <nav class="top-nav">
    <ul class="links">
      <li class="link" ><router-link :to="{name:'home'}">Home</router-link></li>
      <li class="link" ><router-link :to="{name:'blog'}">Blog</router-link></li>
      <li class="link" ><router-link :to="{name:'about'}">About</router-link></li>
    </ul>
    <ul class="controls">
      <LoginSmall></LoginSmall>
    </ul>
  </nav>
</template>

<script>
import LoginSmall from "@/components/shared/LoginSmall";
export default {
  name: "TheNavbar",
  components: {LoginSmall}
}
</script>

<style scoped lang="scss">
.top-nav {
  display: grid;
  grid-template-areas: "branding links controls";
  margin-top: .25rem;
  border-bottom: .1rem solid $color-taupe-gray;
}

.branding {
  grid-area: branding;
}

.links {
  grid-area: links;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;


  .link {
    padding: .25rem .5rem;
    transition: all .1s ease-in;

    &:hover {
    box-shadow: 0 0 0 2px $color-blue;
    }
  }

  .active {
    border-bottom: .2rem solid $color-kobe;
  }
}

.controls {
  grid-area: controls;
}
</style>
