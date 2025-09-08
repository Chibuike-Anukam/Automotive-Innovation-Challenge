import requests

# Define the API endpoint
url = "http://localhost:5000/predict"

# Send a GET request to fetch predictions (for example)
response = requests.get(url)

# Print the response
print(response.json())
