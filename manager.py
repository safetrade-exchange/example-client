import api
import wsstore
import ticker
import asyncio

class SafeTrade:
  def __init__(self, baseURL, key, secret):
    self.baseURL = baseURL
    self.client = api.Client(baseURL, key, secret)
    self._ws = None
    self.tickers = {}

  @property
  def ws(self):
    if self._ws is None:
      self._ws = wsstore.WebsocketStore(self.baseURL, self.client.get_authentication(), self.callback)
    return self._ws

  def callback(self, data):
    print(data)
    for keyData in data:
      if keyData == "global.tickers":
        for market in data[keyData]:
          marketData = data[keyData][market]

          self.tickers[market] = ticker.Ticker(
            marketData["amount"],
            marketData["avg_price"],
            marketData["high"],
            marketData["last"],
            marketData["low"],
            marketData["open"],
            marketData["price_change_percent"],
            marketData["volume"]
          )

  def subscribe(self, type, channel):
    self.ws.subscribe(type, channel)

  def unsubscribe(self, type, channel):
    self.ws.unsubscribe(type, channel)

  async def run(self):
    await self.ws.run()
