const fs = require('fs')
import {PDFDocument} from "pdf-lib";

export const pdfService = {
    async merge(documents: string[]){
        const mergedPDF = await PDFDocument.create()
        for (const pdfPath of documents) {
            console.log(pdfPath)
            const document = await PDFDocument.load(pdfPath)
            const copiedPages = await mergedPDF.copyPages(document, document.getPageIndices())
            copiedPages.forEach(page => mergedPDF.addPage(page))
        }
        return await mergedPDF.save();
    }
}
