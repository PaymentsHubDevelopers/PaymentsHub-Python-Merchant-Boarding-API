import requests
import pprint
import json

# Set the External Key
external_key = ''

# Set the URLs
base_url = 'https://enrollment-api-sandbox.paymentshub.com'
token_base_url = 'https://enrollment-api-auth.paymentshub.com'
token_url = f'{token_base_url}/oauth/token'
create_application_url = f'{base_url}/enroll/application'
send_application_url = f'{base_url}/enroll/application/merchant/send/key/{external_key}'
validate_application_url = f'{base_url}/enroll/application/validate/{external_key}'
submit_application_url = f'{base_url}/enroll/application/submit/{external_key}'

# Set proper Oauth Headers
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Set the urlencoded body
grant_type = 'client_credentials'
scope = 'all'
client_id = ''
client_secret = ''

data = {'scope': scope, 'grant_type': grant_type,
        'client_id': client_id, 'client_secret': client_secret}

# Do the HTTP request
response = requests.post(token_url, headers=headers, data=data)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint('Could not get Token!')
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Get the JSON response
data = response.json()

# Save token
bearer_token = data['access_token']

# Create the Application
# Set proper Send Application Headers
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + bearer_token}

# Set the mandatory urlencoded body
application_payload = {
    "agent": 12345,
    "applicationName": "Test Application 1",
    "externalKey": "12345",
    "plan": {
        "planId": 123
    },
    "principals": [
        {
            "firstName": "Jane",
            "lastName": "Jackson",
            "socialSecurityNumber": "12345",
            "dateOfBirth": "1955-12-25",
            "phoneNumber": "1234567890",
            "email": "user@example",
            "street": "123 Selah Way",
            "street2": "Suite 123",
            "zipCode": "12345",
            "city": "South Burlington",
            "state": "VT",
            "equityOwnershipPercentage": 50,
            "title": "ceo",
            "isPersonalGuarantor": True,
            "driverLicenseNumber": "ABC1234567890",
            "driverLicenseIssuedState": "MI"
        },
        {
            "firstName": "Jeremy",
            "lastName": "Coelman",
            "socialSecurityNumber": "1234567890",
            "dateOfBirth": "1977-12-25",
            "phoneNumber": "1234567890",
            "email": "user@example",
            "street": "1234 Test Drive",
            "zipCode": "12345",
            "city": "Red Bank",
            "state": "NJ",
            "equityOwnershipPercentage": 50,
            "title": "manager",
            "isPersonalGuarantor": False,
            "driverLicenseNumber": None,
            "driverLicenseIssuedState": None
        }
    ],
    "business": {
        "corporateName": "Joe's Spaceage Stereo",
        "dbaName": "Jo Jackson Spaceage Stereo",
        "businessType": "C",
        "federalTaxIdNumber": "123567890",
        "federalTaxIdType": "EIN",
        "mcc": "1234",
        "phone": "1234567890",
        "email": "user@example",
        "websites": [
            {
                "url": "https://example.com",
                "websiteCustomerServiceEmail": "customer-service-email@example.com",
                "websiteCustomerServicePhoneNumber": "1234567890"
            }
        ],
        "averageTicketAmount": 5000,
        "averageMonthlyVolume": 1250000,
        "highTicketAmount": 125000,
        "merchandiseServicesSold": "Audio components and services",
        "percentOfBusinessTransactions": {
            "cardSwiped": 65,
            "keyedCardPresentNotImprinted": 20,
            "mailOrPhoneOrder": 0,
            "internet": 15
        },
        "businessContact": {
            "firstName": "Roy",
            "lastName": "Martin",
            "socialSecurityNumber": "123456789",
            "dateOfBirth": "1947-11-05",
            "street": "123 Late Avenue",
            "street2": "",
            "zipCode": "12345",
            "city": "South Burington",
            "state": "VT",
            "phoneNumber": "1234567890",
            "email": "user@example"
        },
        "statementDeliveryMethod": "electronic",
        "businessAddress": {
            "dba": {
                "street": "1234 Clinton St",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            },
            "corporate": {
                "street": "1234 Sun Valley Rd",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            },
            "shipTo": {
                "street": "1234 Saint James Drive",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            }
        }
    },
    "bankAccount": {
        "abaRouting": "123456789",
        "accountType": "checking",
        "demandDepositAccount": "123456789"
    }
}

# Convert the payload to JSON String
json_payload = json.dumps(application_payload)

# Do the HTTP request
response = requests.post(create_application_url, headers=headers, data=json_payload)

# Check for HTTP codes other than 200
if response.status_code != 201:
    pprint.pprint('Could not get create Application!')
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Send the application
# Set proper Send Application Headers
send_submit_headers = {'Content-Type': 'application/x-www-form-urlencoded',
                       'Authorization': 'Bearer ' + bearer_token}

# Do the HTTP request
response = requests.put(send_application_url, headers=send_submit_headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint('Could not send the application!')
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Validate Application
# Set proper Validation Headers
validate_headers = {'Authorization': 'Bearer ' + bearer_token}

response = requests.get(validate_application_url, headers=validate_headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint('Could not validate the application!')
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Submit Application
# Set the request parameters

# Set proper Submit Headers
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer ' + bearer_token}

# Do the HTTP request
response = requests.put(submit_application_url, headers=send_submit_headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint('Could not get Submit the application!')
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
pprint.pprint(data, indent=2)
