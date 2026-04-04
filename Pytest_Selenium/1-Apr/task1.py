import requests

payload = {
"id": 60,
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
def post():
    response = requests.post("https://petstore.swagger.io/v2/pet",json=payload)
    return response.json()['id']

id = post()
print(id)

def get(id1):
    response1 = requests.get(f"https://petstore.swagger.io/v2/pet/{id1}")
    print(response1.json())

def delete(id1):
    response2 = requests.delete(f"https://petstore.swagger.io/v2/pet/{id1}")
    print(response2.json())

get(id)
delete(id)