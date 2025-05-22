class Restaurant:

    def __init__(self,restaurant_name:str,cuisine_type:str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant (self):

        print(self.restaurant_name)
        
        print(self.cuisine_type)

        
    
    

    def open_restaurant(self):

        return print("The restaurant is open")
    
   
    


restaurant = Restaurant("Frattini","Cucina romana")

restaurant.describe_restaurant()
restaurant.open_restaurant()
