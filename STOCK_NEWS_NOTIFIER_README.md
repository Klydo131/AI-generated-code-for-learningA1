# 📊 Tech Stock News Notifier

An educational Python program that helps you track tech stocks, scrape news, and analyze data to make informed investment decisions.

## ⚠️ Important Disclaimer

**This program is for EDUCATIONAL PURPOSES ONLY!** This is not financial advice. Always:
- Do your own thorough research
- Consult with licensed financial advisors
- Understand that all investing carries risk
- Never invest money you cannot afford to lose

## 🌟 Features

### 1. **Stock Data Scraping**
- Real-time stock price data from Yahoo Finance
- Price changes and percentage movements
- Trading volume information
- Market cap and P/E ratios
- 52-week high/low tracking

### 2. **News Aggregation**
- Latest news articles for each stock
- Publisher information
- Article links for further reading
- Timestamps for news relevance

### 3. **Interactive Stock Selection**
- Choose from 15 popular tech stocks
- Select individual stocks or all at once
- Manage your watchlist easily

### 4. **Investment Analysis**
- Price momentum indicators
- Volume analysis
- News activity tracking
- 52-week range position analysis
- Color-coded signals for easy understanding

### 5. **Alert System**
- Notifications for significant price movements (±3% or more)
- High news activity alerts
- Quick overview of important changes

## 📋 Tech Stocks Included

- **AAPL** - Apple Inc.
- **GOOGL** - Alphabet Inc.
- **MSFT** - Microsoft Corporation
- **TSLA** - Tesla Inc.
- **NVDA** - NVIDIA Corporation
- **META** - Meta Platforms Inc.
- **AMZN** - Amazon.com Inc.
- **NFLX** - Netflix Inc.
- **AMD** - Advanced Micro Devices
- **INTC** - Intel Corporation
- **ORCL** - Oracle Corporation
- **CRM** - Salesforce Inc.
- **ADBE** - Adobe Inc.
- **PYPL** - PayPal Holdings
- **SQ** - Block Inc.

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for fetching stock data)

### Setup Steps

1. **Install required packages:**
   ```bash
   pip install -r stock_news_requirements.txt
   ```

   Or install manually:
   ```bash
   pip install yfinance requests colorama
   ```

2. **Run the program:**
   ```bash
   python stock_news_notifier.py
   ```

## 📖 How to Use

### Main Menu Options:

1. **View All Tech Stocks Overview**
   - See a quick summary of all 15 tech stocks
   - Compare prices and daily changes at a glance
   - Identify which stocks are moving

2. **Select Stocks to Monitor**
   - Choose specific stocks you want to track
   - Select by number (e.g., "1,3,5" for multiple stocks)
   - Type "all" to monitor all stocks
   - Your selections are saved for the session

3. **View Selected Stocks (Detailed)**
   - Get comprehensive information for your selected stocks
   - See current prices, changes, and key metrics
   - Read the latest news articles
   - Get investment analysis and signals

4. **Check for Alerts**
   - Quick scan for significant movements
   - See stocks with ±3% or more price changes
   - Identify stocks with high news activity

5. **View Currently Selected Stocks**
   - Review your current watchlist
   - See which stocks you're monitoring

6. **Exit**
   - Close the program safely

## 🎨 Features Explained

### Color-Coded Display
- 🟢 **Green**: Positive changes, bullish signals
- 🔴 **Red**: Negative changes, bearish signals
- 🟡 **Yellow**: Neutral information, warnings
- 🔵 **Cyan**: General information
- 🟣 **Magenta**: News sections

### Investment Analysis Signals

The program provides several analytical signals:

- **Price Momentum**
  - 🔥 Strong positive momentum (>3%)
  - 📈 Positive momentum (>1%)
  - 📉 Negative momentum (<-1%)
  - ⚠️ Strong negative momentum (<-3%)
  - ➡️ Stable price movement

- **52-Week Range Analysis**
  - Near 52-week high (>80% of range) ⚠️
  - Near 52-week low (<20% of range) 💎 Potential value
  - Mid-range position (20-80%)

- **News Activity**
  - High news activity (>3 recent articles)
  - Moderate news activity (1-3 articles)
  - Low news activity (no recent articles)

## 🔍 Example Use Case

**Scenario**: You're interested in AI chip companies and want to compare NVIDIA and AMD.

1. Run the program
2. Select option 2 (Select Stocks to Monitor)
3. Enter "5,9" (for NVDA and AMD)
4. Select option 3 (View Selected Stocks)
5. Review detailed data, news, and analysis for both companies
6. Make informed decisions based on the information

## 🛠️ Technical Details

### Data Sources
- **Stock Data**: Yahoo Finance API via yfinance library
- **News**: Yahoo Finance news feed
- **Updates**: Real-time when you request data

### Data Provided
- Current stock price
- Price change ($ and %)
- Trading volume
- Market capitalization
- P/E ratio
- 52-week high/low
- Latest news articles (up to 5 per stock)
- Publisher and timestamp for each article

## ⚡ Tips for Best Use

1. **Run regularly**: Market data changes throughout the trading day
2. **Read the news**: Don't just look at numbers - understand the context
3. **Compare stocks**: Use the overview to spot relative performance
4. **Watch alerts**: Significant movements often indicate important news
5. **Do more research**: Use this as a starting point, not your only source

## 🐛 Troubleshooting

### "Error fetching data"
- Check your internet connection
- Yahoo Finance may be temporarily unavailable
- Some stocks may have data delays

### Slow performance
- Fetching data for multiple stocks takes time
- Be patient, especially with option 1 (all stocks)
- Select fewer stocks if speed is important

### No news available
- Not all stocks have frequent news
- News feed may be temporarily empty
- Try again later or check different stocks

## 📚 Learning Objectives

This program demonstrates:
- **API Integration**: Working with financial data APIs
- **Data Scraping**: Fetching and parsing real-time information
- **User Interface**: Creating interactive CLI applications
- **Data Analysis**: Basic financial metrics and indicators
- **Error Handling**: Managing network requests and data issues
- **Code Organization**: Clean class-based structure

## 🔮 Future Enhancements (Ideas for Learning)

- Add email/SMS notifications
- Create price alerts at custom thresholds
- Add technical indicators (RSI, MACD, Moving Averages)
- Save watchlists to file
- Add historical price charts
- Include crypto assets
- Add sentiment analysis for news
- Export data to CSV/Excel

## 📄 License

Educational use only. Not for production trading systems.

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Improve the analysis algorithms
- Add more data sources
- Enhance the user interface
- Fix bugs or improve error handling

## 💡 Educational Note

This program teaches important concepts:
- **Financial APIs**: How to access market data
- **Real-time data**: Handling live information
- **Decision support**: Presenting data for analysis
- **User experience**: Making complex data understandable
- **Risk awareness**: Importance of disclaimers and education

Remember: The best investment is in your education! Use this tool to learn about markets, programming, and data analysis.

---

**Happy Learning! 🎓📈**
