from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os
# Initialize Flask app
app = Flask(__name__)

# Call load_env function to load environment variables from .env file
load_dotenv()
# Define your Deepgram API key (replace 'YOUR_DEEPGRAM_API_KEY' with your actual API key)
DEEPGRAM_API_KEY = os.getenv("DG_API_KEY")

# Define a route to handle POST requests
@app.route('/api/speak', methods=['POST'])
def speak():
    # Get the JSON data from the request body
    request_data = request.get_json()

    # Validate the presence of the 'text' field in the request data
    if 'text' not in request_data:
        return jsonify({'error': 'Text field is required'}), 400

    # Define headers for the request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {DEEPGRAM_API_KEY}'
    }

    # Define the data for the request
    data = {
        'text': request_data['text']
    }

    # Make the POST request to Deepgram API
    response = requests.post('https://api.deepgram.com/v1/speak?model=aura-stella-en', headers=headers, json=data, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the response audio to a file
        with open('output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        return jsonify({'message': 'Audio generated successfully', 'filename': 'output.mp3'}), 200
    else:
        # If the request failed, return the error message
        return jsonify({'error': response.text}), response.status_code

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
