import requests

class IEEE_Xplore:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://ieeexploreapi.ieee.org/api/v1/search/articles"
        
    def fetch_articles(self, query, max_results=10, start_index=1):
        """Fetch articles from IEEE Xplore based on a query."""
        params = {
            'apikey': self.api_key,
            'querytext': query,
            'max_records': max_results,
            'start_record': start_index
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['articles']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from IEEE Xplore: {e}")
            return []

    def get_article_details(self, article_id):
        """Fetch detailed information about a specific article by its ID."""
        url = f"https://ieeexploreapi.ieee.org/api/v1/article/{article_id}"
        params = {
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching article details: {e}")
            return {}
