'''
File: test_enclosure.py
Description: This python script tests the enclosure class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from enclosure import Enclosure
from mammal import Mammal

def test_add_valid_animals():
    lion = Mammal("John", "Lion", 7, "meat")
    enc = Enclosure(200, "savannah", 90, ["Lion"], "savannah")
    added = enc.add_animal(lion)
    assert added is True
    assert enc.list_animals() == ["John"]

def test_add_invalid_animals():
    bear = Mammal("Zoe", "Bear", 4, "berries")
    enc = Enclosure(200, "savannah", 90, ["Lion"], "savannah")
    added = enc.add_animal(bear)
    assert added is False
    assert enc.list_animals() == []

def test_clean_enclosure():
    enc = Enclosure(200, "savannah", 90, ["Lion"], "savannah")
    enc.clean()
    assert enc.cleanliness == 100

