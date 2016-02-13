#kayitekleme parametreleri isimleriyle yazdirma

'''def fonk():
	a = 5
	return a

print "a'nin degeri: %s" %fonk()	'''


def sayi_isle():
	sor = input("bir sayi giriniz: ")
	return sor

sayi = sayi_isle()

print "Gridiginiz sayi: %s" %sayi	

if sayi % 2 == 0 :
	print "girdiginiz sayi cifttir"

else:
	print "Girdiginiz sayi tektir"

print "girdigininz sayinin karesi: %s" %sayi ** 2
print "girdiginiz sayinin kupu: %s" %sayi ** 3