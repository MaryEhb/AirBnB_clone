#!/usr/bin/python3
"""Console 0.0.1"""
import cmd


class HBNBCommand(cmd.Cmd):
    """hbnb Console"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the program"""
        return True

    def help_quit(self):
        """Add documentation for quit method"""
        print("Quit command to exit the program")
    
    def do_EOF(self, line):
        """Exit the program"""
        return True

    def help_EOF(self):
        """Add documentation for EOF method"""
        print("EOF command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
