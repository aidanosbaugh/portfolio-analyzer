

def single_stock_analyze(stocks):
    ticker = input("What stock would you like to view?").upper()
    stock = find_stock(ticker, stocks)
    
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

def portfolio_analyze(stocks):
    origtotalval = original_total(stocks)
    totalval = total_value(stocks)
    totalprof = total_profit(stocks)
    portreturn = (total_profit(stocks)/original_total(stocks)) * 100
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
        
def find_stock(ticker, stocks):
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

def original_total(stocks):
    original_total_value = 0
    for stock in stocks:
        original_total_value += original_value(stock)
    return original_total_value

def total_value(stocks):
    total_value = 0
    for stock in stocks:
        total_value += value_stock(stock)
    return total_value

def total_profit(stocks):
    total_profit = 0
    for stock in stocks:
        total_profit += profit_stock(stock)
    return total_profit

def portfolio_allocate(stocks):
    for stock in stocks:
        print("=" * 35)
        print(f"{stock['Ticker']}\n")
        print(f"Value: ${value_stock(stock):.2f}\n")
        print(f"Allocation: {(value_stock(stock)/total_value(stocks)) * 100:.2f}%")
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
