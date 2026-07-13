import yfinance as yf
import datetime as dt
from csv_handler import save_portfolio


def get_price(ticker):
   try:
        stock = yf.Ticker(ticker)
        return (stock.fast_info["lastPrice"])
   except Exception:
       return None

def update_price(stocks):
    print("Updating Prices ... ")
    for stock in stocks: 
        price = get_price(stock["Ticker"])
        if price is None:
            print(stock["Ticker"], "x failed")
            continue
        stock["Price"] = price
        print(f"{stock['Ticker']:6} ✓ {price:.2f}")
    save_portfolio(stocks)
    print("Portfolio succesfully updated")
    print(f"at {dt.datetime.today()}")
   
