from student import *

class diary(object):

	def __init__(self):
		self.studenci = []

	def dodaj_studenta(self, student):
		self.studenci.append(student)

	def __add__(self, student):
		self.studenci.append(student)

	def stud(self, i):
		return self.studenci[i]
