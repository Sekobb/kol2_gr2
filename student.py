class student:

	def __init__(self, imie, nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko
		self.oceny_spr = []
		self.oceny_inne = []
		self.obecnosci = []

	def dodaj_ocena_spr(self, ocena):
		self.oceny_spr.append(ocena)

	def dodaj_ocena_inna(self, ocena):
		self.oceny_inne.append(ocena)

	def dodaj_obecnosc(self, obecnosc):
		self.obecnosci.append(obecnosc)

	def srednia_ogolna(self):
		suma = 0
		ilosc = 0

		for i in self.oceny_spr:
			suma += i
			ilosc += 1

		for i in self.oceny_inne:
			suma += i
			ilosc += 1

		return suma/ilosc
		

	def srednia_spr(self):
		suma = 0
		ilosc = 0

		for i in self.oceny_spr:
			suma += i
			ilosc += 1

		return suma/ilosc

	def suma_obecnosci(self):
		suma = 0
		ilosc = 0

		for i in self.oceny_spr:
			suma += i
			ilosc += 1

		return suma/ilosc
