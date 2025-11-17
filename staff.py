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
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @abstractmethod
    def feed_animals(self):
        pass

    @abstractmethod
    def cleaning_enclosures(self):
        pass

    @abstractmethod
    def perform_health_checks(self):
        pass

