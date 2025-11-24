'''
File: main.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

"""
This main.py file implements all of the classes
and tests its functionality. 
"""

# Import classes
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian

# Create animals
john = Mammal("John", "Lion", 7, "meat")
beth = Reptile("Beth", "Snake", 3, "rats")
kyle = Bird("Kyle", "Magpie", 2, "seeds")

# Create enclosure
savannah = Enclosure(size=200,
                     environmental_type="savannah",
                     cleanliness=90,
                     allowed_species=["Lion", "Cheetah", "Tiger"],
                     allowed_environment="savannah")

# Adding animals
print("-----Adding Animals-----")
print(savannah.add_animal(john))    # Result = True
print(savannah.add_animal(kyle))    # Result = False
print()

# Check enclosure status
print("-----Checking Enclosure Status-----")
print(savannah.report_status())     # Result = Status report
print()

# Test make_sound method
print("-----Checking make_sound Method-----")
print(john.make_sound())            # Result = Mammal sound
print(kyle.make_sound())            # Result = Bird sound
print()

# Test eat method
print("-----Checking eat Method-----")
print(beth.eat())
print(beth.eat())                   # Result = Name, species and what they're eating
print(john.eat())                   # Result = Name, species and what they're eating
print()

# Test sleep method
print("-----Checking sleep Method-----")
print(john.sleep())                 # Result = Name is sleeping
print(kyle.sleep())                 # Result = Name is sleeping
print()

# Test view_health_records method
print("-----Checking view_health_records Method-----")
print(john.view_health_records())   # Result = health records
print(beth.view_health_records())   # Result = health records
print()

# Create staff
zk = Zookeeper("Eden", 867)
vet = Veterinarian("Patrick", 420)

# Test staff duties
print("-----Checking perform_duties Method-----")
print(vet.perform_duties())
print(zk.perform_duties())
print(vet.perform_duties())
print()

# Assign animals
zk.assign_animal(john)
vet.assign_animal(kyle)
print()

# Zookeeper feeding animals
print("-----Checking feed_animal Method-----")
print(zk.feed_animal(john))
print()

# Clean enclosure
print("-----Checking clean_enclosure Method-----")
zk.clean_enclosure(savannah)
print("Cleanliness after cleaning:", savannah.cleanliness)
print()

# Health check
print("-----Checking conduct_health_check Method-----")
record = vet.conduct_health_check(
    john,
    description="Minor leg injury",
    severity="M",
    treatment_plan="Rest for 48 hours"
)
print()

# Confirm record
print("-----Confirming Record-----")
for r in john.view_health_records():
    print(r)
print()

# Mark record resolved
print("-----Checking mark_resolved Method-----")
record.mark_resolved()
print("Updated status:", record.status)
print()

# Removing animal
print("-----Checking remove_animal Method-----")
savannah.remove_animal(john)
print(savannah.list_animals())
print()