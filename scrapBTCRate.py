from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def cleanRate(rateStr):
    '''
    remove thousands divider from passed 
    rate string and return cleaned string
    '''
    return rateStr.replace(',','')


def getBTCRate(targetCur):
    '''
    Scrap the bitcoin rate in the passed currency
    Usage: getBTCRate("CHF"), getBTCRate("USD")
    :param targetCur: currency in which the bitcoin rate is fetched
    :return: bitcoin rate in targetCur
    '''
    url = "http://markets.businessinsider.com/currencies/realtime-chart/btc-" + targetCur.lower()
    #req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req = Request(url)
    page = urlopen(req).read()
    soup = BeautifulSoup(page,"lxml")
    # print(soup.prettify())
    rateStr = soup.find("span",{'class':'push-data price'}).string
    rateStr = cleanRate(rateStr)
    return rateStr

if __name__ == "__main__":
    print("BTC/CHF: " + getBTCRate("BTC","CHF"))
    print("BTC/EUR: " + getBTCRate("BTC","EUR"))
    print("BTC/USD: " + getBTCRate("BTC","USD"))


