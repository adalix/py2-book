#fonksiyonlar 

def tek():
	print ("Gridiginiz sayi bir tek sayidir.")

def cift():
	print ("Girdiginiz sayi bir cift sayidir.")

sayi = raw_input("Lutfen bir sayi giriniz : ")
if int(sayi) % 2 == 0 :
	cift()
else:
	tek()	

