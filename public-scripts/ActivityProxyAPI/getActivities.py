import sys
sys.path.append("../Util")
import testUtil
import http.client
import json
import requests

CLIENT_ID = "9E5aqUf1aW5toUHDZlQWETcoJLZOWYMT"
CLIENT_SECRET = input("Enter the CLIENT_SECRET? ")
AUDIENCE = "http://healthsuite.allocatesoftware.com/api/v1/activityproxyapi"


API_ADDRESS="https://interop-activityproxy-gateway.allocate-dev.co.uk/api/v1/activities"

# Get access token for the vacancy API
tokenQuery = testUtil.getTokenQuery(
    clientId=CLIENT_ID, clientSecret=CLIENT_SECRET, audience=AUDIENCE)
token = testUtil.getToken(tokenQuery)

bearer_auth = token["access_token"]
bearer = "bearer {}".format(bearer_auth)
print("Token: %s" % bearer)

# Generate randon proposal id
customerCode = "EPSON"
employeeId = "james.jones@test.pl"
assignNumber = "8601872"

# Call the API
srvEndpoint = "{}?customerCode={}&employeeId={}&assignmentNumber={}".format(API_ADDRESS, customerCode, employeeId, assignNumber)
print("URI: %s" % srvEndpoint)


r = requests.get(url=srvEndpoint, headers={
                 "accept": "application/json", "authorization": bearer}, verify=True)
rsp = r.text

print("Response Code: %s" % r.status_code)
print("Response: %s" % rsp)
