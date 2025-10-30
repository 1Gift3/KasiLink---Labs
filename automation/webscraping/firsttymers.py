import requests
from bs4 import BeautifulSoup
import time
import sqlite3  # or PostgreSQL

# database setup
conn = sqlite3.connect("first_timers.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS achievements ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, achievement TEXT, 
               date TEXT, country TEXT, url TEXT ) """)
conn.commit()

# scraping function
def scrape_achievement_page(url):
    resp =requests.get(url, headers={'User-Agent': 'Mozilla/5.'})
    if resp.status_code != 200:
        print(f"Failed to retrieve page: {url}")
        return None
    
    soup = BeautifulSoup(resp.content, 'html.parser')

    # Extracting headlines
    articles = soup.find_all("article")
    data_list = []

    for article in articles:
        text = article.get_text(strip=True)
        link = article.get("href")

        if not link or not text:
            continue

        # keywords for first-timers
        keywords = ["first ever", "makes history", "first to", "first woman", "first man", "historic win"]

        if any(kw in text.lower() for kw in keywords):

            data_list.append({
                "name": None,
                "achievement": text,
                "date": None,
                "country": None,
                "url": link if link.startswith("http") else f"https://www.sabcnews.com"
            })

    return data_list

# Main loop 
urls = ["https://www.sabcnews.com/sabcnews/"]


for url in urls:
    results = scrape_achievement_page(url)
    if not results:
        continue

    for data in results:
        cursor.execute(""" INSERT INTO achievements (name, achievement, date, country, url) 
                           VALUES (?, ?, ?, ?, ?) """,
                       (data["name"], data["achievement"], data["date"], data["country"], data["url"]))
        print(f"Saved: {data['achievement']}")
    conn.commit()

conn.close()
print("Scraping completed. Data saved to first_timers.db")

