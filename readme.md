# SafeTrade WebSocket Client

This is an example Python project that helps clients connect to the SafeTrade Cryptocurrency Exchange WebSocket via Python.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/safetrade-exchange/example-client.git
cd example-client
```

2. Install the required packages:
```sh
pip install -r requirements.txt
```

## Configuration

1. Open main.py and replace <your_api_key> and <your_secret_key> with your actual SafeTrade API key and secret.
```python
yourAPIkey = "<your_api_key>"
yourAPISecret = "<your_secret_key>"
```

## Running the Client
To start the client, run the following command:
```sh
python main.py
```

This will connect to the SafeTrade WebSocket and subscribe to the specified channels.

## Project Structure
- api.py: Contains the Client class for interacting with the SafeTrade API.
- main.py: Entry point of the application.
- manager.py: Contains the SafeTrade class that manages WebSocket connections and subscriptions.
- ticker.py: Contains the Ticker class for handling ticker data.
- ws.py: Contains the Websocket class for managing WebSocket connections.
- wsstore.py: Contains the WebsocketStore class for managing multiple WebSocket connections.
