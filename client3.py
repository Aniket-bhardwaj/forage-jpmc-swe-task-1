import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate average of bid and ask prices
    return {'stock': stock, 'bid_price': bid_price, 'ask_price': ask_price, 'price': price}


def getRatio(price_a, price_b):
    """Get ratio of price_a and price_b"""
    if price_b == 0:
        return None  # Handle division by zero
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    prices = {}  # Initialize dictionary to store stock prices
    for _ in range(N):
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

            # Iterate through each quote and store data points
            for quote in quotes:
                data_point = getDataPoint(quote)
                prices[data_point['stock']] = data_point['price']

            # Calculate and print the ratio if both stocks are available
            if 'stockA' in prices and 'stockB' in prices:
                ratio = getRatio(prices['stockA'], prices['stockB'])
                print("The ratio between stockA and stockB is:", ratio)

        except Exception as e:
            print('Error:', e)
            break
