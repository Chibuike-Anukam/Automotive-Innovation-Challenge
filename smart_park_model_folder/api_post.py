import requests


# Define the API endpoint
url = "http://localhost:5000/predict"

# Load an image file
with open("mammals.jpg", "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Print the predictions
print(response.json())