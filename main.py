import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

mergedObject = PdfFileMerger()
files = glob.glob("*.pdf")

if files:
    print(f"detectados los siguientes ficheros: {files}")

    for file in files:
        mergedObject.append(PdfFileReader(file, 'rb'))

    mergedObject.write("merged-pdf.pdf")

    print("Listo!")

else:
    print("No hay pdfs en esta carpeta")

input("")
