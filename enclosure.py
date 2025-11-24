'''
File: enclosure.py
Description: This python module represents an enclosure class
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """
    This class represents an enclosure in the zoo.
    The enclosure can store animals, has a cleanliness level,
    has an allowed species list and environment type.
    """
    def __init__(self, size, environmental_type, cleanliness, allowed_species, allowed_environment):
        if size <= 0:
            raise ValueError("Size must be positive")
        if not isinstance(cleanliness, int) or not (0 <= cleanliness <= 100):
            raise ValueError("Cleanliness must be a positive integer between 0 and 100")
        if not isinstance(allowed_species, list) or len(allowed_species) == 0:
            raise ValueError("Allowed species must be a non-empty list")

        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness = cleanliness
        self.__allowed_species = allowed_species
        self.__allowed_environment = allowed_environment
        self.__animals = []

    def animal_validate(self, animal):
        """
        Checks if an animal is in the list of allowed species.
        """
        if animal.species not in self.__allowed_species:
            return False

        if self.__environmental_type != self.__allowed_environment:
            return False

        return True

    def add_animal(self, animal):
        """
        Adds a valid animal to the enclosure
        """
        if not self.animal_validate(animal):
            return False

        self.__animals.append(animal)
        animal.assign_enclosure(self)
        return True

    def remove_animal(self, animal):
        """
        Removes animal from the enclosure if animal
        is in enclosure.
        """
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.assign_enclosure(None)
            return True
        return False

    def list_animals(self):
        return [animal.name for animal in self.__animals]

    def report_status(self):
        """
        Returns the enclosure status
        """
        status = "Enclosure Status:\n"
        status += f"Size: {self.__size}\n"
        status += f"Environment: {self.__environmental_type}\n"
        status += f"Cleanliness: {self.__cleanliness}\n"
        status += f"Allowed species: {self.__allowed_species}\n"
        status += "Animals inside: "

        if len(self.__animals) == 0:
            status += "None\n"
            return status

        animal_names = ""
        for i in range(len(self.__animals)):
            animal = self.__animals[i]
            if i == 0:
                animal_names += animal.name
            else:
                animal_names += ", " + animal.name
        status += animal_names + "\n"
        return status

    def clean(self):
        """
        Sets the enclosure cleanliness level to 100
        """
        self.__cleanliness = 100

    # Getters
    @property
    def animals(self):
        return self.__animals.copy()

    @property
    def cleanliness(self):
        return self.__cleanliness

    @property
    def size(self):
        return self.__size

    @property
    def environment(self):
        return self.__environmental_type

