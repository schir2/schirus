<template>
  <main class="main">
    <TheNavbar></TheNavbar>
    <TheHeader></TheHeader>
    <div class="content">
      <router-view/>
    </div>
  </main>
</template>
<script>

export default {
  name: "App",
}
</script>
<style>
.main {
  display: grid;
  height: 100vh;
  grid-template-areas:
      "top-nav top-nav top-nav"
      ". header ."
      ". content ."
      "footer footer footer";
  grid-template-columns: minmax(0,1fr) minmax(700px, 1024px) minmax(0,1fr);
  grid-template-rows: 3rem 5rem 1fr 2rem;
}

.top-nav {
  grid-area: top-nav;
}

.header {
  grid-area: header
}

.content {
  grid-area: content
}

.footer {
  grid-area: footer
}

</style>