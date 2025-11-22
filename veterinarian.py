'''
File: veterinarian.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff
from health_record import HealthRecord
from datetime import date

class Veterinarian(Staff):
    def  __init__(self, name, staff_id):
        super().__init__(name, staff_id, "Veterinarian")

    def conduct_health_check(self, animal, description, severity, treatment_plan):
        if animal is None:
            raise ValueError("The animal cannot be None")

        record = HealthRecord(
            description=description,
            date=date.today(),
            severity=severity,
            treatment_plan=treatment_plan,
            status="active"
        )

        animal.add_health_record(record)
        print(f"{self.name} checked {animal.name}")
        return record

    def perform_duties(self):
        return f"{self.name} is doing health checks"
