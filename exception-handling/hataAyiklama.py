#hata ayiklama ile ilgili


# bu prgoramin ilk hali. Kullanici burada sayi yerine kadarkter girebiliyor
'''sayi = int(raw_input("bir sayi giriniz: "))

print "girdiginiz sayi", sayi

print "tesekkurler ,hoscakalin!!! " '''


# buda programin try except ile yazilmis hali 

try :
	sayi = int(raw_input("bir sayi giriniz: "))
	print "girdiginiz sayi", sayi

except ValueError:
	print "lutfen harf degil, sayi giriniz!!! "
	print "tasakkurler , hoscakalin!"	