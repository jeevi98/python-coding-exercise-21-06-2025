import requests

def get_crypto_price(crypto_id, currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto_id,
        "vs_currencies": currency
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        data = response.json()
        if crypto_id in data:
            price = data[crypto_id][currency]
            print(f" {crypto_id.capitalize()} Price: {price} {currency.upper()}")
        else:
            print(" Invalid crypto ID or not found.")
    except requests.exceptions.RequestException as e:
        print(f" Error fetching price: {e}")

if __name__ == "__main__":
    while True:
        crypto_id = input("Enter cryptocurrency ID (e.g., bitcoin, ethereum) or 'exit' to quit: ").strip().lower()
        if crypto_id == 'exit':
            break
        if crypto_id:
            get_crypto_price(crypto_id)
        else:
            print(" Please enter a valid cryptocurrency ID.")
