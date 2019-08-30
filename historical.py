
import datetime
from yahoofinancials import YahooFinancials

shares = YahooFinancials("2318.HK")
data = shares.get_daily_dividend_data("2018-01-01", "2018-12-31")
print (data)