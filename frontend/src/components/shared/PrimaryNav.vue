<template>
  <nav class="top-nav">
    <img class="logo" src="@/assets/logo.gif">
    <Transition>
      <menu class="menu" v-show="!mobile || menuVisible">
        <ul class="links" id="links">
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
        <AuthSmall></AuthSmall>
      </menu>
    </Transition>
    <Transition name="toggle"
                mode="out-in"
                enter-active-class="animate__animated animate__bounceIn"
    >
      <a v-if="!menuVisible" @click="menuVisible = !menuVisible" key="1" class="toggle"><span
          class="material-icons">menu</span></a>
      <a v-else @click="menuVisible = !menuVisible" key="2" class="toggle"><span
          class="material-icons">close</span></a>
    </Transition>
  </nav>
</template>

<script>
import AuthSmall from "@/components/shared/AuthSmall";
import NavLink from "@/components/shared/NavLink";

export default {
  name: "PrimaryNav",
  data() {
    return {
      menuVisible: false,
      mobile: true
    }
  },
  components: {NavLink, AuthSmall},
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  },
  destroyed() {
    window.removeEventListener('resize', this.onResize)
  },
  methods: {
    onResize() {
      this.mobile = window.matchMedia('(max-width: 35rem)').matches
    }
  }
}
</script>

<style lang="scss">

.top-nav {
  background-color: $color-light-gray;
  padding: 1rem;
  gap: 1rem;
  align-items: center;
  justify-content: center;
  display: flex;
  margin-bottom: 2rem;
}

.logo {
  height: 2rem;
  width: 2rem;
}

.menu {
  display: flex;
  align-items: center;
  background-color: $color-light-gray;
}

.toggle {
  position: absolute;
  top: 1rem;
  right: 1rem;
  display: none;
  height: 2rem;
  width: 2rem;
}


.links {
  grid-area: links;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  font-weight: bold;
  font-size: 1.25rem;
  text-transform: uppercase;

}

@media (max-width: 35rem) {
  .top-nav {
    z-index: 100;
    position: sticky;
    align-items: center;
    justify-content: space-between;
  }

  .toggle {
    z-index: 200;
    display: block;
  }

  .menu {
    position: fixed;
    display: flex;
    padding-top: 4rem;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    top: 0;
    right: 0;
    z-index: 100;
    height: 100vh;
    min-width: 50%;
    margin: 0;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
  }

  .links {
    flex-direction: column;
    justify-content: space-around;

  }
  .auth-small {
    display: flex;
    gap: 1rem;
    flex-direction: column;
  }

  .v-enter-active, .v-leave-active {
    transition: all .5s ease;
  }
  .v-enter-from, .v-leave-to {
    transform: translateX(100%);
    opacity: 0;
  }

}
</style>
