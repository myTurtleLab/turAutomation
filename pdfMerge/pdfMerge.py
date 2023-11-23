import os
import sys
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

def mergePDF(pdf_directory):
    # Change the current working directory to 'PDF'
    os.chdir(pdf_directory)

    pdfFiles = []  # variable for storing pdf filenames

    # Scan for PDF files in the current directory
    for filename in os.listdir('.'):  # List files in the current directory
        if filename.lower().endswith('.pdf'):  # Check for .pdf files
            pdfFiles.append(filename)  # Add them to the list

    # Sorting the files by forcing everything to lower case.
    pdfFiles.sort(key=str.lower)

    # Creating a PdfWriter object
    pdfWriter = PyPDF2.PdfWriter()

    # Loop through all the PDF files
    for pdfFile in pdfFiles:
        pdfReader = PyPDF2.PdfReader(pdfFile)  # Open each PDF file
        for pageNum in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[pageNum]
            pdfWriter.add_page(pageObj)  # Add each page to the writer object
        print(f"File: {pdfFile} | Page #: {pageNum}")
    # Save the resulting merged PDF to a file
    os.chdir(current_directory)
    mergedfile = pdf_directory + "-merged.pdf"
    with open(mergedfile, 'wb') as outFile:
        pdfWriter.write(outFile)

    if len(pdfFiles) > 0:
        print(f"Merged PDF created with {len(pdfFiles)} files.")
    else:
        print(f"No PDF found in {pdf_directory} directory.")

# Main Function #
# Check if an input parameter is provided for the folder name
if __name__ == '__main__':
    if len(sys.argv) > 1:
        foldername = sys.argv[1]  # Use the input parameter as the folder name
    else:
        foldername = "PDF"  # Default folder name

# Check if there is a directory named 'PDF' in the current directory
    current_directory = os.getcwd()
    pdf_directory = os.path.join(current_directory, foldername)

    if not os.path.exists(pdf_directory):
        sys.exit("No PDF folder is found.")
    else:
        mergePDF(pdf_directory)

