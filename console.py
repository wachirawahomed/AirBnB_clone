#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
