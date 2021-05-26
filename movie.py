"""
created by Nagaj at 25/05/2021
"""

from base import MultiMedia
from mixin import JsonifyMultiMedia


class Movie(MultiMedia, JsonifyMultiMedia):

    def __init__(self, title, released, producer, director, length=1):
        super().__init__(title, released, producer, length)
        self.director = director

    def __repr__(self):
        return f"{self.__class__.__name__} <{self.title}> By {self.director}"

    def to_json(self):
        data: dict = super().to_json()
        data.update({"director": self.director.to_json(), "producer": self.producer.to_json()})
        return data
