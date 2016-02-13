def topen(dosyaAdi, mod = "r"):
	if dosyaAdi.strip() == "":
		print "HATA: Dosya Adi Bos Birakilamaz";
	elif mod.strip() == "r" or mod.strip() == "R":
		print "%s OKUMAK icin acildi" %dosyaAdi
	elif mod.strip() == "w" or mod.strip() == "W":
		print "%s YAZMAK icin acildi" %dosyaAdi
	elif mod.strip() == "a" or mod.strip() == "A":
		print "%s EKLEMEK icin acildi" %dosyaAdi
	else:
		print "HATA: r,w,a dan farkli girilmistir."


topen("deneme","W")