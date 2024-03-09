import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/shubh/priv_key.json')
firebase_admin.initialize_app(cred)

# Get Firestore instance
db = firestore.client()

def extract_paragraphs_from_text_file(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    paragraphs = []
    current_paragraph = ''
    for line in lines:
        line = line.strip()
        if line:  
            current_paragraph += line + '\n'  # Add it to the current paragraph
        else:  # If an empty line is encountered, consider it as the end of the paragraph
            if current_paragraph:  # Ensure there is content in the paragraph
                # Add the paragraph to the list
                paragraphs.append(current_paragraph.strip())
                current_paragraph = ''  # Reset the current paragraph for the next iteration

    # Add the last paragraph if it's not empty
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())

    return paragraphs

def upload_to_firestore(title, paragraphs):
    doc_ref = db.collection('books').document()
    data = {
        'title': title,
        'content': paragraphs
    }
    doc_ref.set(data)
    print(f"Document '{title}' uploaded to Firestore with ID: {doc_ref.id}")

# Example usage:
text_file_path = os.path.join('/Users/shubh/development/hashcode_backend/assets', "Cinderella.txt")

title = "Cinderella"
paragraphs = extract_paragraphs_from_text_file(text_file_path)
upload_to_firestore(title, paragraphs)
