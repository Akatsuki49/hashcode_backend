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


def extract_text_from_pdf_with_pdfreader(pdf_path):
    reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(reader.pages)

    paragraphs = []
    for page_num in range(num_pages):
        page_text = reader.pages[page_num].extract_text()
        paragraphs.extend(page_text.split("\n"))

    return paragraphs


def find_parent_folder(filename, search_directory='.'):
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            return os.path.abspath(root)

    return None  # File not found in the specified directory and its subdirectories


fname = r'C:\Users\sowme\StudioProjects\hashcode_backend\assets'
output_file = os.path.join(fname, "Beauty_and_Beast.pdf")

paragraphs = extract_text_from_pdf_with_pdfreader(output_file)

# print(paragraphs)

i = 0
for para in paragraphs:
    print(i)
    print(para, "\n")
    i += 1
