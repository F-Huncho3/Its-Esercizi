#9-11. Imported Admin: Create a module users.py containing three classes:

    #User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    #Privileges: holds a list of privileges and a method show_privileges() to display them.
    #Admin: stores a User instance and a Privileges instance as attributes.

#In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.


class User : 

    def __init__(self, first_name:str, last_name:str, username, email:str ):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email


    def describe_user (self):

        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"E-mail: {self.email}")


    def greet_user (self):

        print(f"Hello {self.first_name}{self.last_name}, your username is {self.username} and your e-mail is {self.email}, is that correct?")



class Privileges:

    def __init__(self, privileges_list):

        self.privileges_list = privileges_list


    def set_privileges(self, privileges_list:list[str]):

        self.privileges_list = privileges_list

        return self.privileges_list
    

    def show_privileges(self):

        print(self.privileges_list)





class Admin:

    def __init__(self, user:User, privilegio:Privileges):

        self.user = user

        self.privilegio = privilegio



    def show_info(self):

        self.user.describe_user()
        self.privilegio.show_privileges()






        
