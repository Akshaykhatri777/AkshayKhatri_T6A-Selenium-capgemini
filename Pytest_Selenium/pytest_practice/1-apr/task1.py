import requests

response = requests.get("https://petstore.swagger.io/v2/store/inventory")
# response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?=status=sold")
# response = requests.get("https://petstore.swagger.io/v2/pet/17")


actual = response.status_code
expected = 200

assert actual == expected, "Not Equal"