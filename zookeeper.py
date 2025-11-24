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
    """
    Represents a zookeeper that can feed animals
    and clean enclosures.
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Zookeeper")

    def feed_animal(self, animal):
        """
        Feeds assigned animal and returns its eaten
        """
        if animal is None:
            raise ValueError("The animal cannot be None")
        print(f"{self.name} feeds {animal.name}")
        return animal.eat()

    def clean_enclosure(self, enclosure):
        """
        Cleans enclosure to 100
        """
        if enclosure is None:
            raise ValueError("The enclosure cannot be None")
        print(f"{self.name} cleans the {enclosure.environment} enclosure")
        enclosure.clean()

    def perform_duties(self):
        """
        Returns a description of the zookeeper's duties.
        """
        return f"{self.name} is feeding animals and cleaning"