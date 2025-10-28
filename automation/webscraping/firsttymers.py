import requests
from bs4 import BeautifulSoup
import time
import sqlite3  # or PostgreSQL

# Example function
def scrape_achievement_page(url):
    resp = requests.get(url, headers={'User-Agent': 'YourScraperBot/1.0'})
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, 'html.parser')
    # parse fields based on your page structure
    # e.g., name = soup.find(...)
    return {
        'name': ..., 
        'achievement': ..., 
        'date': ..., 
        'country': ...,
        'url': url
    }

# Loop over a list of URLs or via search pages
for url in ["https://www.sabcnews.com/sabcnews/"]:
    data = scrape_achievement_page(url)
    if data:
        # insert into database
        time.sleep(2)  # pause between requests
