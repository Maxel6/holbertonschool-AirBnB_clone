#!/usr/bin/python3
"""module to handle console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class tro handle the custom prompt

    Returns:
        cmd: opens a custom shell
    """
    prompt = '(hbnb)'

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

    def do_help(self, arg):
        """gives little man

        Args:
            arg (input line): command typed in by user
        """
        if arg == "hello":
            print("Greets you in the most pleasing way a dev could hope for.")
        if arg == "quit" or arg == "EOF":
            print("Rudely leaves the room.")
        if arg == "help":
            print("Sends godblessed help to your rescue.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
