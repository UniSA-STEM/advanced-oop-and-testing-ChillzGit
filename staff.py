'''
File: staff.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    """
    Represents a Staff that can be assigned to animals
    and enclosures. Staff have a name, ID and role.
    """
    def __init__(self, name, staff_id, role):
        if not name.strip():
            raise ValueError("Staff name cannot be an empty string.")
        if not isinstance(staff_id, int) or staff_id <= 0:
            raise ValueError("Staff ID must be a positive integer.")
        if not role.strip():
            raise ValueError("Staff role cannot be an empty string.")

        self.__name = name
        self.__staff_id = staff_id
        self.__role = role
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def staff_id(self):
        return self.__staff_id

    @property
    def role(self):
        return self.__role

    def assign_animal(self, animal):
        """
        Assigns an animal to this Staff
        """
        if animal is None:
            raise ValueError("Animal cannot be None.")
        self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        """
        Assigns an enclosure to this Staff
        """
        if enclosure is None:
            raise ValueError("Enclosure cannot be None.")
        self.__assigned_enclosures.append(enclosure)

    @abstractmethod
    def perform_duties(self):
        """
        Returns a description of the staff member's duties
        """
        pass


