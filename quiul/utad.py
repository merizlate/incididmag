from example.oauth2 import service_account
import example.auth
from example.auth.transport.requests import Request

# Path to the JSON key file for the service account
key_path = '/path/to/service-account-key.json'

# Create credentials object from the key file
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=['https://www.example.com Create an authorized session
session = example.auth.transport.requests.AuthorizedSession(credentials)

# Make a request to a example Cloud service
response = session.get('https://www.example.com Process the response
print(response.json())
