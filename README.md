# AirBnB_clone
AirBnB clone - The console

# Contributors

* Bosworth Onyema
* Oloruntola Timothy

# Description
This project is a complete web application, intergrating database storage, a backend API, and front-end interfacing in a clone of AirBnB.
This project currently only implements the backend console.

# The console
* Create your data model
* Manage (create, update, destroy, etc) objects via a console / command interpreter
* Store and persist objects to a file (JSON file)

# Storage
All the classes are handled by the Storage engine in the ```FileStorage``` Class.

# Technologies Used

*```Ubuntu```

*```Bash```

*```Python```

*```Vim```

Styles guideline

*Pycodestyle (version 2.7.)

*PEP8

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using Python 3.8.3 programming language. The editors used were VIM and VSCode. Control version using Git.

# Execution


The console can be run both interactively and no-interactively.

In interactive mode, run the file console.py by itself:


`$ ./console.py
(hbnb) help

Document commands (typehelp <topic></topic>):
=============================================
EOF help guit

(hbnb)
(hbnb)
(hbnb) quit
$```



To quit the console, enter the command ```quit```, or input an EOF signal (```control+D```).

In non-interactive mode, pipe any command(s) into an execution of file ```console.py``` at the command line.

```$ echo "help" | ./console.py
(hbnb)

Document commands (types help <topic></topic>):
===============================================
EOF help quit
(hbnb)
$
$ cat test_help | ./console.py
(hbnb)
$```

# Testing

All the tests are defined in the ```tests``` folder.

# Documentation

* Modules:

```python3 -c 'print(__import__("my_module").__doc__)'```

* Classes:

```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```

* Functions (inside and outside a class):

```python3 -c 'print(__import__("my_module").my_function.__doc__)'```

and

```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```




# Python Unit Tests

. unittest module
. file extinsion .py
. files and folders start with ```test_``` *Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py``` *Execution command: ```python3 -m unittest discocer tests```

 r: python3 -m unittest tests/test_models/test_base.py

# run test in interactive mode

```echo "python3 -m unittest discover tests"``` |bash

# run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

python3 -m unittest discover tests

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
Provide default value of any attribute
In the future, provide the same model behavior for file storage or database storage
