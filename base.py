"""
created by Nagaj at 25/05/2021
"""
from abc import ABC, abstractmethod


class Member(ABC):

    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.arts = []

    def __str__(self):
        return f"{self.fname} {self.lname}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fname} {self.lname}"

    def __contains__(self, item):
        return item in self.arts

    def __getitem__(self, item):
        return self.arts[item]

    def __len__(self):
        return len(self.arts)

    @abstractmethod
    def add_art(self, art):
        pass


class MultiMedia(ABC):

    def __init__(self, title, released, producer, length):
        self.title = title
        self.producer = producer
        self.released = released
        self.writers = []
        self.length = length

    @staticmethod
    def validate_value(other):
        if not isinstance(other, (float, int)):
            raise ValueError(f"value '{other}' can not be {other.__class__.__name__}, should, int, float")

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}> By {self.producer}"

    def __lt__(self, other):
        self.validate_value(other)
        return self.length < other

    def __le__(self, other):
        self.validate_value(other)
        return self.length <= other

    def __gt__(self, other):
        self.validate_value(other)
        return self.length > other

    def __ge__(self, other):
        self.validate_value(other)
        return self.length >= other

    def __eq__(self, other):
        # self.validate_value(other)  # todo: fix this bug
        return self.length == other
