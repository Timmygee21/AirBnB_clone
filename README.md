
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
All the classes are handled by the Storage engine in the `FileStorage` Class.

# Technologies Used

* `Ubuntu`

* `Bash`

* `Python`

* `Vim`

Styles guideline

* Pycodestyle (version 2.7.)

* PEP8

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using Python 3.8.3 programming language. The editors used were VIM and VSCode. Control version using Git.

# Execution

The console can be run both interactively and no-interactively.

In interactive mode, run the file `console.py` by itself:

```
$ ./console.py
(hbnb) help

Document commands (typehelp <topic></topic>):
=============================================
EOF help guit

(hbnb)
(hbnb)
(hbnb) quit
$
```
To quit the console, enter the command `quit`, or input an EOF signal (`control+D`).

In non-interactive mode, pipe any command(s) into an execution of file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)

Document commands (types help <topic></topic>):
===============================================
EOF help quit
(hbnb)
$
$ cat test_help | ./console.py
(hbnb)
$
```
# Testing

All the tests are defined in the tests folder.

# Documentation

* Modules:

`python3 -c 'print(__import__("my_module").__doc__)'`

* Classes:

`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`

* Functions (inside and outside a class):

`python3 -c 'print(__import__("my_module").my_function.__doc__)'`

and

`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

# Python Unit Tests

* unittest module

* File extinsion `.py`
* Files and folders start with `test_` 
* Organization:for `models/base.py`, 
* unit tests in: `tests/test_models/test_base.py` 
* Execution command: `python3 -m unittest discocer tests`
* or: `python3 -m unittest tests/test_models/test_base.py`

# run test in interactive mode

`echo "python3 -m unittest discover tests" |bash`

# run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:

`python3 -m unittest discover tests`

# Usage

* Start the console in interactive mode:

`$ ./console.py
(hbnb)`

* Use help to see the available commands:

```
(hbnb) help

Documented commands (type help <topic></topic>):
================================================
EOF all count create destroy help quit show update

(hbnb)
```
* Quit the console:
`(hbnb) quit
$`

###Console Commands

The commands are displayed in the following format

* Command / usage / example with output*

Create a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

*`create <class>`

`(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)`

* Show

`show <class> <id>`


`(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel]
(6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2022, 8, 29, 3, 28, 45, 571360), 'updated_at': datetime.dayetime(2022, 8, 28, 45, 571360)}
(hbnb)`

* Destroy

	* Delets an instance of a given class with a given ID.* > Update the file.json

*`(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)`

* all
