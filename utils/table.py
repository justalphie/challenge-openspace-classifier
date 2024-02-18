#Seat 
import random
class Seat:

    def __init__(self, occupant: str = "", free: bool = True):
        """   
        Initialize a Seat object.
        Parameters:
        - occupant (str): The name of the occupant of the seat (default is an empty string).
        - free (bool): Indicates whether the seat is free or occupied (default is True).
        """
        self.free = free
        self.occupant = occupant

    def __str__(self):
        return f"Seat is occupied by {self.occupant}"

    def set_occupant(self, name: str):
        """
        Set the occupant of the seat.
        Parameters:
        - name (str): The name of the occupant.  
        Raises:
        - Exception: If the seat is already occupied.
        """
        if self.free:
            self.occupant = name
            self.free = False
        else:
            raise Exception ("Look for another seat")

    def remove_occupant(self):
        """
        Remove the occupant from the seat.
        """
        if self.free == False:
            self.free = True
            self.occupant = ""

class Table():
    def __init__(self, capacity: int = 4):
        """
        Initialize a Table object.
        Parameters:
        - capacity (int): The maximum number of seats at the table (default is 4).
        """
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def __str__(self):
        return f"Table has {self.capacity} seats."

    def has_free_spot(self) -> bool:
        """
        Check if the table has any free spots.
        Returns:
        - bool: True if there is at least one free spot, False otherwise.
        """
        for s in self.seats:
            if s.free == True:
                return True
        return False

    def assign_seat(self, name:str):
        """
        Assign a seat to a person.
        Parameters:
        - name (str): The name of the person.
        Raises:
        - Exception: If there are no free spots at the table.
        """
        if self.has_free_spot() == True:
            for s in self.seats:
                if s.free == True:
                    s.set_occupant(name)
                    break
        else:
            raise Exception("Look for another table")

    def left_capacity(self) -> int:
        """
        Get the number of remaining free seats at the table.
        Returns:
        - int: The number of free seats.
        """
        free_seats = 0
        for s in self.seats:
            if s.free == True:
                free_seats += 1
        return free_seats
    