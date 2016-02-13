#!/usr/bin/env python
# _*_ coding: utf -8 _*_

class Oyun:
	def __init__(self):
		self.enerji = 50
		self.para = 100
		self.fabrika = 4
		self.isci = 10
	def goster(self):
		print "enerji:", self.enerji 
		print "para:", self.para
		print "fabrika:", self.fabrika 
		print "isci:", self.isci 
class Oyuncu(Oyun):
	def __init__(self):
		Oyun.__init__(self)


	def fabrikakur(self, miktar):
		if self.enerji > 3 and self.para > 10 :
			self.fabrika = miktar + self.fabrika
			self.enerji = self.enerji -3
			self.para = self.para - 10
			print miktar , "adet fabrika kurdunuz! Tebrikler !!!"

		else :
			print "yeni fabrika kuramazsininz \
			yeteri sayida enerji ve paraniz yok !!!"

oyuncu = Oyuncu()


class Dusman(Oyun):
	def __init__(self):
		Oyun.__init__(self)
		self.ego = 0

	def goster(self):
		Oyun.goster(self)
		print "ego :", self.ego	
	def fabrikayik(self,miktar):
		oyuncu.fabrika = oyuncu.fabrika - miktar
		self.ego = self.ego + 2
		print "Tebrikler.Oyuncunun", miktar, \
		"adet fabrikasini yiktiniz !!!"
		print "egonuz da buyudu!!!"


dsman = Dusman()					

