<template>
  <div>
    <form>
      <ul class="files">
        <li v-for="(file, index) in files" :key="index">{{ file }}</li>
      </ul>
      <input type="file" @change="handleFileUpload">
      <button @click.prevent="onClickMerge">Merge</button>
    </form>
  </div>
</template>

<script>

import {pdfService} from "@/services/PDFService";

export default {
  name: "PDFMerge",
  data() {
    return {
      files: []
    }
  },
  methods: {
    async onClickMerge() {
      const arrayBuffer = await pdfService.merge(this.files)
      const blob = new Blob([arrayBuffer], {type: 'application/pdf'})
      const objectUrl = URL.createObjectURL(blob)
      const link = document.createElement('a');
      link.style.display = 'none';
      document.body.appendChild(link);
      link.href = objectUrl;
      link.href = URL.createObjectURL(blob);
      link.download = 'data.pdf';
      link.click();
      return objectUrl

    },
    async handleFileUpload(event) {
      const file = await event.target.files[0].arrayBuffer()
      console.log(file)
      this.files.push(file)
    },
  }
}
</script>

<style scoped>

</style>