import sys
import cbpro
import time
import json

class MyWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD", "ETH-USD"]
        self.message_count = 0
        print("Let's count the messages!")

    def on_message(self, msg):
        print(json.dumps(msg, indent=4, sort_keys=True))
        self.message_count += 1

    def on_close(self):
        print("-- Goodbye! --")

# Channel options: ['ticker', 'user', 'matches', 'level2', 'full']

wsClient = MyWebsocketClient(auth=True, channels=None)
wsClient.start()
print(wsClient.url, wsClient.products)
try:
    while True:
        print("\nMessageCount =", "%i \n" % wsClient.message_count)
        time.sleep(1)
except KeyboardInterrupt:
    wsClient.close()

if wsClient.error:
    sys.exit(1)
else:
    sys.exit(0)
