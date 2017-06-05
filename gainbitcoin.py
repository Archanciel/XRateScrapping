import xlwings as xw
import scrapBTCRate as sc

@xw.func
def getBTCRateIn(cur):
	return sc.getBTCRate(cur)

