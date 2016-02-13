#while ve break ile ilgili ornekler ...

parola = "parola"

while True:
	kullanici_adi = raw_input("Kullanici Adinizi Giriniz : ")
	soru2 = raw_input ("Parolanizi Giriniz : ")
	
	if soru2 == "parola" :
		print "Hosgeldin %s " %(kullanici_adi)
		break 
	else :
		print "Kullanici adi veya parolaniz yanlis !!!"
		print "Lutfen tekrar deneyiniz "	


		