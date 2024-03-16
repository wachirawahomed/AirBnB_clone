#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import json
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "
    class_name = ["BaseModel", "User", "State", "City", "Amenity",
                  "Place", "Review"]

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.class_name:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]
        if class_name not in self.class_name:
            print("** class doesn't exist **")
            return
        obj_key = "{}.{}".format(class_name, obj_id)
        objs = storage.all()
        if obj_key in objs:
            del objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        Usage: all [<class name>]
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.class_name:
            print("** class doesn't exist **")
            return
        else:
            objs = storage.all()
            result = []
            for obj_key, obj in objs.items():
                if arg == obj_key.split('.')[0] or\
                        arg == obj.__class__.__name__:
                            result.append(str(obj))
                            print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) < 4:
            print("** attribute value missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_name:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in objs:
            print("** no instance found **")
            return
        obj = objs[obj_key]
        try:
            setattr(obj, args[2], args[3])
        except Exception as e:
            print(e)
            return
        storage.save()

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
