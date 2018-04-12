#Import Libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#Specify the URL
##quote_page = ['http://www.bloomberg.com/quote/SPX',
##              'http://www.bloomberg.com/quote/CCMP:IND']
quote_page = ['http://www.stocktwits.com/symbol/SPX',
              'http://www.stocktwits.com/symbol/CCMP']

data = []

for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
    name_box = soup.find('div', attrs={'class': 'ticker-container'})
    ticker_box = name_box.find('div', attrs={'class': 'data-stock-price'})
    print ticker_box
    print name_box
    ##name = name_box.text.strip() # strip() is used to remove starting and trailing
    ##print name
    
    # get the index price
    price_box = soup.find('div', attrs={'class':'data-symbol'})
    print 'Price: ' + price_box
    #price = price_box.text
    #print (name + ': ' + price)

    # save the data in tuple
    #data.append((name, price))
	
# open a csv file with append, so old data will not be erased
##with open('index.csv', 'a') as csv_file:
##	writer = csv.writer(csv_file)
##	for name, price in data:
##	    writer.writerow([name, price, datetime.now()])
