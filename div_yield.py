
from yahoofinancials import YahooFinancials

def div_yield_percentage(dividend, spot_price):
    div_yield = str(round(dividend/spot_price*100, 2)) + "%"
    return div_yield

shares = YahooFinancials(["1299.HK", "2318.HK"])
dividend_data = shares.get_daily_dividend_data("2018-01-01", "2018-12-31")
price_data = shares.get_current_price()
for ins, dividends in dividend_data.items():
    total_div = 0
    spot_price = price_data[ins]
    for dividend in dividends:
        total_div = total_div + dividend["amount"]
    div_yield = div_yield_percentage(total_div, spot_price)
    print ("Dividend yield for %s is %s" % (ins, div_yield))

# div = 0.848 + 0.095
# spot = 84.25
# div_yield = div_yield_percentage(div, spot)
# print ("Dividend yield of 1299.HK = %s " % div_yield )

# div = 1.284144
# spot = 93.8
# div_yield = div_yield_percentage(div, spot)
# print ("Dividend yield of 2318.HK = %s " % div_yield )

