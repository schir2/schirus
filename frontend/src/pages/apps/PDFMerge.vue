<template>
  <div>
    <form>
      <draggable-component
          class="file-drop-zone"
          v-model="files"
          @start="drag=true"
          @end="drag=false"
          item-key="id">
        <template #item="{element}">
          <div>{{ element.name }}</div>
        </template>
      </draggable-component>
      <input type="file" @change="handleFileUpload">
      <button @click.prevent="onClickMerge">Merge</button>
    </form>
  </div>
</template>

<script>

import {pdfService} from "@/services/PDFService";
import draggableComponent from "vuedraggable"

export default {
  name: "PDFMerge",
  components: {draggableComponent},
  data() {
    return {
      files: [],
      drag: false
    }
  },
  methods: {
    async onClickMerge() {
      const arrayBuffer = await pdfService.merge(this.files)
      const blob = new Blob([arrayBuffer], {type: 'application/pdf'})
      const objectUrl = URL.createObjectURL(blob)
      window.open(objectUrl, '', 'height=650,width=840');

    },
    async handleFileUpload(event) {
      const file = await event.target.files[0]
      this.files.push(file)
    },
  }
}
</script>

<style scoped lang="scss">
.file-drop-zone {
  height: 40vh;
  background-color: $color-deep-champagne;
}

.file-drop-zone-item {
  background-color: $color-yellow;
}

</style>