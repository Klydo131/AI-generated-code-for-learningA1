"""
Tech Stock News Notifier
Educational program for tracking tech stocks, news, and making investment decisions.
WARNING: For educational purposes only - not financial advice!
"""

import yfinance as yf
import requests
from datetime import datetime, timedelta
import time
from colorama import init, Fore, Style
import json

# Initialize colorama for colored terminal output
init(autoreset=True)

class StockNewsNotifier:
    def __init__(self):
        # Popular tech stocks to monitor
        self.tech_stocks = {
            'AAPL': 'Apple Inc.',
            'GOOGL': 'Alphabet Inc.',
            'MSFT': 'Microsoft Corporation',
            'TSLA': 'Tesla Inc.',
            'NVDA': 'NVIDIA Corporation',
            'META': 'Meta Platforms Inc.',
            'AMZN': 'Amazon.com Inc.',
            'NFLX': 'Netflix Inc.',
            'AMD': 'Advanced Micro Devices',
            'INTC': 'Intel Corporation',
            'ORCL': 'Oracle Corporation',
            'CRM': 'Salesforce Inc.',
            'ADBE': 'Adobe Inc.',
            'PYPL': 'PayPal Holdings',
            'SQ': 'Block Inc.',
        }
        self.selected_stocks = []
        self.stock_data_cache = {}

    def display_header(self):
        """Display program header"""
        print("\n" + "="*70)
        print(Fore.CYAN + Style.BRIGHT + "📊 TECH STOCK NEWS NOTIFIER 📰")
        print(Fore.YELLOW + "Educational Tool - Not Financial Advice!")
        print("="*70 + "\n")

    def fetch_stock_data(self, symbol):
        """Fetch real-time stock data for a given symbol"""
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            hist = stock.history(period="5d")

            if hist.empty:
                return None

            current_price = hist['Close'].iloc[-1]
            previous_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
            price_change = current_price - previous_close
            percent_change = (price_change / previous_close) * 100

            data = {
                'symbol': symbol,
                'name': info.get('longName', self.tech_stocks.get(symbol, 'Unknown')),
                'current_price': current_price,
                'price_change': price_change,
                'percent_change': percent_change,
                'volume': hist['Volume'].iloc[-1],
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('trailingPE', 'N/A'),
                'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
                'fifty_two_week_low': info.get('fiftyTwoWeekLow', 'N/A'),
            }

            self.stock_data_cache[symbol] = data
            return data

        except Exception as e:
            print(Fore.RED + f"Error fetching data for {symbol}: {str(e)}")
            return None

    def fetch_stock_news(self, symbol):
        """Fetch latest news for a stock"""
        try:
            stock = yf.Ticker(symbol)
            news = stock.news

            if not news:
                return []

            news_items = []
            for item in news[:5]:  # Get top 5 news items
                news_items.append({
                    'title': item.get('title', 'No title'),
                    'publisher': item.get('publisher', 'Unknown'),
                    'link': item.get('link', ''),
                    'published': datetime.fromtimestamp(item.get('providerPublishTime', 0)),
                    'type': item.get('type', 'NEWS'),
                })

            return news_items

        except Exception as e:
            print(Fore.RED + f"Error fetching news for {symbol}: {str(e)}")
            return []

    def display_stock_info(self, data):
        """Display detailed stock information"""
        if not data:
            return

        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}{data['symbol']} - {data['name']}")
        print(f"{Fore.CYAN}{'='*70}")

        # Price information with color coding
        price_color = Fore.GREEN if data['price_change'] >= 0 else Fore.RED
        change_symbol = "▲" if data['price_change'] >= 0 else "▼"

        print(f"{Fore.WHITE}Current Price: {price_color}${data['current_price']:.2f}")
        print(f"{Fore.WHITE}Change: {price_color}{change_symbol} ${abs(data['price_change']):.2f} ({data['percent_change']:.2f}%)")
        print(f"{Fore.WHITE}Volume: {Fore.YELLOW}{data['volume']:,}")

        if data['market_cap'] != 'N/A':
            print(f"{Fore.WHITE}Market Cap: {Fore.YELLOW}${data['market_cap']:,.0f}")

        if data['pe_ratio'] != 'N/A':
            print(f"{Fore.WHITE}P/E Ratio: {Fore.YELLOW}{data['pe_ratio']:.2f}")

        if data['fifty_two_week_high'] != 'N/A':
            print(f"{Fore.WHITE}52-Week High: {Fore.YELLOW}${data['fifty_two_week_high']:.2f}")

        if data['fifty_two_week_low'] != 'N/A':
            print(f"{Fore.WHITE}52-Week Low: {Fore.YELLOW}${data['fifty_two_week_low']:.2f}")

    def display_news(self, symbol, news_items):
        """Display news for a stock"""
        print(f"\n{Fore.MAGENTA}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}📰 LATEST NEWS FOR {symbol}")
        print(f"{Fore.MAGENTA}{'='*70}")

        if not news_items:
            print(Fore.YELLOW + "No recent news available for this stock.")
            return

        for i, news in enumerate(news_items, 1):
            print(f"\n{Fore.CYAN}{i}. {news['title']}")
            print(f"   {Fore.WHITE}Publisher: {news['publisher']}")
            print(f"   {Fore.WHITE}Published: {news['published'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   {Fore.BLUE}Link: {news['link']}")

    def analyze_investment_signal(self, data, news_items):
        """Provide basic investment insights based on data and news"""
        print(f"\n{Fore.GREEN}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}💡 INVESTMENT ANALYSIS")
        print(f"{Fore.GREEN}{'='*70}")

        signals = []

        # Price momentum analysis
        if data['percent_change'] > 3:
            signals.append((Fore.GREEN, "🔥 Strong positive momentum (+3% or more)"))
        elif data['percent_change'] > 1:
            signals.append((Fore.GREEN, "📈 Positive momentum"))
        elif data['percent_change'] < -3:
            signals.append((Fore.RED, "⚠️  Strong negative momentum (-3% or more)"))
        elif data['percent_change'] < -1:
            signals.append((Fore.RED, "📉 Negative momentum"))
        else:
            signals.append((Fore.YELLOW, "➡️  Stable price movement"))

        # Volume analysis
        if isinstance(data['volume'], (int, float)):
            signals.append((Fore.CYAN, f"📊 Trading Volume: {data['volume']:,} shares"))

        # News sentiment
        if len(news_items) > 3:
            signals.append((Fore.CYAN, f"📰 High news activity ({len(news_items)} recent articles)"))
        elif len(news_items) > 0:
            signals.append((Fore.YELLOW, f"📰 Moderate news activity ({len(news_items)} recent articles)"))
        else:
            signals.append((Fore.YELLOW, "📰 Low news activity"))

        # 52-week analysis
        if data['fifty_two_week_high'] != 'N/A' and data['fifty_two_week_low'] != 'N/A':
            price = data['current_price']
            high = data['fifty_two_week_high']
            low = data['fifty_two_week_low']
            position = (price - low) / (high - low) * 100

            if position > 80:
                signals.append((Fore.YELLOW, f"⚠️  Near 52-week high ({position:.1f}% of range)"))
            elif position < 20:
                signals.append((Fore.GREEN, f"💎 Near 52-week low ({position:.1f}% of range) - Potential value"))
            else:
                signals.append((Fore.CYAN, f"📍 Mid-range position ({position:.1f}% of 52-week range)"))

        # Display signals
        for color, signal in signals:
            print(f"{color}{signal}")

        print(f"\n{Fore.YELLOW}{Style.BRIGHT}⚠️  DISCLAIMER: This is educational analysis only.")
        print(f"{Fore.YELLOW}Always do thorough research and consult financial advisors before investing!")

    def display_all_stocks_summary(self):
        """Display summary of all tech stocks"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}📊 TECH STOCKS OVERVIEW")
        print(f"{Fore.CYAN}{'='*70}\n")

        print(f"{Fore.WHITE}{'Symbol':<8} {'Company':<30} {'Price':<12} {'Change'}")
        print("-" * 70)

        for symbol, name in self.tech_stocks.items():
            print(f"{Fore.YELLOW}Fetching {symbol}...", end='\r')
            data = self.fetch_stock_data(symbol)

            if data:
                price_color = Fore.GREEN if data['price_change'] >= 0 else Fore.RED
                change_symbol = "▲" if data['price_change'] >= 0 else "▼"

                print(f"{Fore.CYAN}{symbol:<8} {Fore.WHITE}{name[:28]:<30} "
                      f"{price_color}${data['current_price']:<10.2f} "
                      f"{change_symbol} {data['percent_change']:>6.2f}%")
            else:
                print(f"{Fore.CYAN}{symbol:<8} {Fore.WHITE}{name[:28]:<30} {Fore.RED}Error fetching data")

        print()

    def select_stocks_to_monitor(self):
        """Allow user to select stocks to monitor"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}SELECT STOCKS TO MONITOR")
        print(f"{Fore.CYAN}{'='*70}\n")

        print("Available tech stocks:")
        stocks_list = list(self.tech_stocks.items())

        for i, (symbol, name) in enumerate(stocks_list, 1):
            print(f"{Fore.YELLOW}{i:2d}. {Fore.CYAN}{symbol:<8} {Fore.WHITE}- {name}")

        print(f"\n{Fore.WHITE}Enter stock numbers separated by commas (e.g., 1,3,5)")
        print(f"Or type 'all' to select all stocks, 'back' to return:")

        choice = input(f"{Fore.GREEN}> ").strip().lower()

        if choice == 'back':
            return
        elif choice == 'all':
            self.selected_stocks = list(self.tech_stocks.keys())
            print(f"{Fore.GREEN}✓ All stocks selected!")
        else:
            try:
                indices = [int(x.strip()) for x in choice.split(',')]
                self.selected_stocks = [stocks_list[i-1][0] for i in indices if 1 <= i <= len(stocks_list)]
                print(f"{Fore.GREEN}✓ Selected {len(self.selected_stocks)} stocks!")
            except (ValueError, IndexError):
                print(f"{Fore.RED}Invalid selection. Please try again.")

    def view_selected_stocks_detail(self):
        """View detailed information for selected stocks"""
        if not self.selected_stocks:
            print(f"{Fore.RED}No stocks selected. Please select stocks first.")
            return

        for symbol in self.selected_stocks:
            print(f"\n{Fore.YELLOW}Loading data for {symbol}...")

            # Fetch and display stock data
            data = self.fetch_stock_data(symbol)
            if data:
                self.display_stock_info(data)

                # Fetch and display news
                news = self.fetch_stock_news(symbol)
                self.display_news(symbol, news)

                # Display investment analysis
                self.analyze_investment_signal(data, news)

                print(f"\n{Fore.CYAN}{'-'*70}")

                # Pause between stocks
                if symbol != self.selected_stocks[-1]:
                    input(f"\n{Fore.WHITE}Press Enter to view next stock...")

    def check_for_alerts(self):
        """Check for significant price movements or news"""
        if not self.selected_stocks:
            print(f"{Fore.RED}No stocks selected. Please select stocks first.")
            return

        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.WHITE}{Style.BRIGHT}🔔 CHECKING FOR ALERTS")
        print(f"{Fore.CYAN}{'='*70}\n")

        alerts = []

        for symbol in self.selected_stocks:
            data = self.fetch_stock_data(symbol)
            news = self.fetch_stock_news(symbol)

            if data:
                # Check for significant price movements
                if abs(data['percent_change']) >= 3:
                    alert_type = "🔥 ALERT" if data['percent_change'] > 0 else "⚠️  ALERT"
                    color = Fore.GREEN if data['percent_change'] > 0 else Fore.RED
                    alerts.append((color, f"{alert_type}: {symbol} moved {data['percent_change']:.2f}% today!"))

                # Check for high news activity
                if len(news) >= 3:
                    alerts.append((Fore.CYAN, f"📰 NEWS: {symbol} has {len(news)} recent articles"))

        if alerts:
            for color, alert in alerts:
                print(f"{color}{alert}")
        else:
            print(f"{Fore.YELLOW}No significant alerts at this time.")

        print()

    def run(self):
        """Main program loop"""
        while True:
            self.display_header()

            print(f"{Fore.WHITE}MAIN MENU:")
            print(f"{Fore.CYAN}1. {Fore.WHITE}View All Tech Stocks Overview")
            print(f"{Fore.CYAN}2. {Fore.WHITE}Select Stocks to Monitor")
            print(f"{Fore.CYAN}3. {Fore.WHITE}View Selected Stocks (Detailed)")
            print(f"{Fore.CYAN}4. {Fore.WHITE}Check for Alerts")
            print(f"{Fore.CYAN}5. {Fore.WHITE}View Currently Selected Stocks")
            print(f"{Fore.CYAN}6. {Fore.WHITE}Exit")

            if self.selected_stocks:
                print(f"\n{Fore.GREEN}Currently monitoring: {', '.join(self.selected_stocks)}")

            choice = input(f"\n{Fore.GREEN}Enter your choice (1-6): ").strip()

            if choice == '1':
                self.display_all_stocks_summary()
                input(f"\n{Fore.WHITE}Press Enter to continue...")

            elif choice == '2':
                self.select_stocks_to_monitor()
                input(f"\n{Fore.WHITE}Press Enter to continue...")

            elif choice == '3':
                self.view_selected_stocks_detail()
                input(f"\n{Fore.WHITE}Press Enter to continue...")

            elif choice == '4':
                self.check_for_alerts()
                input(f"\n{Fore.WHITE}Press Enter to continue...")

            elif choice == '5':
                if self.selected_stocks:
                    print(f"\n{Fore.GREEN}Currently selected stocks:")
                    for symbol in self.selected_stocks:
                        print(f"{Fore.CYAN}  • {symbol} - {self.tech_stocks[symbol]}")
                else:
                    print(f"\n{Fore.YELLOW}No stocks currently selected.")
                input(f"\n{Fore.WHITE}Press Enter to continue...")

            elif choice == '6':
                print(f"\n{Fore.CYAN}Thank you for using Tech Stock News Notifier!")
                print(f"{Fore.YELLOW}Remember: Always do your own research before investing!")
                break

            else:
                print(f"{Fore.RED}Invalid choice. Please try again.")
                time.sleep(1)


def main():
    """Entry point for the program"""
    print(f"{Fore.YELLOW}Initializing Tech Stock News Notifier...")
    print(f"{Fore.YELLOW}This may take a moment...\n")

    notifier = StockNewsNotifier()

    try:
        notifier.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.CYAN}Program interrupted by user.")
        print(f"{Fore.YELLOW}Remember: Always do your own research before investing!")
    except Exception as e:
        print(f"\n{Fore.RED}An error occurred: {str(e)}")
        print(f"{Fore.YELLOW}Please try running the program again.")


if __name__ == "__main__":
    main()
