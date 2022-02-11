<template>
  <nav class="top-nav">
    <ul class="branding">
      <img class="logo" src="@/assets/logo.gif">
    </ul>
    <ul class="links">
      <li class="link">
        <NavLink :to="{name:'home'}">Home</NavLink>
      </li>
      <li class="link">
        <NavLink :to="{name:'blog'}">Blog</NavLink>
      </li>
      <li class="link">
        <NavLink :to="{name:'apps'}">Apps</NavLink>
      </li>
      <li class="link">
        <NavLink :to="{name:'about'}">About</NavLink>
      </li>
    </ul>
    <ul class="controls">
      <AuthSmall></AuthSmall>
    </ul>
  </nav>
</template>

<script>
import AuthSmall from "@/components/shared/AuthSmall";
import NavLink from "@/components/shared/NavLink";

export default {
  name: "TheNavbar",
  components: {NavLink, AuthSmall}
}
</script>

<style scoped lang="scss">
.top-nav {
  display: grid;
  grid-template-areas: "branding links controls";
  grid-template-columns: minmax(12ch, 1fr) 1fr minmax(12ch, 1fr);
  margin-top: .25rem;
  border-bottom: .1rem solid $color-taupe-gray;
  align-items: center;
}

.branding {
  grid-area: branding;
  display: flex;
  justify-content: flex-end;

  .logo {
    height: 2rem;
    width: 2rem;
  }
}

.links {
  grid-area: links;
  display: flex;
  justify-content: center;
  gap: 1rem;
  
}

.controls {
  grid-area: controls;
}
</style>
