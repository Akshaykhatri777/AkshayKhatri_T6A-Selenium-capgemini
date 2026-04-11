from api.cart.cart_api import CartAPI
from utils.read_data import read_json
from core.auth import get_auth_data

cart_api = CartAPI()

def test_addtocart(auth_data,headers):
    data = read_json("test_data/add_to_cart.json")

    details = get_auth_data()
    shopperId = details["shopper_id"]

    response = cart_api.addtocart(shopperId,data,headers=headers)

    assert response.status_code == 201
    print(response.json())