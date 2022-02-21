<template>
  <div
    @dragover.prevent
    @drop.prevent
  >
    <form>
      <draggable-component
        v-model="files"
        class="files"
        item-key="id"
        @start="drag=true"
        @end="drag=false"
      >
        <template #item="{element, index}">
          <div class="file">
            <button
              class="material-icons file-action"
              @click.prevent="removeFile(index)"
            >
              delete
            </button>
            <span class="file-heading">{{ element.file.name.substring(0, element.file.name.length-4) }}</span>
            <iframe
              class="file-thumbnail"
              :src="element.thumbnail"
            />
          </div>
        </template>
      </draggable-component>
      <input
        ref="fileInput"
        type="file"
        multiple
        style="display:none"
        @change="onUploadHandler"
      >
      <div
        class="drop-zone"
        @drop="onDropHandler"
        @click="$refs.fileInput.click()"
      >
        <span class="material-icons icon">file_upload</span>
        <span class="display-1">Drop Your Files Here</span>
      </div>
      <button @click.prevent="onClickMerge">
        Merge
      </button>
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
      const objectUrl = await pdfService.generateMergedObjectUrl(
          this.files.map(file => file.file))
      window.open(objectUrl, '', 'height=650,width=840');

    },
    async addFiles(files) {
      const success = []
      const errors = []
      for (const file of files) {

        if (file.name.endsWith('.pdf')) {
          this.files.push({file: file, thumbnail: await pdfService.generateThumbnailObjectUrl(file)})
          success.push(file.name)
        } else {
          errors.push(file.name)
        }
      }
      if (success.length !== 0) {
        this.$toast.success(`Added ${success.length} files.`)
      }
      if (errors.length !== 0) {
        this.$toast.error(`Failed to add ${errors.length} files.`)
      }
    },
    removeFile(index) {
      this.$toast.warning(`Removed ${this.files[index].file.name}`)
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 10rem;
  padding: 20px;
  border-width: 2px;
  border-radius: 2px;
  border-style: dashed;
  background-color: #fafafa;
  color: #bdbdbd;
  outline: none;
  transition: border .24s ease-in-out;

  .icon {
    font-size: 5rem;
  }
}

.files {
  display: flex;
}

.file {
  height: 35rem;
  width: 16rem;
}

.file-thumbnail {
  height: 30rem;
  width: 15rem;
}

</style>