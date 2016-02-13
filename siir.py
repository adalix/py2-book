dosya = open("siir.txt","w")

dosya.write("Butun gunesler batmadan,\nBi turku daha soyleyeyim\
 bu yerde \n\t\t\t\t --Orhan Veli--")
	
dosya.close()	

dosya =open("siir.txt","r")

print dosya.read()