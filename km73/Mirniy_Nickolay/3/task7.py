N = int(input('Количество минут после 00.00 : '))

H = N//60
M = N%60


print('Количество пройденных часов :',H,
	'\nКоличество пройденных минут : ',M)