class Contatti:


    contacts:dict[str,list[str]]

    def __init__(self):

        self.contacts:dict[str] = {}


    def create_contact(self, name:str, phone_numbers:list[str]):

        if name not in self.contacts:

            new_dict:dict = {}

            self.contacts[name] = phone_numbers

            print(f"New Contact--- NAME: {name}, PhoneNumber/s: {phone_numbers}")

            new_dict[name] = self.contacts[name]

        else: 

            print("Name already in contacts")

        return new_dict

    def add_phone_number(self, contact_name:str, phone_number:str):
        
        if contact_name in self.contacts:

                self.contacts[contact_name].append(phone_number)

        else: 

            print ("ERROR")

    def remove_phone_number(self, contact_name:str, phone_number:str):

        if contact_name in self.contacts:
                
                if phone_number in self.contacts[contact_name]:

                    self.contacts[contact_name].remove(phone_number)

                else:

                    print("The number you inserted is not present")

        else:

            print("Contact name not present")


        return self.contacts
    

    
    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str):

        if contact_name in self.contacts:
            
            if old_phone_number in self.contacts[contact_name]:

                new_dict:dict = {}
                    
                self.contacts[contact_name].remove(old_phone_number)

                self.contacts[contact_name].append(new_phone_number)

                new_dict[contact_name] = self.contacts[contact_name]

                return new_dict

            else:

                print("The number you inserted is not present")

        else:

            print("Contact name is not present")

    
    def list_contacts(self):

        print (self.contacts)



    def list_phone_numbers(self, contact_name:str):

        if contact_name in self.contacts:
                
            print (f"NOME: {contact_name}, Numbers: {self.contacts[contact_name]}")



    def search_contact_by_phone_number(self, phone_number:str):

        for key in self.contacts.items():

            if phone_number in self.contacts[key]:

                return f"{key}"
            
            else:

                return f"Error, {phone_number} is not associated with a name"





class Movie:

    #movie_id: str
    #title: str
    #director:str
    #is_rented:bool

    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool = False):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented



    def rent(self) -> None:

        if self.is_rented == True:

            print (f"il film {self.title} è già noleggiato")
        
        else:

            self.is_rented = True
    

    def return_movie(self):

        if self.is_rented == False:

            return f"Il film {self.title} non è noleggiato"
        
        else: 

            self.is_rented = False



class Customer:

    #customer_id:str
    #name:str
    #rented_movies:list[Movie]

    def __init__(self, customer_id:str, name:str):
        
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie:Movie) ->None:

        if movie.is_rented == False:

            self.rented_movies.append(movie)

            movie.rent() 

        else:

            print (f"Il film {movie} è già stato noleggiato")
        

    def return_movie(self, movie:Movie):

        if movie in self.rented_movies:

            self.rented_movies.remove(movie)

            movie.return_movie()

        else:

            return f"Il film non è nella lista"


class VideoRentalStore:

    #movies:dict[str,Movie]
    #customers:dict[str, Customer]


    def __init__(self, movies:dict[str, Movie] = {}, customers:dict[str, Customer] = {}):
        
        self.movies = movies
        self.customers = customers

    def add_movie(self,movie_id:str, title:str, director:str) ->None:

        if movie_id in self.movies:

            print(f"Il film è già presente nel catalogo")

        else:

            movie: Movie = Movie (movie_id = movie_id, title = title, director = director)

            self.movies[movie_id] = movie


    def register_customer(self, customer_id:str, name:str):

        if customer_id in self.customers:

            print(f"Cliente già registrato")

        else:

            customer:Customer = Customer (customer_id = customer_id, name = name)

            self.customers[customer_id] = name

    def rent_movie(self, customer_id:str, movie_id:str):

        if customer_id in self.customers and movie_id in self.movies:

            self.customers[customer_id].rent_movie(self.movies[movie_id])

        else:

            print ("Film già noleggiato")

    def return_movie(self, customer_id:str, movie_id:str) ->None:

        if customer_id in self.customers and movie_id in self.movies:

            self.customers[customer_id].return_movie(self.movies[movie_id])

        else:

            print ("Film non presente")

    def get_rented_movies(self, customer_id:str) ->list[Movie]:

        if customer_id in self.customers:

            return self.customers[customer_id].rented_movies
        
        else:

            print(f"Il cliente non è presente")

            lista_vuota:list = []

            return lista_vuota
        
    def get_all_rented_movies(self) ->list[Movie]:

        all_movies:list[Movie]  = [] 

        for customer in self.customers.values():

            all_movies.extend(customer.rented_movies)

        return all_movies










    
