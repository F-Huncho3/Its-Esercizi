class Restaurant:

    def __init__(self,restaurant_name:str,cuisine_type:str):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant (self):

        print(self.restaurant_name, self.cuisine_type)
        
       

    def open_restaurant(self):

        return print("The restaurant is open")
    

restaurant_1 = Restaurant ("Frattini", "Cucina romana")

restaurant_2 = Restaurant ("Porto Fluviale", "Cucina Fusion")

restaurant_3= Restaurant ("Let's go", "Burger")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
