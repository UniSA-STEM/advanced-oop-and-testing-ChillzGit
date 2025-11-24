'''
File: test_animal.py
Description: This python script runs a series of tests that tests the animal class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from health_record import HealthRecord

def test_animal_sleep():
    m = Mammal("John", "Lion", 5, "meat")
    assert m.sleep() == "John is sleeping."

def test_add_health_record():
    hr = HealthRecord("Cut", "24-11-2025", "L", "Bandage", "active")
    a = Reptile("Beth", "Snake", 3, "rats")
    a.add_health_record(hr)
    assert len(a.view_health_records()) == 1
    assert a.view_health_records()[0].description == "Cut"

def test_make_sounds():
    assert Bird("Jack", "Magpie", 2, "seeds").make_sound() == "Jack makes a bird sound"
    assert Mammal("Ryan", "Lion", 5, "meat").make_sound() == "Ryan makes a mammal sound"
    assert Reptile("Ross", "Snake", 3, "rats").make_sound() == "Ross makes a reptile sound"
