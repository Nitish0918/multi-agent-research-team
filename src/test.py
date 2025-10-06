import requests

# Replace this with your actual API key
API_KEY = "AIzaSyCQPjsptrMsox-VS9VMcJe0Dw3QUCrvPrQ"

# Gemini 2.0 endpoint for listing models
url = "https://generativelanguage.googleapis.com/v1beta2/models"

# Set headers with your API key
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error if request fails
    data = response.json()
    print("API Key is valid! Available models:")
    for model in data.get("models", []):
        print("-", model.get("name"))
except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)
    print("Response:", response.text)
except Exception as err:
    print("Other error occurred:", err)
