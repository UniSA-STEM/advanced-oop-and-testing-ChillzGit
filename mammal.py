'''
File: mammal.py
Description: This python module represents a mammal in the zoo
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Mammal(Animal):
    """
    Represents a mammal in the zoo
    """
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        """
        Returns a string describing what the mammal eats
        """
        return f"{self.name} the {self.species} is eating {self.dietary_needs}."

    def make_sound(self):
        """
        Returns a string describing the sound a mammal makes
        """
        return f"{self.name} makes a mammal sound"
