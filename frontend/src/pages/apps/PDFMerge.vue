<template>
  <div>
    <form>
      <ul class="file-drop-zone">
        <li class="file-drop-zone-item" draggable="true" v-for="(file, index) in files" :key="index">{{ file.name }}</li>
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
      const file = await event.target.files[0]
      this.files.push(file)
    },
  }
}
</script>

<style scoped lang="scss">
.file-drop-zone{
  height:40vh;
  background-color: $color-deep-champagne;
}
.file-drop-zone-item{
  background-color: $color-yellow;
}

</style>