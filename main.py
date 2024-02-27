import manager
import asyncio

yourAPIkey = "<your_api_key>"
yourAPISecret = "<your_secret_key>"
baseURL       = "https://safe.trade/api/v2"

safetrade = manager.SafeTrade(baseURL, yourAPIkey, yourAPISecret)

safetrade.subscribe("public", ["global.tickers"])
safetrade.subscribe("private", ["order"])


if __name__ == "__main__":
  asyncio.run(safetrade.run())

