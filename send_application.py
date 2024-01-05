import requests
import pprint

# Set your access token
bearer_token = ''

# Set the external key
externalKey = ''

# Set the request parameters
url = 'https://enrollment-api-sandbox.paymentshub.com'
path = '/enroll/application/merchant/send/key/' + externalKey

# Set proper headers
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer ' + bearer_token}

# Do the HTTP request
response = requests.put(url + path, headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Get the JSON response
data = response.json()
pprint.pprint(data, indent=2)
