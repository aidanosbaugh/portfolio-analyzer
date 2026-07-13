import csv
import yfinance as yf 
import datetime as dt

## YFINANCE FUNCTIONS

def get_price(ticker):
   try:
        stock = yf.Ticker(ticker)
        return (stock.fast_info["lastPrice"])
   except Exception:
       return None

def update_price():
    print("Updating Prices ... ")
    for stock in stocks: 
        price = get_price(stock["Ticker"])
        if price is None:
            print(stock["Ticker"], "x failed")
            continue
        stock["Price"] = price
        print(f"{stock['Ticker']:6} ✓ {price:.2f}")
    save_portfolio()
    print("Portfolio succesfully updated")
    print(f"at {dt.datetime.today()}")
   


## CSV READING/WRITING FUNCTIONS
def load_portfolio():
    stocks = []

    with open("portfolio.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader: 
            stock = {
                "Ticker": row["Ticker"],
                "Price":float(row["Price"]),   
                "Original Price":float(row["Original Price"]),
                "Shares":int(row["Shares"])
            }
            stocks.append(stock)
    return stocks

def save_portfolio():
    fieldnames = ["Ticker", "Price", "Original Price", "Shares"]
    with open("portfolio.csv", mode="w", newline="", encoding="utf-8") as file:
        saver = csv.DictWriter(file, fieldnames=fieldnames)
        saver.writeheader()
        for stock in stocks:
            saver.writerow(stock)
        
def add_stock():
    ticker = input("Ticker: ").upper()

    if find_stock(ticker):
        print("Stock already exists")
        return
    try:
        price = float(input("Current Price: "))
        original_price = float(input("Purchase Price: "))
        shares = int(input("Shares: "))
    except ValueError:
        print("Please enter valid numbers")
        return

    stock = {
        "Ticker": ticker, 
        "Price": price, 
        "Original Price": original_price,
        "Shares": shares

    }

    confirm = input("Save changes (Y/N):").upper() 
    if confirm == "Y":
            stocks.append(stock)
            save_portfolio()
            print("Stock Added")
    else: 
        print("Cancelled")

def edit_stock():
    ticker = input("What stock would you like to edit?").upper()

    stock = find_stock(ticker)

    if stock is None:
        print("Stock not found")
        return
    
    print(stock)

    try: 
        new_price = float(input("New current price: "))
        new_shares = int(input("New Shares: "))
    except ValueError:
        print("Please enter a number")
        return


    confirm = input("Save changes? (Y/N):").upper()
    if confirm == "Y":
        stock["Price"] = new_price
        stock["Shares"] = new_shares
        save_portfolio()

def remove_stock():
    ticker = input("What stock woudl you like to remove?").upper()

    stock = find_stock(ticker)

    if stock is None:
        print("Stock not found")
        return
    
    delete_confirm = input(f"Are you sure you would like to remove {ticker}? (Y/N)").upper()
    if delete_confirm == "Y":
        stocks.remove(stock)
        save_portfolio()
        print("Stock Removed")
    elif delete_confirm == "N":
        print(f"=== Deletion Cancelled ===\n", "... Returning to menu ... \n", sep="")
        return
    else:
        print("Please enter Y/N")


## PORTFOLIO ANALYSIS / VALUATION FUNCTIONS

def single_stock_analyze():
    ticker = input("What stock would you like to view?").upper()
    stock = find_stock(ticker)
    
    if stock is None: 
        print(f"Error: {ticker} not found in portfolio")
    else:
        value = (value_stock(stock))
        profit = (profit_stock(stock))
        gain = (percent_gain(stock))
        
        print("-" * 35)    
        print(f"Stock: {ticker}", end="\n")
        print(f"Current value: ${value:.2f}")
        print(f"Profit: ${profit:.2f}")  
        print(f"Percent Gain: {gain:.2f}% ") 
        print("-" * 35)

def portfolio_analyze():
    origtotalval = original_total()
    totalval = total_value()
    totalprof = total_profit()
    portreturn = (total_profit()/original_total()) * 100
    print(f"=" * 8, "Portfolio Summary", "=" * 8)
    print("")
    print(f"Stocks owned: ", len(stocks))
    print(f"Original Portfolio Value: ${origtotalval:.2f}")
    print(f"Current Portfolio Value: ${totalval:.2f}")
    print(f"Current Portfolio Profit: ${totalprof:.2f}")
    print(f"Current Portfolio Return: {portreturn:.2f}%\n")
    print("=" * 35)
    for stock in stocks:
        print("=" * 35,)    
        print(f"Stock: {stock['Ticker']}")
        print("")
        print(f"Current value: ${value_stock(stock):.2f}")
        print(f"Profit: ${profit_stock(stock):.2f}")  
        print(f"Percent Gain: ${percent_gain(stock):.2f}% ") 
        print("=" * 35)
        
def find_stock(ticker):
    for stock in stocks:
        if ticker == stock["Ticker"]:
            return stock
    return None

def value_stock(stock):
    current_value = stock["Price"] * stock["Shares"]
    return current_value

def original_value(stock):
    original_value = stock["Original Price"] * stock["Shares"]
    return original_value

def original_total():
    original_total_value = 0
    for stock in stocks:
        original_total_value += original_value(stock)
    return original_total_value

def total_value():
    total_value = 0
    for stock in stocks:
        total_value += value_stock(stock)
    return total_value

def total_profit():
    total_profit = 0
    for stock in stocks:
        total_profit += profit_stock(stock)
    return total_profit

def portfolio_allocate():
    for stock in stocks:
        print("=" * 35)
        print(f"{stock['Ticker']}\n")
        print(f"Value: ${value_stock(stock):.2f}\n")
        print(f"Allocation: {(value_stock(stock)/total_value()) * 100:.2f}%")
        print("=" * 35)


def profit_stock(stock):
    profit = value_stock(stock) - original_value(stock)
    return profit

def percent_gain(stock):
    percent_gain =  profit_stock(stock) / (stock["Original Price"] * stock["Shares"]) * 100 
    return percent_gain  

def sort_stocks(stocks):

    sorted_stocks = sorted(
        stocks, 
        key=percent_gain,
        reverse=True
    )

    print("=" * 9, "Best Performers", "=" * 9)
    
    for stock in sorted_stocks:
        print(
            f"{stock['Ticker']:6}  | "
            f"Gain:  {percent_gain(stock):7.2f}%  | "
            f"Profit: ${profit_stock(stock):8.2f}  | "
            f"Value: ${value_stock(stock):8.2f}  | "
        )
    print("=" * 35)

## RUNNING CODE       
def menu():
    print("=" * 10, "Portfolio Analyzer", "=" * 10)
    while True:
        try:
            choice = int(input( "Single Stock (1)\n"
                            "Whole Portfolio (2)\n"
                            "Portfolio Allocations (3)\n"
                            "Update Live Prices (4)\n"
                            "Add Stock (5)\n"
                            "Edit Stock (6)\n"
                            "Remove Stock (7)\n"
                            "Exit (8)\n"
                            "Choice:"
                            ))
        except ValueError:
            print("Please enter a number!")
            continue 
        if choice == 1:
            single_stock_analyze()
        elif choice == 2:
            portfolio_analyze()
            sort_stocks(stocks)
        elif choice == 3:
            portfolio_allocate()
        elif choice == 4:
            update_price()
        elif choice == 5:
            add_stock()
        elif choice == 6:
            edit_stock()
        elif choice == 7:
            remove_stock()
        elif choice == 8:
            print("Goodbye!")
            break
        else: 
            print("Please enter a valid number!")

stocks = load_portfolio()
menu()