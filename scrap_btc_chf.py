from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def cleanRate(rateStr):
    '''
    remove thousands divider from passed 
    rate string and return cleaned string
    '''
    rateStr = rateStr.replace('.','')
    return rateStr.replace(',','.')
    
url = "https://fr.investing.com/currencies/btc-chf"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
page = urlopen(req).read()

soup = BeautifulSoup(page)
#print(soup.prettify())

rateStr = soup.find(id='last_last').string
rateStr = cleanRate(rateStr)
print(rateStr)


