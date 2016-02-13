class kayit:

	def kayit_ekle(self, ad, soyad, tel):
		self.ad = ad 
		self.soyad = soyad 
		self.tel = tel

		print "Eklemek istediginiz kayit bilgileri ad:%s , soyad:%s, tel:%s" %(self.ad, self.soyad, self.tel)

kayit1 = kayit()
kayit2 = kayit()

kayit1.kayit_ekle("tolga","gumus",2232123123)
kayit2.kayit_ekle("dilek", "gumus", 1029381)


