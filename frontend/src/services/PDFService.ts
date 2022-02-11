import {PDFDocument} from "pdf-lib";

export const pdfService = {
    async merge(documents: File[]){
        const mergedPDF = await PDFDocument.create()
        for (const pdfPath of documents) {
            const document = await PDFDocument.load(await pdfPath.arrayBuffer())
            const copiedPages = await mergedPDF.copyPages(document, document.getPageIndices())
            copiedPages.forEach(page => mergedPDF.addPage(page))
        }
        return await mergedPDF.save();
    }
}
