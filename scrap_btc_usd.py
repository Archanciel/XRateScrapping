from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def cleanRate(rateStr):
    '''
    remove thousands divider from passed 
    rate string and return cleaned string
    '''
    return rateStr.replace(',','')
    
url = "https://uk.investing.com/currencies/streaming-forex-rates-majors"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
page = urlopen(req).read()

soup = BeautifulSoup(page)
#print(soup.prettify())

BTCUSD_CLASS='pid-21-'
BID='bid'
ASK='ask'
rateBidStr = soup.find('td',{'class':BTCUSD_CLASS + BID}).string
rateAskStr = soup.find('td',{'class':BTCUSD_CLASS + ASK}).string
rateBidStr = cleanRate(rateBidStr)
rateAskStr = cleanRate(rateAskStr)
print(rateBidStr)
print(rateAskStr)
rateAvg=(float(rateBidStr)+float(rateAskStr))/2
print(rateAvg)
