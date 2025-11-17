'''
File: health_record.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    def __init__(self, description, date, severity, treatment_plan, status):
        if not description.strip():
            raise ValueError('Description cannot be empty.')
        if severity not in ["L", "M", "H"]:
            raise ValueError('Severity must be one of "L", "M", "H".')
        if status not in ["active", "resolved"]:
            raise ValueError('Status must be one of "active", "resolved".')

        self.__description = description
        self.__date = date
        self.__severity = severity
        self.__treatment_plan = treatment_plan
        self.__status = status

    # Getters
    @property
    def description(self):
        return self.__description

    @property
    def date(self):
        return self.__date

    @property
    def severity(self):
        return self.__severity

    @property
    def treatment_plan(self):
        return self.__treatment_plan

    @property
    def status(self):
        return self.__status

    # Mark resolved
    def mark_resolved(self):
        self.__status = "resolved"

    # String conversion method
    def __str__(self):
        return (f"Health Record: {self.__description} | Date: {self.__date} | "
                f"Severity: {self.__severity} | Treatment Plan: {self.__treatment_plan} | "
                f"Status: {self.__status} ")

