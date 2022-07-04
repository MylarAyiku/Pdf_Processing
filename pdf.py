import PyPDF2
import sys
#this will take the inputs of all the argument you give excluding the first one
inputs =sys.argv[1:]

#function to loop through the  list
def pdf_combiner(pdf_list):
    merger= PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        #test if it works
        #by printing names out
        print (pdf)
        merger.append(pdf)
    #save the merged files
    merge.write("mergedPdf.pdf")

pdf_combiner(inputs)     
