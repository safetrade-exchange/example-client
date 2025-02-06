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

  def thread_task(name):
    """A sample thread task that runs in a loop until stopped."""
    while not stop_event.is_set():
      print(f"Thread {name} running...")
      time.sleep(1)
    print(f"Thread {name} exiting...")

  async def async_task():
    """An async task that runs in a loop until stopped."""
    while not stop_event.is_set():
      print("Async task running...")
      await asyncio.sleep(1)
    print("Async task exiting...")

  async def run(self):
    p1 = threading.Thread(target=self.public.onMessage)
    p1.start()
    p2 = threading.Thread(target=self.private.onMessage)
    p2.start()
