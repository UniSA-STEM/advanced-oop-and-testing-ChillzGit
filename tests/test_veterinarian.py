'''
File: test_veterinarian.py
Description: A python script that tests the veterinarian class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from veterinarian import Veterinarian
from mammal import Mammal

def test_vet_duties():
    vet = Veterinarian("Eden", 101)
    assert vet.perform_duties() == "Eden is doing health checks"

def test_conduct_health_check():
    vet = Veterinarian("Eden", 101)
    lion = Mammal("John", "Lion", 7, "meat")

    record = vet.conduct_health_check(
        lion,
        description="Scratch",
        severity="M",
        treatment_plan="Rest"
    )

    records = lion.view_health_records()
    assert len(records) == 1
    assert records[0].description == "Scratch"
    assert records[0].severity == "M"
    assert records[0].treatment_plan == "Rest"
