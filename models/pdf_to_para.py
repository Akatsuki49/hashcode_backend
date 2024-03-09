import textract
import os
import re


def extract_text(filepath):
    # read the content of pdf as text
    text = textract.process(filepath)
    # use four space as paragraph delimiter to convert the text into list of paragraphs.
    print(re.split('\s{4,}', text.decode('utf-8')))
    print("----------------------------------------------------\n")


fname = r'C:\Users\sowme\StudioProjects\hashcode_backend\assets'
output_file = os.path.join(fname, "Beauty_and_Beast.pdf")

extract_text(output_file)
