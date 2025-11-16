import requests
import time

def fetch_api(url, delay=1):
    """
    Fetch data from an API endpoint with optional delay to respect rate limits.
    """
    time.sleep(delay)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
