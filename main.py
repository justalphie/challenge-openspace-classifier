import sys
sys.path.append("utils")
import table
from table import Seat
from table import Table
import openspace
from openspace import Openspace
import csv

with open("new_colleagues.csv", "r") as f:
    reader = csv.reader(f)
    list_of_people = ["".join(l) for l in list(reader)]

print(list_of_people)

o = Openspace()

o.organize(list_of_people)
o.display()
o.store_occupants_in_excel("Plan")


