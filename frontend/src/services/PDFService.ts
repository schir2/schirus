import {PDFDocument} from "pdf-lib";

export const pdfService = {
    async merge(documents: any[]){
        const newDocument = await PDFDocument.create()
        for (const pdfPath of documents) {
            const document = await PDFDocument.load(await pdfPath.file.arrayBuffer())
            const copiedPages = await newDocument.copyPages(document, document.getPageIndices())
            copiedPages.forEach(page => newDocument.addPage(page))
        }
        return await newDocument.save();
    },

    async generateThumbnail(file: File){
        const newDocument = await PDFDocument.create()
        console.log(file)
        const document = await PDFDocument.load(await file.arrayBuffer())
        const copiedPages = await newDocument.copyPages(document, [0])
        copiedPages.forEach(page => newDocument.addPage(page))
        return await newDocument.save()
}
}
