# AirBnB_clone
AirBnB clone - The console

#Contributors

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

#Technologies Used

*```Ubuntu```
*```Bash```
*```Python```
*```Vim```

Styles guideline
*Pycodestyle (version 2.7.*)
*PEP8

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using Python 3.8.3 programming language. The editors used were VIM and VSCode. Control version using Git.
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
Provide default value of any attribute
In the future, provide the same model behavior for file storage or database storage
