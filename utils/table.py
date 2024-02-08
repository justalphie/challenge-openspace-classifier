#Seat 
class Seat:
    def __init__(self, occupant = "", free = True):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            return f"{name} is seated"
        else:
            return "Look for another seat"

    def remove_occupant(self):
        
        if self.free == False:
            self.free = True
            self.occupant = ""
            return f"The student was removed, the seat is free now"
    

class Table:
    def __init__(capacity:int, seats:list):
        self.capacity = capacity
        self.seats = []

    def has_free_spot(self):
        for s in self.seats:
            if s.free == True:
                return True
        return False

    def assign_seat(self, name):
        #places someone at the table

    def left_capacity(self):
        counter = 0
        for s in self.seats:
            if s.free == True:
                counter+=1

        return counter


