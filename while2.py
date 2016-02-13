'''
n = input("kaca kadar sayalim: ")
for i in range(1,n+1):
	print i 

'''
kitaplar = [
	[45623, 'python', 'mustafa', 'baser', 23],
	[99878, 'linux ag servisleri', 'mustafa', 'baser', 26],
	[98938, 'isletim sistemleri', 'ali', 'saatci', 23],
	[98947, 'php ve ajax', 'haydar', 'tuna', 25]
	]

while True :
	yazarSoyad = raw_input("aramak istediginiz yazarin soyadini yazin: ")
	if yazarSoyad not in ['c','C']:
		found = False;
		for k in kitaplar:
			if yazarSoyad == k[3]:
				print k[3], "soyadli yazarin eserleri:",k[1]
				found = True;
				print "-"*30
		if not found:
			print yazarSoyad, " soyad bilgisi sistemde bulunamadi ."		
	else:		
		break		