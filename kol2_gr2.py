#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surnames
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from diary import *

def main():

	przedmioty = ['matematyka', 'fizyka', 'cpp']
	studenci = ['Jan Kowalski', 'Wojciech Nowak', 'Jerzy Gzik']

	dziennik = diary(przedmioty, studenci)

	dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 4)
	dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 5)
	dziennik.dodaj('fizyka', 'Wojciech Nowak', 'spr', 5)
	dziennik.dodaj('fizyka', 'Wojciech Nowak', 'inne', 2)

	dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 1)
	dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)
	dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)
	dziennik.dodaj('matematyka', 'Jan Kowalski', 'ob', 0)

	print dziennik.spr_srednia('fizyka', 'Wojciech Nowak')
	print dziennik.srednia('fizyka', 'Wojciech Nowak')
	print dziennik.obecnosc('matematyka', 'Jan Kowalski')


if __name__ == "__main__":
	main()

