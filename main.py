import glob
from PyPDF2 import PdfMerger, PdfReader

mergedObject = PdfMerger()

# list all pdf files in current directory
files = glob.glob("*.pdf")

if files:
    print(f"Detected the following files: {files}")
    files.sort()
    for file in files:
        mergedObject.append(PdfReader(file, 'rb'))

    print(f"Joining all files into one...")
    
    mergedObject.write("pdf-mama.pdf")

    print("Done!")

else:
    print("There are no pdfs in this folder")

input("")
