'''
File: reptile.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        super().__init__(name, species, age, dietary_needs)

    def eat(self):
        return f"{self.name} the {self.species} eats {self.dietary_needs}"

    def make_sound(self):
        return f"{self.name} makes a reptile sound"