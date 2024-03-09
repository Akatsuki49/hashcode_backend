

import os
from langchain.document_loaders import PyPDFium2Loader

def ex_text(imgpath):
    loader = PyPDFium2Loader(imgpath)
    data = loader.load()
    print(data)

def find_parent_folder(filename, search_directory='.'):
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            return os.path.abspath(root)

    return None  # File not found in the specified directory and its subdirectories

fname = "Beauty_and_Beast.pdf"
pfolder = find_parent_folder(fname)
ofolder = os.path.join(pfolder, fname)
ex_text(ofolder)
