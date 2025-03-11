#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.



artist:str = str(input("Inserisci il nome dell'artista "))
album_name = input("Inserisci il nome dell'album ")
numero_canzoni = input("Inserisci il numero di canzoni nell'album ")

n = numero_canzoni

if numero_canzoni == "":

    n = None


def make_album(artist:str,album_name,numero_canzoni = None):
    if numero_canzoni is None:
    
        numero_canzoni = "Unknown"
        
    
    

    artist_album:dict = {"Artist": artist , "Album" : album_name , "Numero canzoni" : numero_canzoni}
    
    return artist_album



print(make_album(artist,album_name,n))




