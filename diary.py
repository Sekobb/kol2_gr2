from __future__ import division

class diary(object):

	def __init__(self, przedmioty, studenci):
		self.baza = {}
		for p in przedmioty:
			self.baza[p] = {}
			for s in studenci:
				self.baza[p][s] = {}
				self.baza[p][s]['spr'] = []
				self.baza[p][s]['inne'] = []
				self.baza[p][s]['ob'] = []


	def dodaj(self, przedmiot, student, status, ocena):
		self.baza[przedmiot][student][status].append(ocena)

	def srednia(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['spr']) + sum(self.baza[przedmiot][student]['inne'])
		ilosc = len(self.baza[przedmiot][student]['spr']) + len(self.baza[przedmiot][student]['inne'])
		return round(suma/ilosc, 2)

	def spr_srednia(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['spr'])
		ilosc = len(self.baza[przedmiot][student]['spr'])
		return round(suma/ilosc, 2)

	def obecnosc(self, przedmiot, student):
		suma = sum(self.baza[przedmiot][student]['ob'])
		ilosc = len(self.baza[przedmiot][student]['ob'])
		return str(round((suma/ilosc) * 100, 2)) + '%'

