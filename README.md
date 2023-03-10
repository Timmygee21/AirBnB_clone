# AirBnB_clone
AirBnB clone - The console

#Contributors
Bosworth Onyema

Oloruntola Timothy


![AirBnb](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230310T063110Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=87f76efd2438e71e096d842711979312895d2910bf094ba705aafa2dd12cee7c)

 command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
 website (the front-end) that shows the final product to everybody: static and dynamic
 database or files that store data (data = objects) 
 An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

 # The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

# Storage
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
Provide default value of any attribute
In the future, provide the same model behavior for file storage or database storage
