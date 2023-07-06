#!/usr/bin/python3
"""module to handle console"""
import cmd

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class tro handle the custom prompt

    Returns:
        cmd: opens a custom shell
    """
    prompt = '(hbnb) '

    def do_hello(self, arg):
        """Print a greeting"""
        print("Hello, world!")

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        if arg is None:
            print("** class name missing **")
            try:
                cls = globals()[arg]
                if isinstance(cls, type):
                    print(f"The class {arg} exists.")
                else:
                    print(f"{arg} is not a class.")
            except KeyError:
                print(f"The class {arg} does not exist.")

    def do_help(self, arg):
        """gives little man

        Args:
            arg (input line): command typed in by user
        """
        if arg == "hello":
            print("Greets you in the most pleasing way a dev could hope for.")
        if arg == "quit" or arg == "EOF":
            print("Quit command to exit the program\n")
        else:
            print()
            print("Documented commands (type help <topic>:\n\
========================================\n\
EOF  help  quit\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
