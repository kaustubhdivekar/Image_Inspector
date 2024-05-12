# Import necessary modules
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from PIL import Image
import os
import requests
import google.generativeai as genai
import io

# Create a Flask application instance
app = Flask(__name__)

# Configure the Google Generative AI with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro Vision Model
model = genai.GenerativeModel("gemini-pro-vision")

# Function to get response from the Gemini Pro Vision Model
def get_gemini_response(input, image):
    # If there is an input prompt, generate content based on the input and image
    if input != "":
        response = model.generate_content([input, image])
    # If there is no input prompt, generate content based on the image only
    else:
        response = model.generate_content([image])
    return response.text

# Route for the home page
@app.route('/')
def index():
    # Render the home page
    return render_template('index.html')

# Route for processing the image
@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the input prompt and image URL from the form data
    input_prompt = request.form.get('input_prompt')
    image_url = request.form.get('image_url')
    # Get the uploaded file from the form data
    uploaded_file = request.files.get('image')

    # If there is an image URL, process the image from the URL
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            response = get_gemini_response(input_prompt, image)
            return jsonify(response=response)
        else:
            return jsonify(response="Could not retrieve image from the URL.")
    # If there is an uploaded file, process the uploaded image
    elif uploaded_file:
        image = Image.open(io.BytesIO(uploaded_file.read()))
        response = get_gemini_response(input_prompt, image)
        return jsonify(response=response)
    # If there is no image URL or uploaded file, return an error message
    else:
        return jsonify(response="No image uploaded.")

# Main entry point of the application
if __name__ == '__main__':
    # Load environment variables
    load_dotenv()
    # Run the Flask application in debug mode
    app.run(debug=True)
