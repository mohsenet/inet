#pass
import json


class Parrot:

    # class attribute (and static)
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oop_1(request):
    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    # access the class attributes
    print("Blu is a {}".format(blu.__class__.species))
    print("Woo is also a {}".format(woo.__class__.species))

    # access the instance attributes
    print("{} is {} years old".format(blu.name, blu.age))
    print("{} is {} years old".format(woo.name, woo.age))
    return json.dumps({
        "data": blu.species,
        "site_address": "https://www.programiz.com/python-programming/object-oriented-programming",
    })