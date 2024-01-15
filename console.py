#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def help_quit(self):
        """Prints help message for quit command."""
        print("Quit command to exit the program.")

    def help_EOF(self):
        """Prints help message for EOF command."""
        print("EOF signal to exit the program.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

class User(BaseModel):
    """Represents a User in the HBnB project."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

class State(BaseModel):
    """Represents a State in the HBnB project."""
    name = ""

class City(BaseModel):
    """Represents a City in the HBnB project."""
    state_id = ""
    name = ""

class Amenity(BaseModel):
    """Represents an Amenity in the HBnB project."""
    name = ""

class Place(BaseModel):
    """Represents a Place in the HBnB project."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

class Review(BaseModel):
    """Represents a Review in the HBnB project."""
    place_id = ""
    user_id = ""
    text = ""
