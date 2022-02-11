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
      const success = []
      const errors = []
      files.forEach(file => {

        if (file.name.endsWith('.pdf')) {
          this.files.push(file)
          success.push(file.name)
        } else {
          errors.push(file.name)
        }
      })
      if (success.length !== 0) {
        this.$toast.success(`Added ${success.length} files.`)
      }
      if (errors.length !== 0) {
        this.$toast.error(`Failed to add ${errors.length} files.`)
      }
    },
    removeFile(index) {
      this.$toast.warning(`Removed ${this.files[index].name}`)
      this.files.splice(index, 1)
    }
    ,
    async onUploadHandler(event) {
      this.addFiles(event.target.files)
    }
    ,
    async onDropHandler(event) {
      this.addFiles(event.dataTransfer.files)
    }
    ,
  }
}
</script>

<style scoped lang="scss">
.drop-zone {
  height: 20vh;
}

.file-drop-zone-item {
  background-color: $color-yellow;
}

</style>