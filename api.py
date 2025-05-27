import requests
from datetime import datetime
import pytz
import hmac
import hashlib
import binascii
import time

class Client:
  def __init__(self, baseURL, key, secret):
    self.baseURL = baseURL
    self.key = key
    self.secret = secret
    self.headers = {}

  def get_authentication(self):
    nonce = str(int(time.time()) * 1000)  # Nonce in milliseconds
    signature = self.generate_signature(nonce, self.secret, self.key)
    return {
        "X-Auth-Apikey": self.key,
        "X-Auth-Nonce": nonce,
        "X-Auth-Signature": signature,
        "Content-Type": "application/json;charset=utf-8"
    }

  def get_api(self, url, query=None, headers=None):
    try:
        auth_headers = self.get_authentication()
        if headers:
            auth_headers.update(headers)
        response = requests.get(self.baseURL + url, headers=auth_headers, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None

  def post_api(self, url, data=None, headers=None):
    try:
        auth_headers = self.get_authentication()
        if headers:
            auth_headers.update(headers)
        response = requests.post(self.baseURL + url, headers=auth_headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None

  def generate_signature(self, nonce, secret, key):
    hash = hmac.new(secret.encode(), digestmod=hashlib.sha256)
    # Concatenate nonce and key, then calculate the HMAC hash
    hash.update((nonce + key).encode())
    signature = hash.digest()

    # Convert the binary signature to hexadecimal representation
    signature_hex = binascii.hexlify(signature).decode()

    return signature_hex

  def get_orders(self, state=None):
    return self.get_api("/trade/market/orders", query={"state": state} if state else None)

  def create_order(self, market, side, amount, price=None):
    data = {
        "market": market,
        "side": side,
        "amount": amount,
        "type": "limit" if price is not None else "market"
    }
    if price is not None:
        data["price"] = price
    return self.post_api("/trade/market/orders", data=data)
