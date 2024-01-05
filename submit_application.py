import requests
import pprint

# Set the external key
externalKey = ''

# Set the request parameters
url = 'https://enrollment-api-sandbox.paymentshub.com'
path = '/enroll/application/submit/' + externalKey

# Set proper headers
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lciI6Imlzdl9hcGkiLCJtZWFwaUNsaWVudElkIjo5MywibWVhcGlDbGllbnRLZXkiOiJWQTdML3ZqTUcxWSs4TlNPNTRiZ05VMkRpbnVFQTRrc0xGL1VoaGQzYlhxQWpxVVZiRWh0akRsaEFuWlFYeFVzSGV2N05Yb3RmS0U1ai9jMXIvSGZXUnBVTHpLZVYrak1VZWJMc0lJRlM3ND0iLCJhbGxvd0VucmljaGVyQWNjZXNzIjp0cnVlLCJhbGxvd01lcmNoYW50U2lnbmF0dXJlIjp0cnVlLCJpYXQiOjE2OTE2OTE4NTksImV4cCI6MTY5MTY5MjE1OSwic3ViIjoiNzRjODZiOGRjYTFhMGJlNmUyZmQ4YTZiZWYwMWUzN2IifQ.pe7wrdautnt9nSirqLgA5DZea2FiVj5HuTl5YXjJJvc'}

# Do the HTTP request
response = requests.put(url + path, headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
