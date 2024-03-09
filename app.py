from flask import Flask, request, jsonify
from models.image_generator import generate_image
from models.audio_generator import generate_audio
from models.language_model import extract_context

import re
import textract

app = Flask(__name__)


@app.route('/visualize', methods=['POST'])
def visualize_paragraph():
    paragraph_text = request.json['paragraph']
    context = extract_context(paragraph_text)

    image_data = generate_image(context)
    audio_data = generate_audio(context)

    return jsonify({'image': image_data, 'audio': audio_data})


if __name__ == '__main__':
    app.run()
