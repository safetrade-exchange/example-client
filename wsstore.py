import ws
import threading

class WebsocketStore:
  def __init__(self, baseURL, header = None, callback = None):
    self.public = ws.Websocket(baseURL, "public", None, callback)
    self.private = ws.Websocket(baseURL, "private", header, callback)

  def subscribe(self, type, channel):
    if type == "public":
      self.public.subscribe(channel)
    elif type == "private":
      self.private.subscribe(channel)

  def unsubscribe(self, type, channel):
    if type == "public":
      self.public.unsubscribe(channel)
    elif type == "private":
      self.private.unsubscribe(channel)

  async def run(self):
    p1 = threading.Thread(target=self.public.onMessage)
    p1.start()
    p2 = threading.Thread(target=self.private.onMessage)
    p2.start()
