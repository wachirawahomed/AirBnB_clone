#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
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
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(" ")
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in storage.all()[class_name]:
            print("** no instance found **")
            return
        print(storage.all()[class_name][obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(" ")
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in storage.all()[class_name]:
            print("** no instance found **")
            return
        del storage.all()[class_name][obj_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg:
            if arg not in storage.all():
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in storage.all()[arg].values()])
        else:
            print([str(obj) for objs in storage.all().values()
                  for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(" ")
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key not in storage.all()[class_name]:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[class_name][obj_key]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        command, arg, *_ = line.split(".")
        if command in ["all", "show", "destroy", "update"]:
            arg = arg.replace("(", "").replace(")", "").replace(",", "")
        elif command == "create":
            arg = command + " " + arg
        self.onecmd(arg)

    def precmd(self, line):
        """Hook method executed just before the command is executed"""
        commands = ["all", "show", "destroy", "update"]
        for cmd in commands:
            if cmd in line:
                return line.replace(".", " ")
        return line

    def do_help(self, arg):
        """Help command to display documentation of commands"""
        if arg == "":
            cmd.Cmd.do_help(self, arg)
        else:
            try:
                eval("self.help_" + arg + "()")
            except AttributeError:
                print("** no help on " + arg)

    def help_all(self):
        """Help for all command"""
        print("Prints all string representations of all instances")

    def help_create(self):
        """Help for create command"""
        print("Creates a new instance of BaseModel")

    def help_destroy(self):
        """Help for destroy command"""
        print("Deletes an instance based on the class name and id")

    def help_show(self):
        """Help for show command"""
        print("Prints the string representation of an instance")

    def help_update(self):
        """Help for update command"""
        print("Updates an instance based on the class name and id")

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
