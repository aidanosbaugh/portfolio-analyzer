import csv_handler
import analysis
import price_api

stocks = csv_handler.load_portfolio()

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
            analysis.single_stock_analyze(stocks)
        elif choice == 2:
            analysis.portfolio_analyze(stocks)
            analysis.sort_stocks(stocks)
        elif choice == 3:
            analysis.portfolio_allocate(stocks)
        elif choice == 4:
            price_api.update_price(stocks)
        elif choice == 5:
            csv_handler.add_stock(stocks)
        elif choice == 6:
            csv_handler.edit_stock(stocks)
        elif choice == 7:
            csv_handler.remove_stock(stocks)
        elif choice == 8:
            print("Goodbye!")
            break
        else: 
            print("Please enter a valid number!")

menu()