import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from itertools import combinations
import re
from datetime import datetime
import pytz
import yfinance as yf


def fetch_ft_articles(keywords, num_links):
    base_search_url = "https://www.ft.com/search?sort=relevance&q="
    search_query = "+".join(keyword.replace(" ", "+") for keyword in keywords)
    search_url = base_search_url + search_query

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for article in soup.find_all("div", class_="o-teaser__heading")[:num_links]:
        link = article.find("a")
        if link:
            title = link.get_text(strip=True)
            url = "https://www.ft.com" + link["href"]
            articles.append({"title": title, "url": url})

    return articles


def fetch_bloomberg_article_urls(keywords, num_links):
    base_search_url = "https://www.bloomberg.com/search?query="
    search_query = "%20".join(keyword.replace(" ", "%20") for keyword in keywords)
    search_url = base_search_url + search_query

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    ]

    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--window-size=1920x1080")
    firefox_options.add_argument(f"user-agent={random.choice(user_agents)}")

    urls = []

    driver = None
    try:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

        driver.get(search_url)
        time.sleep(random.uniform(5, 10))

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="storyItem"]'))
        )

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        for article in soup.find_all(
            "div", class_=lambda x: x and x.startswith("storyItem")
        )[:num_links]:
            link = article.find("a", href=True)
            if link:
                url = link["href"]
                if not url.startswith("https://"):
                    url = "https://www.bloomberg.com" + url
                urls.append(url)

    except Exception as e:
        st.write(f"Error: {e}")
    finally:
        if driver:
            driver.quit()

    return urls[:num_links]


def get_titles_from_urls(urls):
    articles = []
    for url in urls:
        # Extract the title from the URL
        match = re.search(
            r"https://www.bloomberg.com/news/[^/]+/\d{4}-\d{2}-\d{2}/(.+)$", url
        )
        if match:
            title = match.group(1).replace("-", " ").title()
            articles.append({"title": title, "url": url})
    return articles


def get_combinations(keywords, r):
    return list(combinations(keywords, r))


def fetch_volatility_data():
    sectors = {
        "XLE": "Energy",
        "XLF": "Financials",
        "XLK": "Technology",
        "XLY": "Consumer Discretionary",
        "XLP": "Consumer Staples",
        "XLV": "Health Care",
        "XLI": "Industrials",
        "XLB": "Materials",
        "XLRE": "Real Estate",
        "XLU": "Utilities",
    }
    volatility_data = []
    for symbol, sector in sectors.items():
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1mo")
        volatility = hist["Close"].pct_change().std() * (252**0.5)
        volatility_data.append((sector, volatility))
    return sorted(volatility_data, key=lambda x: x[1], reverse=True)


hk_tz = pytz.timezone("Europe/Istanbul")
hk_time = datetime.now(hk_tz)
current_date = hk_time.strftime("%B %d, %Y")
current_hour = hk_time.hour

# Language selection for UI
language = st.selectbox("Choose your language", ("English", "Türkçe"))

if language == "Türkçe":
    greeting = (
        "Günaydın"
        if 5 <= current_hour < 12
        else "Tünaydın"
        if 12 <= current_hour < 18
        else "İyi Geceler"
    )
    instructions = "Lütfen aramak istediğiniz anahtar kelimeleri girin (en fazla 10):"
    num_keywords_label = "Anahtar Kelime Sayısı"
    num_links_label = "Kaç bağlantı gösterilsin?"
    fetch_button_label = "Makale Getir"
    volatility_check_label = "Volatilite Kontrolü"
    recent_news_label = "Piyasayı Etkileyebilecek Güncel Haberler"
    volatility_data_label = "En Volatil Sektörler:"
else:
    greeting = (
        "Good Morning"
        if 5 <= current_hour < 12
        else "Good Afternoon"
        if 12 <= current_hour < 18
        else "Good Night"
    )
    instructions = (
        "Please enter the number of keywords you want to search for (up to 10):"
    )
    num_keywords_label = "Number of Keywords"
    num_links_label = "How many links to show?"
    fetch_button_label = "Fetch Articles"
    volatility_check_label = "Volatility Check"
    recent_news_label = "Recent News Impact"
    volatility_data_label = "Most Volatile Sectors:"

st.title(f"{greeting} Serkan")
st.markdown(
    f"## {current_date} ve işte en son haberler:"
    if language == "Türkçe"
    else f"## Today is {current_date} and here are the latest news:"
)

st.write(instructions)
num_keywords = st.slider(num_keywords_label, 1, 10, 3)

keywords = []
for i in range(1, num_keywords + 1):
    keyword = st.text_input(f"Keyword {i}", key=f"keyword_{i}")
    if keyword:
        keywords.append(keyword)

num_links = st.slider(num_links_label, 1, 30, 10)

if st.button(fetch_button_label):
    if keywords:
        st.write(
            f"{'Fetching top' if language == 'English' else 'Top'} {num_links} {'articles' if language == 'English' else 'makaleler'} for keywords: {', '.join(keywords)}"
        )

        st.write("### Financial Times Articles")
        ft_articles = fetch_ft_articles(keywords, num_links)
        for i, article in enumerate(ft_articles, start=1):
            st.write(f"{i}. [{article['title']}]({article['url']})")

        st.write("### Bloomberg Articles")
        bloomberg_urls = []
        for r in range(len(keywords), 0, -1):
            if len(bloomberg_urls) >= num_links:
                break
            keyword_combinations = get_combinations(keywords, r)
            for combo in keyword_combinations:
                if len(bloomberg_urls) >= num_links:
                    break
                try:
                    bloomberg_urls += fetch_bloomberg_article_urls(
                        combo, num_links - len(bloomberg_urls)
                    )
                except Exception as e:
                    st.write(f"Error fetching articles for combination {combo}: {e}")

        bloomberg_articles = get_titles_from_urls(bloomberg_urls)
        for i, article in enumerate(bloomberg_articles, start=1):
            st.write(f"{i}. [{article['title']}]({article['url']})")
    else:
        st.write(
            "Please enter at least one keyword."
            if language == "English"
            else "Lütfen en az bir anahtar kelime girin."
        )

st.write(volatility_check_label)
volatility_data = fetch_volatility_data()
st.write(volatility_data_label)
for sector, volatility in volatility_data:
    st.write(f"{sector}: {volatility:.2%}")

st.write(recent_news_label)
st.write("Placeholder for recent impactful news...")
