#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.


class User:

    def __init__(self, first_name:str, last_name:str,title:str,age:int):

        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.age = age

    def describe_user(self):
        
        print (f"Name: {self.first_name}")
        print (f"Last Name: {self.last_name}")
        print (f"Title: {self.title}")
        print (f"Age: {self.age}")


        