from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def cleanRate(rateStr):
    '''
    remove thousands divider from passed 
    rate string and return cleaned string
    '''
    rateStr = rateStr.replace('.','')
    return rateStr.replace(',','.')


def getBTCRate(targetCur):
    '''
    Scrap the bitcoin rate in the passed currency
    :param targetCur: currency in which the bitcoin rate is fetched
    :return: bitcoin rate in targetCur
    '''
    url = "https://fr.investing.com/currencies/btc-" + targetCur.lower()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page,"lxml")
    # print(soup.prettify())
    rateStr = soup.find(id='last_last').string
    rateStr = cleanRate(rateStr)
    return rateStr

if __name__ == "__main__":
    print("BTC/CHF: " + getBTCRate("CHF"))
    print("BTC/EUR: " + getBTCRate("EUR"))
    print("BTC/USD: " + getBTCRate("USD"))


