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
  member = safetrade.client.get_member_me()
  if member:
    print(f"UID: {member.get('uid')}")
    print(f"Email: {member.get('email')}")
    print(f"Level: {member.get('level')}")
  else:
    print("Failed to fetch member info.")

  canceled_orders = safetrade.client.get_orders(state="cancel")
  if canceled_orders:
    print(f"\nCanceled Orders ({len(canceled_orders)}):")
    for o in canceled_orders:
      print(f"  [{o['id']}] {o['market']} {o['side']} {o['origin_amount']} @ {o['price']} (filled: {o['filled_amount']})")
  else:
    print("No orders found or an error occurred.")

  created_order = safetrade.client.create_order(
    side="sell",
    market="xtmusdt",
    amount="12.5",
    price="0.45"
  )
  if created_order:
    print(f"\nCreated Order: [{created_order['id']}] {created_order['market']} {created_order['side']} {created_order['origin_amount']} @ {created_order['price']} ({created_order['state']})")
  else:
    print("Failed to create order or an error occurred.")
