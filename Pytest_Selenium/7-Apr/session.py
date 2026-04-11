import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com/shopping"
session = requests.Session()

# payload = {
#   "city": "string",
#   "country": "string",
#   "email": "usershopper002@gmail.com",
#   "firstName": "string",
#   "gender": "MALE",
#   "lastName": "Bh",
#   "password": "ABCD@1234",
#   "phone": 9876000011,
#   "state": "RJ",
#   "zoneId": "ALPHA"
# }
#
# response = requests.post("https://www.shoppersstack.com/shopping/shoppers", json=payload, verify=False)



payload2 = {
  "email": "usershopper002@gmail.com",
  "password": "ABCD@1234",
  "role": "SHOPPER"
}

response2 = session.post("https://www.shoppersstack.com/shopping/users/login", json=payload2,verify=False)
data = response2.json()
id = data['data']['userId']
token = data['data']['jwtToken']
print(id,token,sep='\n')

assert response2.status_code == 200, 'Invalid status code'

header = {'Authorization': 'Bearer ' + token}

response3 = session.get(f"https://www.shoppersstack.com/shopping/shoppers/{id}",headers=header,verify=False)
print(response3.json())