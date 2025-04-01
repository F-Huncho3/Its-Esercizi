#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, first_name:str, last_name:str,title:str,age:int):

        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.age = age
        self.login_attempts = 0 

    def describe_user(self):
        
        print (f"Name: {self.first_name}")
        print (f"Last Name: {self.last_name}")
        print (f"Title: {self.title}")
        print (f"Age: {self.age}")
        print (f"Login attempts: {self.login_attempts}")


    def increment_login_attempts (self)->int:

        self.login_attempts += 1

        return self.login_attempts

    def reset_login_attempts (self)->int:

        self.login_attempts = 0

        return self.login_attempts




fm:User = User("Francesco","Magno","Senior",21)

fm.describe_user()


fm.increment_login_attempts()
fm.increment_login_attempts()
print(fm.increment_login_attempts())




print(fm.reset_login_attempts())

