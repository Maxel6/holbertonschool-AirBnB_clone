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
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
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

    def do_destroy(self, arg):
        from models.base_model import BaseModel
        from models.engine.file_storage import FileStorage
        arg = arg.split()
        if len(arg) < 2:
            if len(arg) == 0:
                print("** class name missing **")
            elif len(arg) == 1:
                print("** instance id missing **")
            return
        class_name = arg[0]
        instance_id = arg[1]
        try:
            cls = globals()[class_name]
            if isinstance(cls, type):
                instances = FileStorage().all()
                key = class_name + "." + instance_id
                if key in instances:
                    instances.pop(key)
                    FileStorage().save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")

    
    def do_all(self, arg):
        from models.engine.file_storage import FileStorage

        classes = arg.split()
        instances = FileStorage().all()

        if len(classes) == 0:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = classes[0]
            try:
                cls = globals()[class_name]
                if isinstance(cls, type):
                    filtered_instances = [str(instance) for instance in instances.values() if isinstance(instance, cls)]
                    print(filtered_instances)
                else:
                    print("** class doesn't exist **")
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        from models.base_model import BaseModel
        from models.engine.file_storage import FileStorage
        arg = arg.split()
        if len(arg) < 4:
            if len(arg) == 0:
                print("** class name missing **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            return
        class_name = arg[0]
        instance_id = arg[1]
        attribute_name = arg[2]
        attribute_value = arg[3]
        try:
            cls = globals()[class_name]
            if isinstance(cls, type):
                instances = FileStorage().all()
                key = class_name + "." + instance_id
                if key in instances:
                    instance = instances[key]
                    if attribute_name not in ["id", "created_at", "updated_at"]:
                        setattr(instance, attribute_name, type(attribute_value)(attribute_value))
                        FileStorage().save()
                    else:
                        print("** cannot update '{}' attribute **".format(attribute_name))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except KeyError:
            print("** class doesn't exist **")

       


    def do_help(self, arg):
        """Affiche l'aide pour les commandes."""
        commands = {
            "hello": "Greets you in the most pleasing way a dev could hope for.",
            "quit": "Quit command to exit the program.",
            "EOF": "Quit command to exit the program.",
            "create": "Create a new instance of a class.",
            "show": "Print the string representation of an instance.",
            "destroy": "Delete an instance based on the class name and ID.",
            "all": "Print string representations of all instances (filtered by class name if provided)."
        }

        if arg:
            if arg in commands:
                print(commands[arg])
            else:
                print("Command not found.")
        else:
            print("Documented commands (type help <command>):")
            for command, description in commands.items():
                print(f"{command:<10} {description}")



if __name__ == '__main__':
    HBNBCommand().cmdloop()