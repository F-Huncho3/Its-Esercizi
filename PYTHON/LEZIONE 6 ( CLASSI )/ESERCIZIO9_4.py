#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:

    def __init__(self,restaurant_name:str,cuisine_type:str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant (self):

        print(self.restaurant_name)
        
        print(self.cuisine_type)

        print (self.number_served)

        
    
    

    def open_restaurant(self):

        return print("The restaurant is open")
    
    def setnumber_served(self, number_served:int):

        self.number_served = number_served


    def incrementNumber_served (self, number:int):

        self.number_served += number
        
    
   
    


restaurant = Restaurant("Frattini","Cucina romana")


restaurant.setnumber_served(20)



restaurant.describe_restaurant()


restaurant.incrementNumber_served(4)


restaurant.describe_restaurant()
