'''
File: test_staff.py
Description: A python script that tests the staff class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from staff import Staff

class TestStaff(Staff):
    def perform_duties(self):
        return "working"

def test_staff_initialisation():
    staff = TestStaff("Patrick", 123, "Tester")
    assert staff.name == "Patrick"
    assert staff.staff_id == 123
    assert staff.role == "Tester"

def test_assign_animal():
    staff = TestStaff("Patrick", 123, "Tester")
    test_animal = "Lion"
    staff.assign_animal(test_animal)
    assert True