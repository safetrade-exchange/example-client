import api
import wsstore
import ticker

class SafeTrade:
  def __init__(self, baseURL, key, secret, channel = None):
    self.client = api.Client(baseURL, key, secret)
    self.ws = wsstore.WebsocketStore(baseURL, channel, self.client.headers, self.callback)
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

  async def run(self):
    await self.ws.run()