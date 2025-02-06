import manager
import asyncio

yourAPIkey = "<your_api_key>"
yourAPISecret = "<your_secret_key>"
baseURL       = "https://safe.trade/api/v2"

safetrade = manager.SafeTrade(baseURL, yourAPIkey, yourAPISecret)

safetrade.subscribe("public", ["global.tickers", "qubicusdt.depth", "qubicusdt.trades"])
safetrade.subscribe("private", ["order", "trade", "balance"])

if __name__ == "__main__":
  asyncio.run(safetrade.run())  # Ensure the coroutine is awaited
