# pdfMerge.py

## Description
`pdfMerge.py` is a Python script that merges all PDF files within a specified folder. If no argument is provided, it will attempt to merge all PDF files from a directory named `PDF` under the current directory. The merged PDF file is saved in the current directory.

## Features
- **Directory-based Merging**: Merges all PDF files in a specified directory into one PDF document.
- **Command-line Interface**: Easy to use with command-line arguments.
- **Customizable Folder Selection**: Allows specifying a target folder for locating PDF files.
- **Sorted Merging**: Merges PDF files in alphabetical order.

## Technologies Used
This script uses the `PyPDF2` library to handle PDF files.

## How to Run
This script requires Python to run. You do not need to install it separately. To run the script, use the following command:

```
python pdfMerge.py <foldername>
```

Replace `<foldername>` with the name of the folder containing the PDF files you want to merge. If you do not provide a folder name, the script will attempt to merge all PDF files from a directory named `PDF` under the current directory.

## Note
Please ensure that you have the necessary permissions to read the PDF files in the specified folder and to write to the current directory. Also, make sure that the `PyPDF2` library is installed in your Python environment. If it's not, you can install it using pip:

```
pip install PyPDF2
```
