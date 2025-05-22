#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop

i = 0
while  i <= 1:
    artist:str = str(input("Inserisci il nome dell'artista "))
    album_name = input("Inserisci il nome dell'album ")
    i += 1
    if i == 1:
        domanda:str = str(input("Vuoi inserire il numero di canzoni? (Scrivere si o no)")).title()

        match domanda:
            case "Si":
                numero_canzoni = input("Inserisci il numero di canzoni nell'album ")

            case "No":
            
                n = ""

            case _:
                print("Inserimento non valido")
            
    break

n = numero_canzoni




if numero_canzoni == "":

    n = None


def make_album(artist:str,album_name,numero_canzoni = None):
    if numero_canzoni is None:
    
        numero_canzoni = "Unknown"
        
    
    

    artist_album:dict = {"Artist": artist , "Album" : album_name , "Numero canzoni" : numero_canzoni}
    
    return artist_album



print(make_album(artist,album_name,n))


#for key, value in artist_album.items():


