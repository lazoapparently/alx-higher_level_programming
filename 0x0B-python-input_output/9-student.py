#!/usr/bin/python3
'''A module for managing students.
'''


class Student:
    """Represents a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes student's first name, second and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary of this students attributes.
         Returns:
             dict: A dictionary of this students attr
        """
        if '__dict__' in dir(self):
            return self.__dict__
