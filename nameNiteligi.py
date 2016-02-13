#name niteligine bakiyoruz (hangi isletim sistemini kullandigimiz ornek)

import os

if os.name == "posix" :
	a = raw_input("linus torvlads'a mesajinizi yazin: ")
	print "Merhaba linux kullanicisi"

if os.name == "nt" :
	a = raw_input("bill gates'e mesajinizi yazin: ")
	print "Merhaba windows kullanicisi!"


if os.name == "mac" :
	a = raw_input("steve jobs'a mesajinizi yazin: ")
	print "Merhaba Mac kullanicisi"	
