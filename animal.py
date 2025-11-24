'''
File: animal.py
Description: This python module represents an animal class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Base abstract class for all types of animals.
    Each animal has a name, species, age and dietary needs.
    Includes a range of methods such as storing health records
    and an enclosure assignment.
    """
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health_records = []
        self.__enclosure = None

    @abstractmethod
    def eat(self):
        """
        Returns animal eating
        """
        pass

    @abstractmethod
    def make_sound(self):
        """
        Returns animal making a sound
        """
        pass

    def sleep(self):
        """
        Returns animal sleeping
        """
        return f"{self.__name} is sleeping."

    def add_health_record(self, record):
        """
        Appends health record to animal's health_records
        """
        self.__health_records.append(record)

    def assign_enclosure(self, enclosure):
        """
        Assigns an enclosure to the animal
        """
        self.__enclosure = enclosure

    def view_health_records(self):
        return self.__health_records.copy()

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def dietary_needs(self):
        return self.__dietary_needs

    @property
    def enclosure(self):
        return self.__enclosure

