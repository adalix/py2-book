

Toplama = " (1) toplama islemi icin "
Cikarma = " (2) cikarma islemi icin "
Carpma = " (3) carpma islemi icin "
Bolme = " (4) bolme islemi icin "

print "toplama"
print "cikarma"
print "carpma"
print "bolme"

soru = raw_input ("yapacaginin islemi seciniz : ")

if soru == "1" :
	sayi1 = input ("toplamak istediginiz ilk sayiyi girin : ")
	print sayi1

	sayi2 = input ("toplamak istediginiz ikinci sayiyi girin : ")

	print sayi1 ,"+",sayi2,"=",sayi1+sayi2	

if soru == "2" :
	sayi1 = input ("cikarma islemi yapmak istedigin sayiyi girin : ")
	print sayi1 	

	sayi2 = input ("cikarma islemi yapmak istediginiz ikinci sayi : ")
	print sayi1,"-",sayi2,"=",sayi1-sayi2


if soru == "3" :
	sayi1 = input ("carpma islemi icin birinci sayiyi girin : ")
	print sayi1

	sayi2 = input ("ikinci sayiyi girin : ")

	print sayi1,"*",sayi2,"=",sayi1*sayi2

if soru == "4"	:
	sayi1 = input ("bolme islemi yapmak istediginiz ilk sayiyi girin : ")
	print sayi1
	sayi2 = input ("ikinci sayiyi girin : ")
	print sayi1,"/",sayi2,"=",sayi1/sa