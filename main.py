"""
created by Nagaj at 25/05/2021
"""

from data import movies
from members import Producer, Director
from movie import Movie

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
