# 0x00. AirBnB clone - The console

Welcome to the AirBnB clone project! This is the initial step towards building a full web application resembling AirBnB. This phase involves creating a command interpreter to manage AirBnB objects.

## Objective

The goal of this project is to:

- Implement a command-line interface to handle AirBnB objects such as User, State, City, Place, etc.
- Set up a parent class (BaseModel) responsible for initialization, serialization, and deserialization of future instances.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes for AirBnB objects inheriting from BaseModel.
- Develop the first abstracted storage engine for the project: File storage.
- Construct comprehensive unit tests to validate classes and the storage engine.

## What's a Command Interpreter?

Similar to a Shell, the Command Interpreter is tailored to manage specific functionalities related to AirBnB objects:

- Creation of new objects (e.g., User, Place)
- Retrieval of objects from files, databases, etc.
- Execution of operations on objects (count, stats, etc.)
- Updating object attributes
- Deletion of objects

## Python Unit Tests

- Tests organized within a `tests` folder mirroring the project's structure
- Usage of `unittest` module for testing
- All test files and folders named with the prefix `test_`
- All your tests aree executed by using this command: `python3 -m unittest discover tests`
- All tests also pass in non-interactive mode:
```bash
$ echo "python3 -m unittest discover tests" | bash
```

## Execution
The Shell works in both interactive and non-interactive modes. Examples include:

**Interactive Mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

**Non-Interactive Mode:**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Supported Commands

The `console.py` command interpreter supports the following commands:

### create

Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.

```
$ create BaseModel
```

- If the class name is missing, print **class name missing** (e.g., `$ create`).
- If the class name doesn't exist, print **class doesn't exist** (e.g., `$ create MyModel`).

### show

Prints the string representation of an instance based on the class name and id.

```
$ show BaseModel 1234-1234-1234
```

- If the class name is missing, print **class name missing** (e.g., `$ show`).
- If the class name doesn't exist, print **class doesn't exist** (e.g., `$ show MyModel`).
- If the id is missing, print **instance id missing** (e.g., `$ show BaseModel`).
- If the instance of the class name doesn't exist for the id, print **no instance found** (e.g., `$ show BaseModel 121212`).

### destroy

Deletes an instance based on the class name and id, saving the change into the JSON file.

```
$ destroy BaseModel 1234-1234-1234
```

- If the class name is missing, print **class name missing** (e.g., `$ destroy`).
- If the class name doesn't exist, print **class doesn't exist** (e.g., `$ destroy MyModel`).
- If the id is missing, print **instance id missing** (e.g., `$ destroy BaseModel`).
- If the instance of the class name doesn't exist for the id, print **no instance found** (e.g., `$ destroy BaseModel 121212`).

### all

Prints all string representations of instances based or not on the class name.

```
$ all BaseModel
```

- If the class name doesn't exist, print **class doesn't exist** (e.g., `$ all MyModel`).

### update

Updates an instance based on the class name and id by adding or updating an attribute.

```
$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
```

- If the class name is missing, print **class name missing** (e.g., `$ update`).
- If the class name doesn't exist, print **class doesn't exist** (e.g., `$ update MyModel`).
- If the id is missing, print **instance id missing** (e.g., `$ update BaseModel`).
- If the instance of the class name doesn't exist for the id, print **no instance found** (e.g., `$ update BaseModel 121212`).
- If the attribute name is missing, print **attribute name missing** (e.g., `$ update BaseModel existing-id`).
- If the value for the attribute name doesn't exist, print **value missing** (e.g., `$ update BaseModel existing-id first_name`).
- Only one attribute can be updated at a time.
- Only simple arguments can be updated: string, integer, and float.
