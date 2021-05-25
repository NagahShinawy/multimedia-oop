"""
created by Nagaj at 25/05/2021
"""
from abc import ABC, abstractmethod


class Member(ABC):

    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob

    def __repr__(self):
        return f"{self.fname} {self.lname}"

    @abstractmethod
    def add_art(self, art):
        pass


class MultiMedia(ABC):

    def __init__(self, title, released, producer):
        self.title = title
        self.producer = producer
        self.released = released
        self.writers = []

    def __str__(self):
        return f"{self.__class__.__name__} <{self.title}> By {self.producer}"
