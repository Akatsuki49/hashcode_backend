import re
import base64
from diffusers import StableDiffusionPipeline
import torch
import numpy as np
import soundfile as sf
from models.testing import imggen
from pydub import AudioSegment
from flask import Flask, request, jsonify, send_file
import json
from openai import OpenAI
from models.audioext import audgen

# Load API key from config file

API_KEY = "Add secret key"


app = Flask(__name__)


@app.route('/image_endpoint', methods=['POST'])
def visualize_paragraph():
    paragraph_text = request.form['paragraph']
    title = request.form['title']
    image_context = generate_SummarizedPrompt_image(paragraph_text, title)
    print(image_context)

    image_data = imggen(image_context)


    return jsonify({'image': image_data})


@app.route('/audio_endpoint', methods=['POST'])
def generate_audio_endpoint():
    paragraph_text = request.form['paragraph']
    audio_context = generate_SummarizedPrompt_audio(paragraph_text)

    audgen(audio_context)

    return send_file('musicgen_out.wav', as_attachment=True)
    # return send_file(audio_data, mimetype='audio/wav')


def generate_SummarizedPrompt_image(paragraph_text, title):
    extra_text = "This is a paragraph from the story book "+ title +" , deduce the context of the given paragraph while keeping in mind thigs like title, genre, keywords and also what happened previously in this book before this point of time. Give me an optimized prompt to query a model to generate an image for the paragraph given the surrounding context and keep it very creative. Keep it limited to 70 words and Give me only the prompt. "
    final_text = paragraph_text+extra_text
    # query open AI gpt4:
    return query_llm(final_text,title)
    pass


def generate_SummarizedPrompt_audio(paragraph_text):
    extra_text = "Deduce the context of the given paragraph and give me an optimized prompt to query a model to generate audio for the paragraph given the surrounding context. Keep it limited to 30 words. Give me only the prompt"

    final_text = paragraph_text+extra_text
    # query gpt4
    return query_llm(final_text,"")


def query_llm(text, extra):
    final=""
    if(len(extra)>0):
        final=text+" Book Title : "+extra
    else:
        final=text
    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": final,
            }
        ],
        max_tokens = 75,
        model="gpt-3.5-turbo",
        temperature = 0.4,
    )

    if response and response.choices:
        summarized_content = response.choices[0].message.content
        # print(summarized_content)
        return summarized_content
    else:
        # print("Error: No response from the model")
        return "Error: No response from the model"


paragraph_text = "The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn't think they could bear it if anyone found out about the Potters. Mrs. Potter was Mrs. Dursley's sister, but they hadn't met for several years; in fact, Mrs. Dursley pretended she didn't have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn't want Dudley mixing with a child like that. When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday our story starts, there was nothing about the cloudy sky outside to suggest that strange and mysterious things would soon be happening all over the country. Mr. Dursley hummed as he picked out his most boring tie for work, and Mrs. Dursley gossiped away happily as she wrestled a screaming Dudley into his high chair."

title = "Harry Potter and the Sorcerer's Stone"
# generate_SummarizedPrompt_image(
#     paragraph_text, title)
generate_SummarizedPrompt_audio(paragraph_text)

if __name__ == '__main__':
    app.run()
