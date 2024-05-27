import os
from PyPDF2 import PdfFileReader
from docx import Document
from docx.shared import Inches

def pdf_to_docx(pdf_file, docx_file):
    # Create a new Word document
    document = Document()

    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PdfFileReader(file)

        # Iterate through the pages of the PDF
        for page_num in range(pdf_reader.numPages):
            # Get the current page
            page = pdf_reader.getPage(page_num)

            # Extract the text from the page
            text = page.extractText()

            # Add the text to the Word document
            document.add_paragraph(text)

            # Add a page break after each page
            document.add_page_break()

    # Save the Word document
    document.save(docx_file)

# Example usage
pdf_file = 'input.pdf'
docx_file = 'output.docx'

pdf_to_docx(pdf_file, docx_file)
print(f'PDF file "{pdf_file}" converted to "{docx_file}".')
