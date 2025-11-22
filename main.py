'''
File: main.py
Description: A brief description of this Python module.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''
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
print(savannah.add_animal(john))    # Result = True
print(savannah.add_animal(kyle))    # Result = False

# Check enclosure status
print(savannah.report_status())     # Result = Status report

# Test make_sound method
print(john.make_sound())            # Result = Mammal sound
print(kyle.make_sound())            # Result = Bird sound

# Test eat method
print(beth.eat())                   # Result = Name, species and what they're eating
print(john.eat())                   # Result = Name, species and what they're eating

# Test sleep method
print(john.sleep())                 # Result = Name is sleeping
print(kyle.sleep())                 # Result = Name is sleeping

# Test view_health_records method
print(john.view_health_records())   # Result = health records
print(beth.view_health_records())   # Result = health records

# Create staff
zk = Zookeeper("Eden", 867)
vet = Veterinarian("Patrick", 420)

# Test staff duties
print(zk.perform_duties())
print(vet.perform_duties())

# Assign animals
zk.assign_animal(john)
vet.assign_animal(kyle)

# Zookeeper feeding animals
print(zk.feed_animal(john))

# Clean enclosure
zk.clean_enclosure(savannah)
print("Cleanliness after cleaning:", savannah.cleanliness)

# Health check
record = vet.conduct_health_check(
    john,
    description="Minor leg injury",
    severity="M",
    treatment_plan="Rest for 48 hours"
)

# Confirm record
for r in john.view_health_records():
    print(r)