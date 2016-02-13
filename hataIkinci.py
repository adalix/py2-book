#hata ayiklama ikinci ornek

#kullanici sifir girdiginde alinan hatayi duzeltme


'''ilk = int(raw_input("bolem islemi icin sayi girin: "))
ikinci = int(raw_input("ikinci sayiyi girin: "))
sonuc = float(ilk) / ikinci

print sonuc'''

try:
	ilk = int(raw_input("bolme islemi icin sayi girin: "))
	ikinci = int(raw_input("bolme islemi icin ikinci sayiyi girin: "))

	sonuc = float(ilk) / ikinci 
	print sonuc
except ZeroDivisionError:
	print "lutfen sayiyi sifira bolmeye calismayin"
except ValueError:
	print "lutfen harf degil, sayi giriniz !!!"


