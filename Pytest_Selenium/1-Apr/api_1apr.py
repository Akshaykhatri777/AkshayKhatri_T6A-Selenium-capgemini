import requests

para = {
    'name':'Special_char_owner_!@#$^&()`.testing'
}
# response = requests.get("https://petstore.swagger.io/v2/store/inventory")
# response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?=status=sold")
# response = requests.get("https://petstore.swagger.io/v2/pet/17")
# response = requests.get("https://petstore.swagger.io/v2/pet/params=para")


payload = {
  "id": 63,
  "category": {
    "id": 0,
    "name": "animal"
  },
  "name": "dogesh",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
post = requests.post("https://petstore.swagger.io/v2/pet",json=payload)
#response = requests.get("https://petstore.swagger.io/v2/pet/63")
delete = requests.delete("https://petstore.swagger.io/v2/pet/63")


#print(response.text)
# print(response.status_code)
print("/n")
#print(post.json())

print(delete.json())

# actual = post.status_code
# expected = 200

# assert actual == expected, "Not Equal"