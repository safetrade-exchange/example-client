import requests
from datetime import datetime
import pytz
import hmac
import hashlib
import binascii

class Client:
  def __init__(self, baseURL, key, secret):
    self.baseURL = baseURL
    timestamp = self.get_timestamp()
    nonce = str(timestamp)
    signature = self.generate_signature(nonce, secret, key)
    self.headers = {
      "X-Auth-Apikey": key,
      "X-Auth-Nonce":     nonce,
      "X-Auth-Signature": signature,
      "Content-Type":     "application/json;charset=utf-8",
    }

  def get_api(self, url, headers=None):
    try:
      response = requests.get(self.baseURL + url, headers=headers)
      # Check if the request was successful (status code 200)
      if response.status_code == 200:
        # Return the JSON data
        return response.json()
      else:
        # If the request was unsuccessful, print the error code
        print(f"Error: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
      # Handle connection errors
      print(f"Connection error: {e}")
      return None
  
  def get_timestamp(self):
    data = self.get_api("/trade/public/timestamp")
    if data:
      data = data[:23] + data[-1]
      t = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
      now = datetime.now().replace(tzinfo=pytz.UTC)
      clientTimestamp = int(now.timestamp())
      serverTimestamp = int(t.timestamp())

      now = int(now.timestamp() + 1)
      return (now - clientTimestamp + serverTimestamp) * 1000
    else:
      print("Failed to fetch data from the API.")
  def generate_signature(self, nonce, secret, key):
    hash = hmac.new(secret.encode(), digestmod=hashlib.sha256)
    # Concatenate nonce and key, then calculate the HMAC hash
    hash.update((nonce + key).encode())
    signature = hash.digest()
    
    # Convert the binary signature to hexadecimal representation
    signature_hex = binascii.hexlify(signature).decode()
    
    return signature_hex