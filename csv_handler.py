import csv
import analysis

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

def save_portfolio(stocks):
    fieldnames = ["Ticker", "Price", "Original Price", "Shares"]
    with open("portfolio.csv", mode="w", newline="", encoding="utf-8") as file:
        saver = csv.DictWriter(file, fieldnames=fieldnames)
        saver.writeheader()
        for stock in stocks:
            saver.writerow(stock)
        
def add_stock(stocks):
    ticker = input("Ticker: ").upper()

    if analysis.find_stock(ticker, stocks):
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
            save_portfolio(stocks)
            print("Stock Added")
    else: 
        print("Cancelled")

def edit_stock(stocks):
    ticker = input("What stock would you like to edit?").upper()

    stock = analysis.find_stock(ticker, stocks)

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
        save_portfolio(stocks)

def remove_stock(stocks):
    ticker = input("What stock woudl you like to remove?").upper()

    stock = analysis.find_stock(ticker, stocks)

    if stock is None:
        print("Stock not found")
        return
    
    delete_confirm = input(f"Are you sure you would like to remove {ticker}? (Y/N)").upper()
    if delete_confirm == "Y":
        stocks.remove(stock)
        save_portfolio(stocks)
        print("Stock Removed")
    elif delete_confirm == "N":
        print(f"=== Deletion Cancelled ===\n", "... Returning to menu ... \n", sep="")
        return
    else:
        print("Please enter Y/N")
