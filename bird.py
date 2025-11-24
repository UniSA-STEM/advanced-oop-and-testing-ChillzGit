'''
File: bird.py
Description: This python module represents a bird class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    """
    Represents a bird in the zoo
    """
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        """
        Returns a string describing what the bird eats
        """
        return f"{self.name} the {self.species} eats {self.dietary_needs}"

    def make_sound(self):
        """
        Returns a string describing the sound a bird makes
        """
        return f"{self.name} makes a bird sound"