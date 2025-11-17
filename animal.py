'''
File: animal.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__health_records = []
        self.__enclosure = None

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        return f"{self.__name} is sleeping."

    def add_health_record(self, record):
        self.__health_records.append(record)

    def assign_enclosure(self, enclosure):
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

