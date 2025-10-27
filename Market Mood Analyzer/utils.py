"""
Utility functions for News Sentiment Scanner
"""

import logging
import time
from urllib.parse import quote
from typing import Optional, Dict, Any
import requests
from bs4 import BeautifulSoup

from config import (
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY,
    MAX_CONTENT_LENGTH,
    MIN_CONTENT_LENGTH,
    LOG_LEVEL,
    LOG_FORMAT,
)


def setup_logging(name: str = __name__) -> logging.Logger:
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format=LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(name)


def create_google_news_url(query: str) -> str:
    """Create Google News RSS URL for given query"""
    from config import GOOGLE_NEWS_RSS_BASE_URL

    encoded_query = quote(query)
    return GOOGLE_NEWS_RSS_BASE_URL.format(encoded_query)


def fetch_url_with_retry(
    url: str, timeout: int = REQUEST_TIMEOUT
) -> Optional[requests.Response]:
    """
    Fetch URL with retry mechanism

    Args:
        url: URL to fetch
        timeout: Request timeout in seconds

    Returns:
        Response object or None if failed
    """
    logger = logging.getLogger(__name__)

    for attempt in range(MAX_RETRIES):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, timeout=timeout, headers=headers)
            response.raise_for_status()
            return response

        except requests.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for URL {url}: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"All {MAX_RETRIES} attempts failed for URL {url}")

    return None


def extract_text_content(html_content: str) -> str:
    """
    Extract clean text content from HTML

    Args:
        html_content: Raw HTML content

    Returns:
        Cleaned text content
    """
    try:
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text from paragraphs
        paragraphs = soup.find_all("p")
        if not paragraphs:
            # Fallback to all text if no paragraphs found
            content = soup.get_text()
        else:
            content = " ".join([p.get_text() for p in paragraphs])

        # Clean up the text
        content = " ".join(content.split())  # Remove extra whitespace

        # Limit content length
        if len(content) > MAX_CONTENT_LENGTH:
            content = content[:MAX_CONTENT_LENGTH] + "..."

        return content.strip() if len(content) >= MIN_CONTENT_LENGTH else ""

    except Exception as e:
        logging.getLogger(__name__).error(f"Error extracting text content: {str(e)}")
        return ""


def calculate_sentiment_distribution(sentiments: list) -> Dict[str, Any]:
    """
    Calculate sentiment distribution statistics

    Args:
        sentiments: List of sentiment labels

    Returns:
        Dictionary containing sentiment statistics
    """
    total = len(sentiments)
    if total == 0:
        return {"total": 0, "distribution": {}, "percentages": {}}

    distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for sentiment in sentiments:
        distribution[sentiment] += 1

    percentages = {
        sentiment: (count / total) * 100 for sentiment, count in distribution.items()
    }

    return {"total": total, "distribution": distribution, "percentages": percentages}


def format_sentiment_summary(stats: Dict[str, Any]) -> str:
    """
    Format sentiment statistics for display

    Args:
        stats: Sentiment statistics dictionary

    Returns:
        Formatted string for display
    """
    if stats["total"] == 0:
        return "No articles analyzed."

    lines = [f"Total articles analyzed: {stats['total']}", "Sentiment Distribution:"]

    for sentiment in ["Positive", "Negative", "Neutral"]:
        count = stats["distribution"][sentiment]
        percentage = stats["percentages"][sentiment]
        lines.append(f"  {sentiment}: {count} ({percentage:.1f}%)")

    return "\n".join(lines)


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe file operations

    Args:
        filename: Original filename

    Returns:
        Sanitized filename
    """
    import re

    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", filename)
    # Limit length
    if len(sanitized) > 200:
        sanitized = sanitized[:200]
    return sanitized.strip()
