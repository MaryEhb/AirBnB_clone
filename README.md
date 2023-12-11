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

### 1. help
Display help
```
$ help
```

### 2. quit
Quit command to exit the program.
```
$ quit
```

### 3. EOF
Quit command to exit the program.
```
$ EOF
```

### 4. create

Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.

```
$ create BaseModel
```

### 5. show

Prints the string representation of an instance based on the class name and id.

```
$ show BaseModel 1234-1234-1234
$ BaseModel.show("1234-1234-1234")
```

### 6. destroy

Deletes an instance based on the class name and id, saving the change into the JSON file.

```
$ destroy BaseModel 1234-1234-1234
$ BaseModel.detroy("1234-1234-1234)
```

### 7. all

Prints all string representations of instances based or not on the class name.

```
$ all
$ all BaseModel
$ BaseModel.all()
```

### 8. update

Updates an instance based on the class name and id by adding or updating an attribute.

```
$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
```
### 9. count

Retrieves the number of instances of a class.

```
$ count
$ count BaseModel
$ BaseModel.count()
```

## Authors
<ul>
<li><a href="https://github.com/AmiraWalid1">Amira Walid </li>
<li><a href="https://github.com/MaryEhb">Mariem Ehab </li>
</ul>
