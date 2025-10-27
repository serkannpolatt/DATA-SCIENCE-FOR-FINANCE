# 📈 News Sentiment Scanner

Advanced news sentiment analysis tool - A comprehensive solution for collecting news articles and analyzing market sentiment using VADER and FinBERT sentiment analysis models.

## 🚀 Features

- **🔍 Smart News Collection**: Automatic news gathering from Google News RSS feeds
- **🧠 Multi-Model Sentiment Analysis**: VADER and optional FinBERT models
- **📊 Detailed Analysis**: Title and content analysis options
- **🛡️ Reliable Performance**: Error handling and retry mechanisms
- **⚙️ Easy Configuration**: Centralized configuration system
- **📈 Visual Results**: Emoji-rich and colorful outputs
- **🔧 Modular Design**: Clean code architecture



## 🎯 Usage

### Basic Usage
```python
from sentiment_analysis import NewsSentimentScanner

# Initialize scanner
scanner = NewsSentimentScanner()

# Perform sentiment analysis for gold market
articles = scanner.scan_sentiment()

# Display results
scanner.print_detailed_results(articles)
scanner.print_summary(articles)
```

### Advanced Usage
```python
# Analysis with FinBERT model
scanner = NewsSentimentScanner(use_finbert=True)

# Custom queries analysis
custom_queries = ["bitcoin price", "crypto market", "blockchain news"]
articles = scanner.scan_sentiment(
    queries=custom_queries,
    articles_per_query=15,
    analyze_content=True  # Enable content analysis
)
```

### Command Line Execution
```bash
python sentiment_analysis.py
```

## ⚙️ Configuration

You can modify settings in the `config.py` file:

```python
# Sentiment thresholds
SENTIMENT_THRESHOLD_POSITIVE = 0.05
SENTIMENT_THRESHOLD_NEGATIVE = -0.05

# Number of articles
DEFAULT_ARTICLES_PER_QUERY = 10

# Default search queries
DEFAULT_GOLD_QUERIES = [
    "gold market",
    "gold price", 
    "gold investment"
]

# Output settings
ENABLE_DETAILED_OUTPUT = True
```

## 📊 Output Examples

### Detailed Analysis
```
📊 DETAILED SENTIMENT ANALYSIS RESULTS
================================================================================

[1] 📈 Gold Prices Surge to New Highs Amid Economic Uncertainty
🔗 Link: https://example.com/news1
📅 Published: Mon, 25 Oct 2025 10:30:00 GMT
💭 Sentiment: Positive (Score: 0.742)

[2] 📉 Gold Market Faces Pressure from Rising Interest Rates
🔗 Link: https://example.com/news2
📅 Published: Mon, 25 Oct 2025 09:15:00 GMT
💭 Sentiment: Negative (Score: -0.521)
```

### Summary Report
```
📊 MARKET SENTIMENT SUMMARY
==================================================
Total articles analyzed: 70
Sentiment Distribution:
  Positive: 28 (40.0%)
  Negative: 21 (30.0%)
  Neutral: 21 (30.0%)

💡 Market Outlook:
   🟢 BULLISH - Predominantly positive sentiment
```

## 🏗️ Project Structure

```
NewsSentimentScanner/
├── sentiment_analysis.py    # Main application file
├── config.py               # Configuration settings
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Main Classes

### `NewsSentimentScanner`
Main analysis class for coordinating news collection and sentiment analysis.

**Methods:**
- `scan_sentiment()`: News collection and analysis
- `print_detailed_results()`: Print detailed results
- `print_summary()`: Summary report

### `SentimentAnalyzer`
Multi-model sentiment analysis engine.

**Features:**
- VADER sentiment analyzer
- Optional FinBERT model
- Automatic fallback mechanism

### `NewsCollector`
News collection and content extraction.

**Features:**
- RSS feed parsing
- Error-tolerant content extraction
- Retry mechanism

## 🎨 Sentiment Analysis Models

### VADER (Default)
- **Advantages**: Fast, lightweight, optimized for social media texts
- **Usage**: Title analysis, quick results
- **Output**: Score between -1 (very negative) to +1 (very positive)

### FinBERT (Optional)
- **Advantages**: Specialized training for financial texts, high accuracy
- **Usage**: Detailed financial analysis
- **Requirements**: Additional memory and computational power

## 🔒 Error Handling

- **Connection Errors**: Automatic retry (3 attempts)
- **Parsing Errors**: Graceful degradation
- **Model Loading**: Automatic fallback (FinBERT → VADER)
- **Logging System**: Detailed error logging

## 🚀 Performance Tips

1. **Use VADER**: Disable FinBERT for faster results
2. **Query Optimization**: Use specific search terms
3. **Article Count**: Increase count for larger datasets
4. **Content Analysis**: Enable only when necessary



## 📝 Version History

### v2.0.0 (2025-10-25)
- ✨ Complete rewrite
- 🏗️ Class-based modular structure
- 🔧 Centralized configuration system
- 🛡️ Advanced error handling
- 📊 Improved output formatting
- 🧠 FinBERT support

### v1.0.0
- 🎯 Basic sentiment analysis
- 📰 Google News integration
- 📈 VADER sentiment analyzer

## 🙏 Acknowledgments

- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) - Sentiment analysis
- [FinBERT](https://github.com/ProsusAI/finBERT) - Financial sentiment analysis
- [Feedparser](https://feedparser.readthedocs.io/) - RSS parsing
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing

---

