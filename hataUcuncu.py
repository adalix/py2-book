#hata ayiklama pass ile ilgili ornek

try:

	ilk = int(raw_input("bolme islemi icin bir sayi girin: "))
	ikinci = int(raw_input("bolme islemi icin ikinci sayiyi girin: "))
	sonuc = float(ilk) / ikinci
	print sonuc
except(ZeroDivisionError,ValueError):
	pass	