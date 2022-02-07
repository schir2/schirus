<template>
  <main id="app">
    <TheNavbar></TheNavbar>
    <TheHeader></TheHeader>
    <router-view/>
  </main>
</template>
<script>
import TheNavbar from "@/components/shared/TheNavbar";
import TheHeader from "@/components/shared/TheHeader";
export default {
  name:"App",
  components: {TheHeader, TheNavbar},
}
</script>
