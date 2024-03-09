import PyPDF2
import easyocr
import os
import re


# def extract_text(filepath):
#     pdf_reader = PyPDF2.PdfReader(filepath)
#     paragraphs = []

#     # Use len(reader.pages) for number of pages
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         text = page.extract_text()

#         # Split the text into paragraphs.
#         paragraphs.extend(text.split("\n\n"))

#     return paragraphs


def extract_text_from_pdf_with_easyocr(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(reader.pages)

    text = ''
    for page_num in range(num_pages):
        page_text = reader.pages[page_num].extract_text()
        text += page_text

    return text

def extract_text_with_ocr(text):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(text)
    extracted_text = ' '.join([entry[1] for entry in result])
    return extracted_text

def find_parent_folder(filename, search_directory='.'):
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            return os.path.abspath(root)

    return None  # File not found in the specified directory and its subdirectories

fname = "Beauty_and_Beast.pdf"
pfolder = find_parent_folder(fname)
ofolder = os.path.join(pfolder,fname)
pdf_text = extract_text_from_pdf_with_easyocr(ofolder)
extracted_text = extract_text_with_ocr(pdf_text)
print(extracted_text)
# print(x1)
