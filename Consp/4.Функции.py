-------------------------------------
def get_vat(modding):
	mama_cline = modding / 100 * 22           #функция вычесления НДС
	return round(mama_cline,2)

print("{} %" .format(get_vat(100)))               #вызов и вывод функции НДС
-------------------------------------
def get_vat(modding):    
	try:                                          #попробую
		mama_cline = modding / 100 * 22           #функция вычесления НДС
		return round(mama_cline,2)
	except (TypeError, ValueError):               #если получится 'TypeError' то:
		print("Не могу посчитать вводимые данные")

result = get_vat(50)
print(result)
------------------------------------
