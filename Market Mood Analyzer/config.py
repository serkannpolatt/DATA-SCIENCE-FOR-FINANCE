"""
Configuration file for News Sentiment Scanner
"""

# API and URL configurations
GOOGLE_NEWS_RSS_BASE_URL = "https://news.google.com/rss/search?q={}"

# Request configurations
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

# Sentiment analysis configurations
SENTIMENT_THRESHOLD_POSITIVE = 0.05
SENTIMENT_THRESHOLD_NEGATIVE = -0.05

# FinBERT model configurations (optional)
FINBERT_MODEL_NAME = "yiyanghkust/finbert-tone"
FINBERT_MAX_LENGTH = 512

# Content extraction configurations
MAX_CONTENT_LENGTH = 5000
MIN_CONTENT_LENGTH = 50

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Default search queries for gold market analysis
DEFAULT_GOLD_QUERIES = [
    "gold market",
    "gold price",
    "gold news",
    "gold trends",
    "gold analysis",
    "gold forecast",
    "gold investment",
]

# Default number of articles per query
DEFAULT_ARTICLES_PER_QUERY = 10

# Output configurations
ENABLE_DETAILED_OUTPUT = True
ENABLE_PROGRESS_BAR = True
