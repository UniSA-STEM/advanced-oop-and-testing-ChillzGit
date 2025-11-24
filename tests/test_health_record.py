'''
File: test_health_record.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from health_record import HealthRecord

def test_health_record_fields():
    hr = HealthRecord("Cut", "23-11-2025", "L", "Bandage", "active")
    assert hr.description == "Cut"
    assert hr.date == "23-11-2025"
    assert hr.severity == "L"
    assert hr.treatment_plan == "Bandage"
    assert hr.status == "active"

def test_mark_resolved():
    hr = HealthRecord("Cut", "23-11-2025", "L", "Bandage", "active")
    hr.mark_resolved()
    assert hr.status == "resolved"

