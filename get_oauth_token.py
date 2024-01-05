import requests
import pprint

# Set the request parameters
url = 'https://enrollment-api-auth.paymentshub.com'
path = "/oauth/token"

# Set proper headers
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Set the URL-encoded body
grant_type = 'client_credentials'
scope = 'all'
client_id = ''
client_secret = ''

data = {'grant_type': grant_type, 'scope': scope, 'client_id': client_id, 'client_secret': client_secret}

# Do the HTTP request
response = requests.post(url + path, headers=headers, data=data)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Get the JSON response
data = response.json()
pprint.pprint(data, indent=2)
