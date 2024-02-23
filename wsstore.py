import ws
import threading

class WebsocketStore:
  def __init__(self, baseURL, channels, header = None, callback = None):
    self.channels = channels
    self.public = ws.Websocket(baseURL, "public", None, callback)
    self.private = ws.Websocket(baseURL, "private", header, callback)
  
  async def run(self):
    self.public.subscribe(self.channels["public"])
    self.private.subscribe(self.channels["private"])

    p1 = threading.Thread(target=self.public.onMessage)
    p1.start()
    
    p2 = threading.Thread(target=self.private.onMessage)
    p2.start()
