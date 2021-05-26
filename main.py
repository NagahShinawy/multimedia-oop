"""
created by Nagaj at 25/05/2021
"""

from data import movies
from members import Producer, Director, Singer
from movie import Movie
from song import Song

movie: dict = movies[0]
director = movie["director"].split()
producer = movie["producer"].split()
tim = Director(fname=director[0], lname=director[-1])
john = Producer(fname=producer[0], lname=producer[-1])


def dump_movies():
    for _movie in movies:
        title = _movie["title"]
        released = _movie["released"]

        mov = Movie(
            title=title,
            released=released,
            producer=john,
            director=tim,
        )

        tim.add_art(mov)
        john.add_art(mov)
        # print(mov.to_json())
        yield mov


def dump_songs():
    pass


if __name__ == "__main__":
    for mo in dump_movies():
        print(mo.to_json())

    print("#" * 100)
    print(tim.to_json())

    print("#" * 100)
    print(john.to_json())
    monir = Singer("Mo", "Monir", "1950")
    song = Song("song", "1990", john, monir)
    print("#" * 100)
    print(monir.to_json())
    monir.add_art(song)
    print(monir.to_json())
    print(song.to_json())

    print("#" * 100)
    print(tim)
    print(repr(tim))
    print(song in tim)  # False  , you can do this using __contains__
    print(mo in tim)  # True  , you can do this using __contains__

    print("#" * 100)
    for movie in tim:  # , you can do this using __getitem__
        print(repr(movie))

    print("#" * 100)
    print(len(tim))  # , you can do this using __len__
    print(len(john))  # , you can do this using __len__

    print("#" * 100)
    print(mo == 1)   # , you can do this using __eq__
    print(mo >= 1)   # , you can do this using __ge__
    print(mo > 1)   # , you can do this using __gt__
    print(mo <= 1)   # , you can do this using __le__
    print(mo < 1)   # , you can do this using __lt__
