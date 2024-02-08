from table.py import Table
from table.py import Seat
import random

class Openspace:
    def __init__(self, tables: list, number_of_tables = int):
        self.tables = tables
        self.number_of_tables = number_of_tables
    
    def organize(self, names):
        for name in names:
            table.assign_seat(name)
            return 

    def display (self):
        print (occupants)

    def store(self, filename):
        with open #to be continued 




