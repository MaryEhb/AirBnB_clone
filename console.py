#!/usr/bin/python3
"""Console 0.0.1"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
