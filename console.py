#!/usr/bin/python3
'''
A module that contains the console class.
'''
from models.engine.file_storage import FileStorage
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    '''
    A class that sets the airbnb console.
    '''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''
        A method that quits the console.
        '''
        return True

    def do_EOF(self, arg):
        '''
        The End of file Method.
        '''
        return True

    def emptyline(self):
        '''
        A method for enter prompt to do nothing.
        '''
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return

        if args not in globals():
            print("** class doesn't exist **")
            return

        cls = globals()[args]
        new_instance = cls()
        storage.save()

        print(new_instance.id)

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return

        list_args = args.split()

        if list_args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(list_args) != 2:
            print("** instance id missing **")
            return
        instance = f"{list_args[0]}.{list_args[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance])

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return

        list_args = args.split()

        if list_args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(list_args) != 2:
            print("** instance id missing **")
            return
        instance = f"{list_args[0]}.{list_args[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[instance]
        storage.save()

    def do_all(self, args):

        if not args:
            print([str(storage.all()[id]) for id in storage.all()])
            return

        list_args = args.split()

        if list_args[0] not in globals():
            print("** class doesn't exist **")
            return

        list = []
        for instance in storage.all():
            if args in instance:
                list.append(str(storage.all()[instance]))

        print(list)

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return

        list_args = args.split()

        if list_args[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(list_args) < 2:
            print("** instance id missing **")
            return
        instance = f"{list_args[0]}.{list_args[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        if len(list_args) < 3:
            print("** attribute name missing **")
            return

        if len(list_args) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[instance], list_args[2], list_args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
