# sectigimiz semtlere gore kira araliklari veren program

print("UYGUN OLAN SEMTLERIN LISTESI : ")

print "Basaksehir"
print "Bebek"
print "Cihangir"
print "Tophane"
print "Kirsehir"
print "Kaman"


secenek1 = "(1) Basaksehir"
secenek2 = "(2) Bebek"
secenek3 = "(3) Cihangir"
secenek4 = "(4) Tophane"
secenek5 = "(5) Kirsehir"
secenek6 = "(6) Kaman"



sec = raw_input("Listeden bir semt ismi secin : ")
if sec == "1" :
	print("Basaksehir semtinde fiyat araligi 900 - 1200")
elif sec == "2" :
	print ("Bebek semtinde fiyat araligi 1400-1800")
elif sec == "3" :
	print ("Cihangir semtinde fiyat araligi 2500-3000")
elif sec == "4" :
	print ("Tophane semtte fiyat araligi 2500-3000")
elif sec == "5" :
	print ("Kirsehir semtinde fiyat araligi 3500-4000")
elif sec == "6" :
	print ("Kaman semtinde fiyat araligi 6500-7000")

