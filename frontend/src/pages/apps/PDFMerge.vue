<template>
  <div @dragover.prevent @drop.prevent>
    <form>
      <draggable-component
          class="files"
          v-model="files"
          @start="drag=true"
          @end="drag=false"
          item-key="id">
        <template #item="{element, index}">
          <div class="file"><span>{{ element.name }}</span>
            <button @click.prevent="removeFile(index)">Remove</button>
          </div>
        </template>
      </draggable-component>
      <input type="file" multiple @change="onUploadHandler">
      <div @drop="onDropHandler" class="drop-zone">
        <span class="display-1">Drop You File Here</span>
      </div>
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
    addFiles(files) {
      files.forEach(file => {
        this.files.push(file)
      })
    },
    removeFile(index) {
      this.files.splice(index, 1)
    },
    async onUploadHandler(event) {
      this.addFiles(event.target.files)
    },
    async onDropHandler(event) {
      this.addFiles(event.dataTransfer.files)
    },
  }
}
</script>

<style scoped lang="scss">
.drop-zone {
  height: 20vh;
  box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
}

.file-drop-zone-item {
  background-color: $color-yellow;
}

</style>