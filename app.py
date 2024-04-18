from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from PIL import Image
import os
import requests
import google.generativeai as genai
import io

app = Flask(__name__)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision Model and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    input_prompt = request.form.get('input_prompt')
    image_url = request.form.get('image_url')
    uploaded_file = request.files.get('image')

    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            response = get_gemini_response(input_prompt, image)
            return jsonify(response=response)
        else:
            return jsonify(response="Could not retrieve image from the URL.")
    elif uploaded_file:
        image = Image.open(io.BytesIO(uploaded_file.read()))
        response = get_gemini_response(input_prompt, image)
        return jsonify(response=response)
    else:
        return jsonify(response="No image uploaded.")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
