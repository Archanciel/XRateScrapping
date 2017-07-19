import quandl
from forex_python.converter import CurrencyRates
import datetime
import sys

def getBtcRateForDate(dateDDMMYYYY):
	'''
	Function intended for execution on android. But not possible for now since trying to install quandl aswell
	as forex_python fails !
	:param dateDDMMYYYY:
	:return:
	'''
	dateDDMMYYYY = dateDDMMYYYY.replace('-','.')
	dateComponents = dateDDMMYYYY.split('.')
	dateYYYY = int(dateComponents[2])
	dateMM = int(dateComponents[1])
	dateDD = int(dateComponents[0])

	dateObj = datetime.date(dateYYYY, dateMM, dateDD)

	dateStart = dateObj
	dateEnd = dateStart
	dataBtc = quandl.get(["BCHARTS/KRAKENUSD.4"], start_date=dateStart, end_date=dateEnd, returns="numpy")
	if dataBtc.size > 0:
		btcUsdClosePrice = dataBtc[0][1]
	else:
		statusMsg = "ERROR - BTC/USD close price not found for date {0} !".format(dateStart)
		print(statusMsg)
		sys.exit(1)

	cr = CurrencyRates()
	usdChfRate = cr.get_rate('USD', 'CHF', dateObj)

	return float(btcUsdClosePrice), float(usdChfRate)


if __name__ == '__main__':
	print("BTC/USD hist rate: %f USD/CHF hist rate: %f" % getBtcRateForDate('3.6.2017'))
	print(getBtcRateForDate('3-6-2017'))
