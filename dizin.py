import os 
import re

dizin = raw_input("Arama yapmak istediginiz dizini girin : ")

	for i in dizin :
		a = re.match(".*txt", i)
		if a :
			print a.group()
