import requests
import json

# Define the URL
url = "http://localhost:5000/iris"

# Define the headers
headers = {'Content-Type': 'application/json'}

# Define the data
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.json())

