"""
created by Nagaj at 25/05/2021
"""
from base import Member
from mixin import JsonifyMember


class Singer(Member, JsonifyMember):

    def __init__(self, fname, lname, dob):
        super().__init__(fname, lname, dob)
        self.songs = []

    def add_art(self, song):
        self.songs.append(song)

    def to_json(self):
        data: dict = super().to_json()
        data.update({"songs": self.songs})
        return data


class Director(Member, JsonifyMember):

    def __init__(self, fname, lname, dob=None):
        super().__init__(fname, lname, dob)
        self.movies = []

    def add_art(self, movie):
        self.movies.append(movie)

    def to_json(self):
        data: dict = super().to_json()
        data.update({"movies": self.movies})
        return data


class Producer(Member, JsonifyMember):

    def __init__(self, fname, lname, dob=None):
        super().__init__(fname, lname, dob)
        self.work_history = []

    def add_art(self, art):
        self.work_history.append(art)

    def to_json(self):
        data: dict = super().to_json()
        data.update({"work": self.work_history})
        return data
