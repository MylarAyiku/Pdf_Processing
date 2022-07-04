import PyPDF2
#apply a watermark on a number on  pdf pages
#Requirement
#pdf_watermarked file
#the pdf file you want to apply

#open the pdf file you want to watermark
#r >read b>binary
template=PyPDF2.Pdf.FileReader(open('MyFile.pdf','rb'))
#the file that contains the watermark
watermark=PyPDF2.Pdf.FileReader(open('wtmFile.pdf','rb'))

output=PyPDF2.PdFileWriter()

#loop through page to apply the watermark
for i in range(template.getNumPages()):
    page=template.getPage(i)
    #merge the page with the watermarked page
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("watermarked_output.pdf",'wb') as file:
