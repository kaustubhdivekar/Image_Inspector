# Image Inspector using Gemini API

Image Inspector is a Flask application that uses the Google Generative AI to generate content based on an image and an optional input prompt.

## Installation

Before running the application, you need to install the necessary Python packages. You can do this by running the following command in your terminal:


pip install -r requirements.txt


This will install all the packages listed in the `requirements.txt` file.

## Usage

To run the application, use the following command:


python app.py


This will start the Flask development server, and the application will be accessible at `http://localhost:5000`.

## Endpoints

The application has the following endpoints:

- `/`: The home page, which renders the `index.html` template.
- `/process_image`: A POST endpoint that processes an image and returns a response generated by the Gemini Pro Vision Model. The image can be provided either as a URL in the `image_url` form field, or as an uploaded file in the `image` form field. An optional input prompt can be provided in the `input_prompt` form field.

## Environment Variables

The application uses the following environment variables:

- `GOOGLE_API_KEY`: The API key for the Google Generative AI.

You can set these environment variables in a `.env` file in the root directory of the project. The `python-dotenv` package is used to load these variables when the application starts.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

