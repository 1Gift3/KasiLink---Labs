import requests
from bs4 import BeautifulSoup
import time
import sqlite3  # or PostgreSQL
import os
from urllib.parse import urljoin


# database setup
DB_PATH = os.path.abspath("first_timers.db")
print(f"Using database: {DB_PATH}")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS achievements ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, achievement TEXT, 
               date TEXT, country TEXT, url TEXT ) """)
conn.commit()

# scraping function
def scrape_achievement_page(url):
    url = url.strip()
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to GET {url}: {e}")
        return None

    soup = BeautifulSoup(resp.content, "html.parser")

    # try primary selector (news sites often use <article>), but fall back
    articles = soup.find_all("article")
    if not articles:
        # fallback: for Wikipedia and many sites, use the main content area
        main = soup.select_one("#mw-content-text, main, #content")
        if main:
            # find reasonable blocks (list items, paragraphs, headings)
            articles = main.select("li, p, div")[:200]   # limit to first 200 blocks
        else:
            # last fallback: all anchors
            articles = soup.select("a[href]")[:200]

    data_list = []
    keywords = ["first ever", "makes history", "first to", "first woman", "first man", "historic win"]
    for block in articles:
        # prefer anchor text if block is an <a>
        if block.name == "a":
            text = block.get_text(" ", strip=True)
            href = block.get("href")
        else:
            text = block.get_text(" ", strip=True)
            a = block.find("a", href=True)
            href = a.get("href") if a else ""

        if not text:
            continue

        # show what we're seeing so you can tune keywords
        print("SNIPPET:", text[:180])
        abs_link = urljoin(url, href) if href else ""

        text_lower = text.lower()
        if any(kw in text_lower for kw in keywords):
            print("  -> MATCH", text[:160])
            data_list.append({
                "name": None,
                "achievement": text,
                "date": None,
                "country": None,
                "url": abs_link or url
            })

    return data_list

# Main loop
# fixed URL: use the singular "List_of_firsts" page (remove typo/extra 's')
urls = ["https://en.wikipedia.org/wiki/"]

for url in urls:
    results = scrape_achievement_page(url)
    if not results:
        continue

    # track how many inserts this run
    inserted_this_url = 0
    for data in results:
        try:
            cursor.execute(""" INSERT INTO achievements (name, achievement, date, country, url) 
                               VALUES (?, ?, ?, ?, ?) """,
                           (data["name"], data["achievement"], data["date"], data["country"], data["url"]))
            inserted_id = cursor.lastrowid
            inserted_this_url += 1
            print(f"Inserted id={inserted_id} for achievement snippet={data['achievement'][:120]!r}")
        except Exception as e:
            print(f"Failed to insert row: {e}")
    conn.commit()
    if inserted_this_url:
        print(f"Inserted {inserted_this_url} rows from {url}")

conn.close()
print("Scraping completed. Data saved to first_timers.db")

