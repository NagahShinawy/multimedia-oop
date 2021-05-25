"""
created by Nagaj at 25/05/2021
"""

from abc import ABC, abstractmethod


class JsonifyMultiMedia(ABC):

    @abstractmethod
    def to_json(self):
        return {
            "title": self.title,
            "released": self.released,
            "producer": self.producer,
        }


class JsonifyMember(ABC):

    @abstractmethod
    def to_json(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
        }
