#!/usr/bin/python3
"""Console 0.0.1"""
import ast
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """hbnb Console"""

    prompt = '(hbnb) '

    def emptyline(self):
        """do nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, className=None):
        """ Creates a new instance of <className> """
        if className:
            if className in globals():
                obj = eval(className)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
                based on the class name and id.
        """
        arg_list = args.split(' ')
        className = arg_list[0] if len(arg_list) >= 1 else None
        id = arg_list[1] if len(arg_list) >= 2 else None

        if not className:
            print("** class name missing **")
        else:
            if className not in globals():
                print("** class doesn't exist **")
            else:
                if not id:
                    print("** instance id missing **")
                else:
                    key = className + '.' + id
                    if key in storage.all().keys():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
           (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        arg_list = args.split(' ')
        className = arg_list[0] if len(arg_list) >= 1 else None
        id = arg_list[1] if len(arg_list) >= 2 else None

        if not className:
            print("** class name missing **")
        else:
            if className not in globals():
                print("** class doesn't exist **")
            else:
                if not id:
                    print("** instance id missing **")
                else:
                    key = className + '.' + id
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, className):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all.
        '''
        if className == '':
            for obj in storage.all().values():
                print(obj)
        elif className in globals():
            for obj in storage.all().values():
                if obj.__class__.__name__ == className:
                    print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        arg_list = args.split(' ')
        className = arg_list[0] if len(arg_list) >= 1 else None
        id = arg_list[1] if len(arg_list) >= 2 else None
        name = arg_list[2] if len(arg_list) >= 3 else None
        value = arg_list[3] if len(arg_list) >= 4 else None

        if not className:
            print("** class name missing **")
        else:
            if className not in globals():
                print("** class doesn't exist **")
            else:
                if not id:
                    print("** instance id missing **")
                else:
                    key = className + '.' + id
                    if key in storage.all().keys():
                        if not name:
                            print("** attribute name missing **")
                        else:
                            if not value:
                                print("** value missing **")
                            else:
                                value = ast.literal_eval(value)
                                setattr(storage.all()[key], name, value)
                                storage.save()
                    else:
                        print("** no instance found **")

    def do_count(self, className):
        """Retrieve the number of instances of a class"""
        cnt = 0
        if className == '':
            for obj in storage.all().values():
                cnt += 1
            print(cnt)
        elif className in globals():
            for obj in storage.all().values():
                if obj.__class__.__name__ == className:
                    cnt += 1
            print(cnt)
        else:
            print("** class doesn't exist **")

    def default(self, line: str) -> None:
        """
        Called on an input line when the command prefix is not recognized.
        """
        if '.' in line:
            args = line.split('.')
            className = args[0]
            command = args[1]
            if (command == 'all()'):
                self.do_all(className)
            elif (command == 'count()'):
                self.do_count(className)
            elif 'show(' in command and ')' in command:
                show_arg = className + ' ' + command[6:-2]
                self.do_show(show_arg)
            elif 'destroy(' in command and ')' in command:
                destroy_arg = className + ' ' + command[9:-2]
                self.do_destroy(destroy_arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
