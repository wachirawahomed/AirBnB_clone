#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
import shlex
import json
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        obj_key = "{}.{}".format(args[0], obj_id)
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = storage.all()
        obj_key = "{}.{}".format(args[0], obj_id)
        if obj_key in objs:
            del objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objs.items()
                   if args[0] == key.split('.')[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        objects = storage.all()
        obj_key = "{}.{}".format(class_name, obj_id)
        if obj_key not in objects:
            print("** no instance found **")
            return

        obj = objects[obj_key]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value_str = args[3]
        attr_value = None
        if isinstance(attr_value_str, str):
            try:
                attr_value = int(attr_value_str)
            except ValueError:
                try:
                    attr_value = float(attr_value_str)
                except ValueError:
                    attr_value = attr_value_str

        if attr_value is None:
            print("** invalid value **")
            return

        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, or updated_at **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()

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
