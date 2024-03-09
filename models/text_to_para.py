import os


def extract_paragraphs_from_text_file(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    paragraphs = []
    current_paragraph = ''
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespaces
        if line:  # If the line is not empty
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


# Example usage:
fname = r'C:\Users\sowme\StudioProjects\hashcode_backend\assets'
text_file_path = os.path.join(fname, "PussInBoots.txt")

paragraphs = extract_paragraphs_from_text_file(text_file_path)

# Print the extracted paragraphs
for i, para in enumerate(paragraphs):
    print(f"Paragraph {i+1}:")
    print(para)
    print()
