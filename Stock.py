__author__ = 'ChristopherChan'
import ystockquote
from pprint import pprint
import bokeh
from bokeh.plotting import figure, output_file, show
import json
import datetime
import time
from yahoo_finance import Share

'''
    Uses ystockquote API. Pretty easy to use.
    prints graph depending on three inputs: stock name, start date, end date
'''
def yStockQuoteExample(stock,startDate,endDate):
    pprint(ystockquote.get_historical_prices(stock, startDate, endDate))
    stockQuote = ystockquote.get_historical_prices(stock, startDate, endDate)
    dates = []
    dailyClose = []
    for key in stockQuote.keys():
        year =  int(key[0:4])
        month =  int(key[5:7])
        day =  int(key[8:11])
        dates.append(datetime.date(year,month,day))
        dailyClose.append(float(stockQuote.get(key).get("Close")))
    dates= sorted(dates)

    output_file("lines.html", title="line plot example")

    p = figure(title=stock, x_axis_type="datetime")
    p.line(dates, dailyClose, legend=stock,  x_axis_label='dates', y_axis_label='dailyClose')

    show(p)


'''
    Uses a different API. yahoo_finance. Both are pretty good.
'''
def yahooFinanceExample(stock):
    yahoo = Share(stock)
    print yahoo.get_open()


def main():
    yStockQuoteExample("msft",'2014-10-03','2014-12-08')
    yStockQuoteExample("msft",'2014-10-03','2014-12-08')

main()