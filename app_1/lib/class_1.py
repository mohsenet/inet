#pass
import json


class Parrot:

    # class attribute (and static)
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oop_1():
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
        "mode": "0",
        "data": blu.species,
        "site_address": "https://www.programiz.com/python-programming/object-oriented-programming",
    })


class Maximume:
    ip = "192.168.121.156"
    port = "4000"
    os = "CentOS"
    task = "web_server"
    zone = "shaparak"
    developer = "mohsen"
    ssl_support = "no"

    def __init__(self):
        pass

    @staticmethod
    def connect():
        return json.dumps({
            "mode": "1",
            "state": "connecting",
            "role": "full_access",
        })

    @staticmethod
    def diconnect():
        return json.dumps({
            "mode": "2",
            "state": "disconnect",
            "time": "10m",
            "cause": "no_need",
        })

    @staticmethod
    def type_set():
        return json.dumps({
            "mode": "3",
            "type": "tcp",
            "version": "ipv4",
        })















