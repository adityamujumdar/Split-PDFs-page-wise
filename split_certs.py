from PyPDF2 import PdfFileWriter, PdfFileReader
import os.path
import pandas as pd

df = pd.read_excel("excel sheet with names") # can also index sheet by name or fetch all sheets
df.tail(15)
pages_to_delete = [91, 92, 94, 103] # page numbering starts from 0
infile = PdfFileReader(open("pdf to separate", "rb"))
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)
destination = "processed pdf to separate without blank pages"
with open(destination, 'wb') as f:
    output.write(f)
    
names = df['Full Name'].tolist()

inputpdf = PdfFileReader(open("processed pdf to separate without blank pages", "rb"))
destination_directory = "destination folder"
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    names_pdf = names[i] + ".pdf"
    outputFilename = os.path.join(destination_directory, names_pdf)
    with open (outputFilename, "wb") as outputStream:
        output.write(outputStream)
