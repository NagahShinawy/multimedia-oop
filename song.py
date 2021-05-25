"""
created by Nagaj at 25/05/2021
"""

from base import MultiMedia
from mixin import JsonifyMultiMedia


class Song(MultiMedia, JsonifyMultiMedia):

    def __init__(self, title, released, producer, singer):
        super().__init__(title, released, producer)
        self.singer = singer

    def __repr__(self):
        return f"{self.__class__.__name__} <{self.title}> By {self.singer}"

    def to_json(self):
        data: dict = super().to_json()
        data.update({"singer": self.singer.to_json()})
        return data

