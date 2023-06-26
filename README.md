# ColorsInPDFPages

The script provided is a Python program that analyses a PDF file to find pages that contain colours other than black in both text and images. See below for detailed information on how the script works.

## Dependencies
The script requires the following Python library:

**fitz**: This library provides an interface for working with PDF files using the Poppler library.

Make sure you have installed all the necessary dependencies before running the script.

Install using: _**pip install PyMuPDF**_

## Functions
### has_color(page)
This function checks whether a specific page contains colors other than black in both text and images. It returns _True_ if colors other than black are found, otherwise it returns _False_.

**Arguments**

_page_: An object representing the PDF page to be analyzed.

### find_colored_pages(pdf_path)
This function finds and returns the pages in the PDF file that contain colors other than black in both text and images.

**Arguments**

_pdf_path_: The path of the PDF file to be analyzed.

**Returns**

The function returns a list of page numbers corresponding to the pages in the PDF file that contain colors other than black.

## Exceptions
_FileNotFoundError_: Raised if the specified PDF file path does not exist.

## Usage

When the script is run, the user is prompted for the path to the PDF file to be analysed. The script will then print the pages in the PDF file that contain colours other than black, along with the total number of coloured pages.

**Note**: The script uses the _fitz_ interface to work with PDF files using the _Poppler_ library. Make sure you have _Poppler_ installed and configured correctly on your system.

## Additional Resources:

_Poppler Documentation_: https://poppler.freedesktop.org/documentation.html

_fitz Documentation_: https://pymupdf.readthedocs.io/
