import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader

list1 = ["File1.pdf", "File2.pdf"]

merge = PdfFileMerger()

for file in list1:
    merge.append(PyPDF2.PdfFileReader(file, 'rb'))
merge.write("mergedFile.pdf")
merge.close()
createdFile = PdfFileReader("mergedFile.pdf")

print(createdFile)