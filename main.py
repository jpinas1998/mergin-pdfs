import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

mergedObject = PdfFileMerger()

# list all pdf files in current directory
files = glob.glob("*.pdf")

if files:
    print(f"Detected the following files: {files}")

    for file in files:
        mergedObject.append(PdfFileReader(file, 'rb'))

    print(f"Joining all files into one...")
    
    mergedObject.write("merged-pdf.pdf")

    print("Done!")

else:
    print("There are no pdfs in this folder")

input("")
