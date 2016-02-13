import os
import re

a = raw_input("Aramak istediginiz dizini yazin :")
b = raw_input("Aramak istediginiz uzantiyi girin : ")

print "Aramak istediginiz dizin : %s  uzanti ise : %s" %(a,b)

x = os.listdir(a)

for i in x:
	c = re.match(b, i)
	if c :
		print c.group() 
