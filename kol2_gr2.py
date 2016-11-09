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
	dziennik = diary()

	dziennik.dodaj_studenta(student('Jan', 'Kowalski'))

	(dziennik.stud(0)).dodaj_ocena_spr(5)
	(dziennik.stud(0)).dodaj_ocena_spr(4)
	(dziennik.stud(0)).dodaj_ocena_inna(4)

	print(dziennik.studenci[0].srednia_ogolna())
	print(dziennik.studenci[0].srednia_spr())



if __name__ == "__main__":
	main()
