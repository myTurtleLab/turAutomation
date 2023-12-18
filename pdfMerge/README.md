
# pdfMerge.py

## Description
`pdfMerge.py` is a Python script for merging PDF files within a specified folder into a single document. It supports additional features like adding footnotes. If no folder name is provided, it defaults to a directory named `PDF`.

## Features
- **Directory-based Merging**: Merges all PDF files in a specified directory into a single document.
- **Footnote Addition**: Can add a footnote to each page of the merged PDF, containing the original file's name and page number.
- **Command-line Interface**: Easy to use with command-line arguments for various functionalities.
- **Customizable Folder Selection**: Allows specifying a target folder for locating PDF files.
- **Sorted Merging**: Merges PDF files in alphabetical order.
- **Help Option**: Includes a `--help` option to display usage instructions.

## Technologies Used
This script uses the `PyPDF2` and `reportlab` libraries for handling and modifying PDF files.

## How to Run
This script requires Python to run. To run the script, use the following command:

```
python pdfMerge.py [foldername] [options]
```

### Options
- `--footnote`: Adds a footnote on each page with the file name and page number.
- `--help`: Displays a help message with usage instructions.

### Examples
- `python pdfMerge.py PDF --footnote`: Merges PDFs in the 'PDF' folder and adds footnotes.
- `python pdfMerge.py MyPDFs`: Merges PDFs in the 'MyPDFs' folder without footnotes.
- `python pdfMerge.py --help`: Displays help information.

Replace `[foldername]` with the name of the folder containing the PDF files you want to merge. If you do not specify a folder, it defaults to a folder named `PDF`.

## Note
Please ensure that you have the necessary permissions to read the PDF files in the specified folder and to write to the current directory. Also, make sure that the `PyPDF2` library is installed in your Python environment. If it's not, you can install it using pip:

```
pip install PyPDF2
```

## License
This project is licensed under MIT License. See the LICENSE file for more details.
