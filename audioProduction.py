import requests
import os

def load_env():
    with open('.env') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Call load_env function to load environment variables from .env file
load_env()

# Now you can access the API key using os.environ.get
API_KEY = os.environ.get("DG_API_KEY")
# Define the API endpoint
url = "https://api.deepgram.com/v1/speak?model=aura-hera-en"

# Set your Deepgram API key
api_key = "12a7bbacc2c80f20088f242eedc0fb551d76545c"

# Define the headers
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "text": "Hello, from getAIChatbots"
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("File saved successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")
