from requests import get

url = "http://localhost:8123/api/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhNmZlMDIwNmE3YmQ0MmRhOWFmYTJiM2RjNmM3ZmNmYyIsImlhdCI6MTcwMjQ3MzcwNiwiZXhwIjoyMDE3ODMzNzA2fQ.CcwUj20jwHL6nq8n8Nsfbrdww9q6tJ95yGHLlB1CRNg",
    "content-type": "application/json",
}

response = get(url, headers=headers)
print(response.text)