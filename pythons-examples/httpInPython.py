import httplib2

print(httplib2.__version__)
print(httplib2.__copyright__)
print(httplib2.__doc__)

# GET call
http = httplib2.Http()
content = http.request(
    "http://localhost:8080/v7/identifier-types?page=0&size=2&businessPartnerType=LEGAL_ENTITY",
    method="GET"
    )

print(content)

import json
import requests

response = requests.get("http://localhost:8080/v7/identifier-types?page=0&size=2&businessPartnerType=LEGAL_ENTITY")
contentOfResponse = json.loads(response.text)
print("Hehehe from request lib", contentOfResponse)