import api
import wsstore
import ticker
import asyncio

class SafeTrade:
  def __init__(self, baseURL, key, secret):
    self.client = api.Client(baseURL, key, secret)
    self.ws = wsstore.WebsocketStore(baseURL, self.client.get_authentication(), self.callback)

    self.tickers = {}

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
