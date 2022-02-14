import {PDFDocument} from "pdf-lib";

export const pdfService = {
    async merge(documents: File[]) {
        const newDocument = await PDFDocument.create()

        for (const file of documents) {
            const document = await PDFDocument.load(await file.arrayBuffer())
            const copiedPages = await newDocument.copyPages(document, document.getPageIndices())

            copiedPages.forEach(page => newDocument.addPage(page))
        }
        return await newDocument.save();
    },

    async copy(file: File, single: boolean = false) {
        const newDocument = await PDFDocument.create()
        const document = await PDFDocument.load(await file.arrayBuffer())
        const indexesToCopy = single ? [0] : document.getPageIndices()
        const copiedPages = await newDocument.copyPages(document, indexesToCopy)
        copiedPages.forEach(page => newDocument.addPage(page))
        return await newDocument.save()
    },

    async generateObjectUrl(arrayBuffer: ArrayBuffer){
        const blob = new Blob([arrayBuffer], {type: 'application/pdf'})
        return URL.createObjectURL(blob)

    },

    async generateThumbnailObjectUrl(file: File) {
        const arrayBuffer = await this.copy(file)
        return this.generateObjectUrl(arrayBuffer)
    },

    async generateMergedObjectUrl(files: File[]) {
        const arrayBuffer = await this.merge(files)
        return this.generateObjectUrl(arrayBuffer)
    }
}