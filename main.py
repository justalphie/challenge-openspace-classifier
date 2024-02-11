import sys
sys.path.append("utils")
import table
from table import Seat
from table import Table
import openspace
from openspace import Openspace
import csv
import json

with open("config.json", "r") as f:
    config = json.load(f)



with open(config["file_path"], "r") as f:
    reader = csv.reader(f)
    list_of_people = ["".join(l) for l in list(reader)]

print(list_of_people)

o = Openspace(config["table_number"], config["table_capacity"])

organized = False
while organized == False:
    try:
        o.organize(list_of_people)
        organized = True
    except:
        o.empty_all_tables()
        agree = input("Not enough tables. Would you like to add more? Type (yes/no): ").lower()
        if agree == "yes":
            number_tables_to_add = int(input("How many tables would you like to add? "))
            added_tables_capacity = int(input("How many seats do new tables have? "))
            o.add_table(number_tables_to_add, added_tables_capacity)



o.display()
o.store_occupants_in_excel("Plan")


