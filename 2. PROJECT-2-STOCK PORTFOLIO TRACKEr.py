import yfinance as yf

# FOR STARTING 
portfolio = {}

# TO ADD STOCKS TO THE PORTFOLIO
def add_stock(symbol):
    if symbol in portfolio:
        print(f"{symbol} is already in your portfolio.")
    else:
        stock = yf.Ticker(symbol)
        try:
            price = stock.history(period="1d").iloc[-1]["Close"]
            portfolio[symbol] = price
            print(f"{symbol} added to your portfolio at ${price:.2f}.")
        except Exception:
            print(f"Could not fetch data for {symbol}. Please check the symbol and try again.")

# TO REMOVE STOCK FROM THE PRTFOLIO
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from your portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")

# TO SHOW THE PRTFLIO
def show_portfolio():
    if portfolio:
        print("\nYour Portfolio:")
        for symbol, price in portfolio.items():
            print(f"{symbol}: ${price:.2f}")
    else:
        print("Your portfolio is empty.")

# TO DISPLAY STOCK SYMBOLS
def show_available_stocks():
    print("\nHere are some popular stocks and their symbols:")
    popular_stocks = {
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Amazon": "AMZN",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX"
    }
    for company, symbol in popular_stocks.items():
        print(f"{company}: {symbol}")
    print("\nFor more symbols, visit: https://finance.yahoo.com/screener/new/")

# TO SEARCH STOCK BY NAME
def search_stock_symbol(company_name):
    stock_list = {
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Amazon": "AMZN",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX"
    }
    symbol = stock_list.get(company_name.title())
    if symbol:
        print(f"The stock symbol for {company_name} is {symbol}.")
    else:
        print(f"Sorry, no stock symbol found for {company_name}.")

# MAIN ONE
def main():
    username = input("Enter your name: ")
    print(f"Welcome to STOCK PORTFOLIO TRACKER, Let's Go..., {username}!")
    while True:
        print("\nMenu:")
        print("1. Add a stock to your portfolio")
        print("2. Remove a stock from your portfolio")
        print("3. Show your portfolio")
        print("4. Exit")
        print("5. Show available stock symbols")
        print("6. Search for a stock symbol by company name")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            symbol = input("Enter the stock symbol to add: ").upper()
            add_stock(symbol)
        elif choice == "2":
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            show_portfolio()
        elif choice == "4":
            print("Thank you for using the Stock Portfolio Tracker. Goodbye!")
            break
        elif choice == "5":
            show_available_stocks()
        elif choice == "6":
            company = input("Enter the company name to search: ").strip()
            search_stock_symbol(company)
        else:
            print("Invalid choice. Please try again.")

# LAST
main()
