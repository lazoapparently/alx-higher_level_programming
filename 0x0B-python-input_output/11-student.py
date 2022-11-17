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

    def to_json(self, attrs=None):
        """Retrieves a dictionary of this students attributes.
        Returns:
            dict: A dictionary of this students attr
        """
        if '__dict__' in dir(self):
            res = dict()
            can_filter = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                can_filter = True
            for key in self.__dict__.keys():
                if (not can_filter) or (can_filter and key in attrs):
                    res[key] = self.__dict__[key]
            return res

    def reload_from_json(self, json):
        """Replaces all attr of student instance with
        key-value pairs in the given dir.
        Args:
            jso (dict): A dictionary of new attributes
        """
        if isinstance(json, dict) and ('__dict__' in dir(self)):
            # self.__dict__.clear()
            for key in json.keys():
                self.__dict__[key] = json[key]
