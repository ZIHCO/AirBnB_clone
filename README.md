# AirBnB clone - The console
## 1. Description
This is the first in The AirBnB Clone project; building the console(command intepreter). The command intepreter will take care of:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object.

In addition to the command intepreter, we created our data model by defining our super class [BaseModel](https://github.com/ZIHCO/AirBnB_clone/blob/master/models/base_model.py) and its subclasses defined [here](https://github.com/ZIHCO/AirBnB_clone/blob/master/models).
We have also taken care of storing and persisting objects to a file (JSON file) which will help with the storage engine.

## 2. Command Interpreter
### How to start it
To run the command interpreter, simply run the [console.py](https://github.com/ZIHCO/AirBnB_clone/blob/master/console.py) file with command: ./console.py.
This will start the intepreter and the propmpt "(hbnb)" will appear on the screen. 

### How to use it
The interpreter has the following commands defined: create, quit, EOF, update, destroy, all, and show. The following is the syntax for each command:
* (hbnb) create (class name)
* (hbnb) quit
* (hbnb) EOF
* (hbnb) update (class name) (id) (attribute name) (attribute value)
* (hbnb) destroy (class name) (id)
* (hbnb) all / (hbnb) all (class name)
* (hbnb) show (class name) (id)

### Example  
![Screenshot 2022-11-28 011122](https://user-images.githubusercontent.com/54947406/204164804-39664a08-c6d2-4df9-9aa5-53fdfd181f1b.jpg)

