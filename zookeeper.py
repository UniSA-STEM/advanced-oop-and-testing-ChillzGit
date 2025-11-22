'''
File: zookeeper.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Zookeeper")

    def feed_animal(self, animal):
        if animal is None:
            raise ValueError("The animal cannot be None")
        print(f"{self.name} feeds {animal.name}")
        return animal.eat()

    def clean_enclosure(self, enclosure):
        if enclosure is None:
            raise ValueError("The enclosure cannot be None")
        print(f"{self.name} cleans the {enclosure.environment} enclosure")
        enclosure.clean()

    def perform_duties(self):
        return f"{self.name} is feeding animals and cleaning"