import manager
import asyncio

yourAPIkey = "<your_api_key>"
yourAPISecret = "<your_secret_key>"
baseURL       = "https://safe.trade/api/v2"

safetrade = manager.SafeTrade(baseURL, yourAPIkey, yourAPISecret)

async def websocket_run():
  safetrade.subscribe("public", ["global.tickers", "qubicusdt.depth", "qubicusdt.trades"])
  safetrade.subscribe("private", ["order", "trade", "balance"])
  safetrade.run()

if __name__ == "__main__":
  canceled_orders = safetrade.client.get_orders(state="cancel")
  if canceled_orders:
    print("Canceled Orders:", canceled_orders)
  else:
    print("No orders found or an error occurred.")

  created_order = safetrade.client.create_order(
    side="sell",
    market="xtmusdt",
    amount="12.5",
    price="0.45"
  )
  if created_order:
    print("Created Order:", created_order)
  else:
    print("Failed to create order or an error occurred.")
