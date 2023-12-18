### verion 2 by HY LEUNG at Dec 2023
import os
import sys
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def display_help():
    help_message = """
    PDF Merger Script

    Usage:
      python PDFmerge.py [foldername] [options]

    Options:
      --footnote  Adds a footnote to each page of the merged PDF. The footnote includes the filename and the page number.
      --help      Displays this help message.

    Arguments:
      foldername  Optional. The name of the folder containing PDFs to merge. Defaults to 'PDF' if not specified.

    Examples:
      python PDFmerge.py PDF --footnote   Merges PDFs in the 'PDF' folder and adds footnotes.
      python PDFmerge.py MyPDFs           Merges PDFs in the 'MyPDFs' folder without footnotes.
      python PDFmerge.py --help           Displays help information.
    """
    print(help_message)

def create_footnote_page(original_page, footnote_text, pdf_writer):
    # Create a PDF with ReportLab and draw the footnote
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 10, footnote_text)  # Position at bottom left
    can.save()

    # Move the ReportLab string to a PDF object
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Merge the PDFs
    page = original_page
    page.merge_page(new_pdf.pages[0])
    pdf_writer.add_page(page)

def mergePDF(pdf_directory, add_footnote=False):
    # Change the current working directory to the specified directory
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
            page = pdfReader.pages[pageNum]
            if add_footnote:
                footnote_text = f"{pdfFile}, Page {pageNum + 1}"
                create_footnote_page(page, footnote_text, pdfWriter)
            else:
                pdfWriter.add_page(page)  # Add each page to the writer object
            print(f"File: {pdfFile} | Page #: {pageNum + 1}")

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
if __name__ == '__main__':
    # Process command line arguments
    args = sys.argv[1:]
    if "--help" in args:
        display_help()
        sys.exit()

    add_footnote = "--footnote" in args

    # Remove parameters starting with "--"
    args = [arg for arg in args if not arg.startswith("--")]

    # Set the folder name, default to "PDF" if no other parameters are provided
    foldername = args[0] if args else "PDF"

    current_directory = os.getcwd()
    pdf_directory = os.path.join(current_directory, foldername)

    if not os.path.exists(pdf_directory):
        sys.exit(f"No folder named {foldername} is found.")
    else:
        mergePDF(pdf_directory, add_footnote)
