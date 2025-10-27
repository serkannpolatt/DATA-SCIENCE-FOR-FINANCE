"""
News Sentiment Scanner - Advanced sentiment analysis for news articles

A comprehensive tool for fetching news articles and analyzing market sentiment
using multiple sentiment analysis models including VADER and optional FinBERT.
"""

import feedparser
from typing import List, Tuple
from dataclasses import dataclass
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Optional imports for advanced features
try:
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch
    import numpy as np

    FINBERT_AVAILABLE = True
except ImportError:
    FINBERT_AVAILABLE = False

from config import (
    SENTIMENT_THRESHOLD_POSITIVE,
    SENTIMENT_THRESHOLD_NEGATIVE,
    DEFAULT_GOLD_QUERIES,
    DEFAULT_ARTICLES_PER_QUERY,
    FINBERT_MODEL_NAME,
    FINBERT_MAX_LENGTH,
    ENABLE_DETAILED_OUTPUT,
)
from utils import (
    setup_logging,
    create_google_news_url,
    fetch_url_with_retry,
    extract_text_content,
    calculate_sentiment_distribution,
    format_sentiment_summary,
)


@dataclass
class NewsArticle:
    """Data class for news articles"""

    title: str
    link: str
    published: str
    content: str = ""
    sentiment: str = ""
    polarity: float = 0.0
    confidence: float = 0.0


class SentimentAnalyzer:
    """Advanced sentiment analyzer with multiple models"""

    def __init__(self, use_finbert: bool = False):
        self.logger = setup_logging(f"{__name__}.SentimentAnalyzer")
        self.use_finbert = use_finbert and FINBERT_AVAILABLE

        # Initialize VADER analyzer
        self.vader_analyzer = SentimentIntensityAnalyzer()

        # Initialize FinBERT if requested and available
        self.finbert_model = None
        self.finbert_tokenizer = None

        if self.use_finbert:
            try:
                self.finbert_model = AutoModelForSequenceClassification.from_pretrained(
                    FINBERT_MODEL_NAME
                )
                self.finbert_tokenizer = AutoTokenizer.from_pretrained(
                    FINBERT_MODEL_NAME
                )
                self.finbert_labels = ["Positive", "Negative", "Neutral"]
                self.logger.info("FinBERT model loaded successfully")
            except Exception as e:
                self.logger.warning(f"Failed to load FinBERT model: {str(e)}")
                self.use_finbert = False

    def analyze_with_vader(self, text: str) -> Tuple[float, str]:
        """Analyze sentiment using VADER"""
        if not text.strip():
            return 0.0, "Neutral"

        scores = self.vader_analyzer.polarity_scores(text)
        polarity = scores["compound"]

        if polarity > SENTIMENT_THRESHOLD_POSITIVE:
            sentiment = "Positive"
        elif polarity < SENTIMENT_THRESHOLD_NEGATIVE:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return polarity, sentiment

    def analyze_with_finbert(self, text: str) -> Tuple[float, str]:
        """Analyze sentiment using FinBERT"""
        if not self.use_finbert or not text.strip():
            return 0.0, "Neutral"

        try:
            inputs = self.finbert_tokenizer(
                text,
                return_tensors="pt",
                truncation=True,
                max_length=FINBERT_MAX_LENGTH,
            )

            with torch.no_grad():
                outputs = self.finbert_model(**inputs)

            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=1).numpy()[0]
            max_index = np.argmax(probabilities)
            sentiment = self.finbert_labels[max_index]
            confidence = probabilities[max_index]

            return confidence, sentiment

        except Exception as e:
            self.logger.error(f"FinBERT analysis failed: {str(e)}")
            return self.analyze_with_vader(text)

    def analyze(self, text: str) -> Tuple[float, str]:
        """Analyze sentiment using the configured method"""
        if self.use_finbert:
            return self.analyze_with_finbert(text)
        else:
            return self.analyze_with_vader(text)


class NewsCollector:
    """Collects news articles from various sources"""

    def __init__(self):
        self.logger = setup_logging(f"{__name__}.NewsCollector")

    def fetch_news_from_rss(
        self, query: str, num_articles: int = DEFAULT_ARTICLES_PER_QUERY
    ) -> List[NewsArticle]:
        """Fetch news articles from RSS feed for given query"""
        try:
            rss_url = create_google_news_url(query)
            self.logger.info(f"Fetching RSS feed for query: {query}")

            feed = feedparser.parse(rss_url)

            if not feed.entries:
                self.logger.warning(f"No articles found for query: {query}")
                return []

            articles = []
            for item in feed.entries[:num_articles]:
                article = NewsArticle(
                    title=item.title,
                    link=item.link,
                    published=item.published,
                    content=self._fetch_article_content(item.link),
                )
                articles.append(article)

            self.logger.info(
                f"Successfully fetched {len(articles)} articles for query: {query}"
            )
            return articles

        except Exception as e:
            self.logger.error(f"Failed to fetch news for query '{query}': {str(e)}")
            return []

    def _fetch_article_content(self, url: str) -> str:
        """Fetch and extract content from article URL"""
        response = fetch_url_with_retry(url)
        if response is None:
            return ""

        try:
            content = extract_text_content(response.text)
            return content
        except Exception as e:
            self.logger.error(f"Failed to extract content from {url}: {str(e)}")
            return ""


class NewsSentimentScanner:
    """Main class for news sentiment analysis"""

    def __init__(self, use_finbert: bool = False):
        self.logger = setup_logging(f"{__name__}.NewsSentimentScanner")
        self.collector = NewsCollector()
        self.analyzer = SentimentAnalyzer(use_finbert=use_finbert)

    def scan_sentiment(
        self,
        queries: List[str] = None,
        articles_per_query: int = DEFAULT_ARTICLES_PER_QUERY,
        analyze_content: bool = False,
    ) -> List[NewsArticle]:
        """
        Scan sentiment for given queries

        Args:
            queries: List of search queries
            articles_per_query: Number of articles per query
            analyze_content: Whether to analyze full content or just titles

        Returns:
            List of analyzed articles
        """
        if queries is None:
            queries = DEFAULT_GOLD_QUERIES

        all_articles = []

        for query in queries:
            if ENABLE_DETAILED_OUTPUT:
                print(f"\n📰 Fetching articles for: '{query}'")

            articles = self.collector.fetch_news_from_rss(query, articles_per_query)

            # Analyze sentiment for each article
            for article in articles:
                text_to_analyze = (
                    article.content
                    if analyze_content and article.content
                    else article.title
                )
                polarity, sentiment = self.analyzer.analyze(text_to_analyze)

                article.sentiment = sentiment
                article.polarity = polarity
                article.confidence = abs(polarity)

            all_articles.extend(articles)

        self.logger.info(f"Total articles collected and analyzed: {len(all_articles)}")
        return all_articles

    def print_detailed_results(self, articles: List[NewsArticle]):
        """Print detailed analysis results"""
        if not ENABLE_DETAILED_OUTPUT:
            return

        print("\n" + "=" * 80)
        print(" 📊 DETAILED SENTIMENT ANALYSIS RESULTS")
        print("=" * 80)

        for idx, article in enumerate(articles, 1):
            sentiment_emoji = {"Positive": "📈", "Negative": "📉", "Neutral": "➖"}
            emoji = sentiment_emoji.get(article.sentiment, "❓")

            print(f"\n[{idx}] {emoji} {article.title}")
            print(f"🔗 Link: {article.link}")
            print(f"📅 Published: {article.published}")
            print(f"💭 Sentiment: {article.sentiment} (Score: {article.polarity:.3f})")

            if len(articles) > 20 and idx == 20:
                remaining = len(articles) - 20
                print(f"\n... and {remaining} more articles")
                break

    def print_summary(self, articles: List[NewsArticle]):
        """Print sentiment summary"""
        sentiments = [article.sentiment for article in articles]
        stats = calculate_sentiment_distribution(sentiments)

        print("\n" + "=" * 50)
        print(" 📊 MARKET SENTIMENT SUMMARY")
        print("=" * 50)
        print(format_sentiment_summary(stats))

        # Additional insights
        if stats["total"] > 0:
            positive_ratio = stats["percentages"]["Positive"]
            negative_ratio = stats["percentages"]["Negative"]

            print("\n💡 Market Outlook:")
            if positive_ratio > negative_ratio + 10:
                print("   🟢 BULLISH - Predominantly positive sentiment")
            elif negative_ratio > positive_ratio + 10:
                print("   🔴 BEARISH - Predominantly negative sentiment")
            else:
                print("   🟡 MIXED - Balanced sentiment indicators")


def main():
    """Main execution function"""
    print("🚀 Starting News Sentiment Scanner...")
    print("=" * 60)

    # Initialize scanner
    scanner = NewsSentimentScanner(use_finbert=False)  # Set to True to use FinBERT

    # Perform sentiment analysis
    articles = scanner.scan_sentiment()

    if not articles:
        print("❌ No articles found. Please check your internet connection.")
        return

    # Display results
    scanner.print_detailed_results(articles)
    scanner.print_summary(articles)

    print("\n✅ Analysis completed successfully!")
    print(
        f"📊 Analyzed {len(articles)} articles from {len(DEFAULT_GOLD_QUERIES)} different queries"
    )


if __name__ == "__main__":
    main()
