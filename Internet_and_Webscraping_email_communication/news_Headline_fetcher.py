import requests


API_KEY = 'your_api_key_here'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_top_headlines(country='in', category='general'):
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': 10  
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  
        data = response.json()

        if data['status'] == 'ok':
            articles = data['articles']
            print(f"\nTop {len(articles)} Headlines in {category.capitalize()} ({country.upper()}):\n")
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']}")
        else:
            print("Error fetching news:", data.get('message'))

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

if __name__ == "__main__":
    country = input("Enter country code (default 'in'): ") or 'in'
    category = input("Enter news category (default 'general'): ") or 'general'
    fetch_top_headlines(country, category)
