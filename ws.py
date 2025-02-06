import websocket
import json

class Websocket:
  def __init__(self, baseURL, type, header, callback = None):
    self.wsUrl = baseURL.replace("https://", "wss://").replace('http://', 'ws://') + "/websocket/"
    self.callback = callback
    self.ws = websocket.create_connection(url=self.wsUrl+type, header=header)

  def subscribe(self, channel):
    data = {
      "event": "subscribe",
      "streams": channel,
    }
    json_string = json.dumps(data)

    self.ws.send(json_string)
    print("Send websocket:" + json_string)

  def unsubscribe(self, channel):
    data = {
      "event": "unsubscribe",
      "streams": channel,
    }
    json_string = json.dumps(data)

    self.ws.send(json_string)
    print("Send unsubscribe:" + json_string)


  def onMessage(self):
    while True:
      res = self.ws.recv()

      if self.callback != None:
        self.callback(json.loads(res))
