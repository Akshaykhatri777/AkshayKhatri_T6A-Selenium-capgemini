from core.base_api import BaseAPI
from utils.config import BASE_URL

class CartAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def addtocart(self, shopperId, payload, headers):
        return self.api.post(f'/shoppers/{shopperId}/carts', json=payload, headers=headers)