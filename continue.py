#continue ile ilgili ornek ;
while True:
	s = raw_input("Bir sayi girininz : ")
	if s == "iptal":
		break
	if len(s) <= 3:
		continue
	print "en fazla uc haneli bir sayi giriniz "	