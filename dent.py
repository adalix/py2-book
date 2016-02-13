import re
import urllib
import os 


kelime = raw_input("google.com 'da aramak \
	istediginiz kelime: ")

adres = urllib.urlopen("http://www.google.com.tr")

kar_dizisi = " ".join(adres)

nesne = re.search(kelime,kar_dizisi)

if nesne :
	print "kelime bulundu: %s"%nesne.group()
else :
	print "kelime bulunamadi! :%s"%kelime


tg = open("/Users/user/Desktop/aranan_kelime.txt", "a")

tg.write("Aranilan kelime : %s\n" %kelime)

tg.close()


	

	
