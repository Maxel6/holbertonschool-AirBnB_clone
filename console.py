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
    created_instance = ()

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
        from models.base_model import BaseModel
        if len(arg) < 1:
            print("** class name missing **")
        else:
            try:
                cls = globals()[arg]
                if isinstance(cls, type):
                    self.created_instance = cls()
                    print(self.created_instance.id)
                    self.created_instance.save()
                else:
                    print("** class doesn't exist **")
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        from models.base_model import BaseModel
        arg = arg.split()
        if len(arg) < 2:
            print("** class name missing **")
            return
        class_name = arg[0]
        instance_id = arg[1]
        try:
            cls = globals()[class_name]
            if isinstance(cls, type):
                from models.engine.file_storage import FileStorage
                instances = FileStorage().all()
                key = class_name + "." + instance_id
                if key in instances:
                    instance = instances[key]
                    print(instance)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")


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