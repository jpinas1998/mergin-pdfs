import glob
import fitz

# List all PDF files in the current directory
files = glob.glob("*.pdf")

if files:
    print(f"Detected the following files: {files}")
    files.sort()

    pdf_document = fitz.open()

    for file in files:
        pdf_document.insert_pdf(fitz.open(file))

    # Compress the resulting PDF
    pdf_document.save("all-in-one-compressed.pdf", deflate=True)

    print("Joining and compressing all files into one...")

    pdf_document.close()

    print("Done!")

else:
    print("There are no PDFs in this folder")

input("")
