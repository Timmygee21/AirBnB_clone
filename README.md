
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
