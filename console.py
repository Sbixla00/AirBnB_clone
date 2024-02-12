import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print("")  
        return True

    def do_create(self, arg):

        if not arg:
            print("** class name missing **")
            return
        
        class_name = arg.split()[0]
        
        try:
            class_instance = globals()[class_name]()
            class_instance.save()  
            print(class_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):

        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return

        if not arg.split()[1]:
            print("** instance id missing **")
            return
        if arg.split()[1] not in BaseModel.all_id :
            print("** no instance found **")
            return
      
        instance = BaseModel.get_instance_by_id(arg.split()[1])
        print(instance)
    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on the class name and id
        Usage: destroy <class_name> <instance_id>
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if instance_id not in BaseModel.all_instances:
            print("** no instance found **")
            return

        del BaseModel.all_instances[instance_id]
        BaseModel.save()
        print("Instance deleted successfully.")
    
    def do_all(self, arg):
        """
        All command to print string representation of all instances
        Usage: all [<class_name>]
        """
        class_name = arg.split()[0] if arg else None

        if class_name:
            if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
                print("** class doesn't exist **")
                return

        if class_name:
            instances = [str(instance) for instance in BaseModel.all_instances.values() if isinstance(instance, globals()[class_name])]
        else:
            instances = [str(instance) for instance in BaseModel.all_instances.values()]

        for instance_str in instances:
            print(instance_str)
if __name__ == '__main__':
    HBNBCommand().cmdloop()

