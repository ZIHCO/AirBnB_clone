#!/usr/bin/python3
"""This module contains the class HBNBCommand.
   It is the console for the AirBnB project
"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """The class is a subclass of Cmd, the console for this
       project.
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State", "City",
               "Amenity", "Review"]
    filename = "file.json"
    cmds = ["create", "show", "all", "destroy", "quit", "EOF"]

    def onecmd(self, line):
        """define preline"""
        list_line = line.split()
        if list_line[0] in self.__class__.cmds:
            return super(HBNBCommand, self).onecmd(line)
        list_line = line.split(".")
        this_cls = list_line[0]
        if list_line[1][-2:] == "()":
            cmd = list_line[1][:-2]
            line = cmd + " " + this_cls
            return super(HBNBCommand, self).onecmd(line)
        idx = list_line[1].index("(")
        cmd = list_line[1][:idx]
        if cmd == "update":
            this_attr = list_line[1][(idx + 1):-1].split(", ", maxsplit=1)
            if type(eval(this_attr[1])) is dict:
                this_id = this_attr[0][1:-1]
                attr_dict = this_attr[1]
                line = cmd + " " + this_cls + " " + this_id + " " + attr_dict
                return super(HBNBCommand, self).onecmd(line)
            this_attr = list_line[1][(idx + 1):-1].split(", ")
            this_id = this_attr[0][1:-1]
            attr = this_attr[1][1:-1]
            value = this_attr[2]
            line = (cmd + " " + this_cls + " " + this_id + " " + attr +
                    " " + value)
            return super(HBNBCommand, self).onecmd(line)
        this_id = list_line[1][(idx + 2):-2]
        line = cmd + " " + this_cls + " " + this_id
        return super(HBNBCommand, self).onecmd(line)

    def do_create(self, line):
        """create and save a new instance of BaseModel"""

        if not line:
            print("** class name missing **")
        elif line not in self.__class__.classes:
            print("** class doesn't exist **")
        else:
            new_log = eval(line)()
            new_log.save()
            print(new_log.id)

    def do_show(self, line):
        """Show the string representation of the instance"""

        list_line = line.split()
        validate = self.__class__.line_validator(line)
        if validate == 0:
            validate
        else:
            with open(self.__class__.filename, encoding="utf-8") as f:
                load_file_str = f.read()
                load_dict = json.loads(load_file_str)
            instance = list_line[0] + "." + list_line[1]
            if instance not in load_dict:
                print("** no instance found **")
            else:
                object_dict = load_dict[instance]
                obj = eval(list_line[0])(**object_dict)
                print(obj)

    def do_destroy(self, line):
        """delete objects"""
        list_line = line.split()
        validate = self.__class__.line_validator(line)
        if validate == 0:
            validate
        else:
            with open(self.__class__.filename, encoding="utf-8") as f:
                load_file_str = f.read()
                load_dict = json.loads(load_file_str)
            instance = list_line[0] + "." + list_line[1]
            if instance not in load_dict:
                print("** no instance found **")
            else:
                del load_dict[instance]
            with open(type(self).filename, 'w', encoding="utf-8") as f:
                dump_dict = json.dumps(load_dict)
                f.write(dump_dict)

    def do_all(self, line):
        """print objects"""
        list_line = line.split()
        list_all_obj = []
        if line and line not in self.__class__.classes:
            print("** class doesn't exist **")
        elif (not line) or line == "BaseModel":
            with open(self.__class__.filename, encoding="utf-8") as f:
                load_file_str = f.read()
                load_dict = json.loads(load_file_str)
            for key in list(load_dict):
                this_cls = key.split(".")[0]
                if this_cls == "BaseModel":
                    obj_str = BaseModel(**load_dict[key]).__str__()
                    list_all_obj.append(obj_str)
            print(list_all_obj)
        elif line in self.__class__.classes:
            with open(self.__class__.filename, encoding="utf-8") as f:
                load_file_str = f.read()
                load_dict = json.loads(load_file_str)
            for key in list(load_dict):
                this_cls = key.split(".")[0]
                if this_cls == list_line[0]:
                    obj_str = eval(this_cls)(**load_dict[key]).__str__()
                    list_all_obj.append(obj_str)
            print(list_all_obj)

    def do_update(self, line):
        """update objects"""
        list_line = line.split(maxsplit=2)
        validate = self.__class__.line_validator(line)
        try:
            type(eval(list_line[2]))
            type_dict = True
        except Exception:
            list_line = line.split()
            type_dict = False
        if validate == 0:
            validate
        elif type_dict:
            instance = list_line[0] + "." + list_line[1]
            with open(type(self).filename, encoding='utf-8') as f:
                load_file_str = f.read()
                load_dict = json.loads(load_file_str)
            for item in list(load_dict):
                if instance == item:
                    instance_dict = load_dict[instance]
                    break
            dict_updates = eval(list_line[2])
            for key in list(dict_updates):
                instance_dict[key] = dict_updates[key]
            updated_obj = eval(list_line[0])(**instance_dict)
            updated_obj.save()
        else:
            if len(list_line) < 3:
                print("** attribute name missing **")
            elif len(list_line) < 4:
                print("** value missing **")
            else:
                instance = list_line[0] + "." + list_line[1]
                with open(type(self).filename, encoding='utf-8') as f:
                    load_file_str = f.read()
                    load_dict = json.loads(load_file_str)
                for item in list(load_dict):
                    if instance == item:
                        instance_dict = load_dict[instance]
                        break
                key = list_line[2]
                value = list_line[3]
                instance_dict[key] = eval(value)
                updated_obj = eval(list_line[0])(**instance_dict)
                updated_obj.save()

    def do_count(self, line):
        """count objects"""
        with open(type(self).filename, encoding='utf-8') as f:
            load_file_str = f.read()
            load_dict = json.loads(load_file_str)
            count = 0
            for item in list(load_dict):
                this_cls = item.split(".")[0]
                if this_cls == line:
                    count += 1
        print(count)

    @classmethod
    def line_validator(cls, line):
        """line validator"""
        import os

        list_line = line.split()
        if not line:
            print("** class name missing **")
            return 0
        if list_line[0] not in cls.classes:
            print("** class doesn't exist **")
            return 0
        try:
            id = list_line[1]
        except Exception:
            print("** instance id missing **")
            return 0
        else:
            if not os.path.exists(cls.filename):
                print("** no instance found **")
                return 0
        return 1

    def do_quit(self, line):
        """EOF or quit exits the console"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    do_EOF = do_quit

    def postloop(self):
        """postloop"""
        print("")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
