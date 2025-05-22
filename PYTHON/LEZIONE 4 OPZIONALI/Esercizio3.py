#Creare una funzione che definisce un prodotto (con nome, prezzo e quantità) 

'''Creare un'altra funzione che controlli il carrello della spesa.

- Il carrello deve permettere di visualizzare i prodotti, aggiungerli e/o rimuoverli.

- La funzione deve anche calcolare il totale e applicare sconti e/o tasse.

-Implementare un for loop che iteri sugli oggetti del carrello e che ne stampi in output le informazioni su ogni prodotto.


1. FUNZIONE PRODOTTO:
    1.1 Nome 
    1.2 Prezzo
    1.3 Quantità 

    In base al nome inserito devo essere in grado di associare prezzo e quantità

    Dizionario: implementiamo un dizionario che in base al nome del prodotto mi riesca a ricavare il valore e la quantità.

    Inseriamo il dizionario in una lista iterabile


2. FUNZIONE CARRELLO:
    Lo user deve poter scegliere di aggiunger/rimuovere prodotti, vedere i prodotti ed il totale.

    2.1 Aggiungere
    2.2 Rimuovere
    2.3 Visualizzare
    2.4 Totale


3. ITERAZIONE DEL CARRELLO
    Visualizzare le informazioni dettagliate dei prodotti ed il totale (preferibilmente all'interno della FUNZIONE CARRELLO)

'''
 

tax = 0

total = 0

discount = 0

scelta = 10

lista_prodotti = []
#FUNZIONE PRODOTTO

def new_product (product_name:str, quantity:int, price:float ) -> dict:

    product_name:dict = {"product name": product_name, "Quantity" : quantity, "Price" : price}

    return product_name


def shopping_cart():

    #Inseriamo un messaggio per far decidere allo user cosa fare
    total = 0
    
    

    scelta:int = int(input("Inserisci la scelta"))

    match scelta:

        case 1: #aggiungiamo al carrello il prodotto.

            product_name:str = str(input("Inserisci il nome del prodotto"))
            quantity:int = int(input("Inserisci la quantità di oggetti"))
            price : float = float(input("Inserisci il prezzo"))

            lista_prodotti.append(new_product(product_name,quantity,price))
 
            
            total += quantity*price
            print (total,lista_prodotti)

            
            



        

            

            

            

        #case 2: #eliminiamo un prodotto dal carrello

            #elimina:str = str(input("Scegli il prodotto che vuoi eliminare"))

            #for product in lista_prodotti:

                #if elimina == product_name:

                    #total -= product_name["Quantity"] * product_name["Price"]

                #else:

                    #pass

    return total,lista_prodotti


for i in range (0,3):

    print(shopping_cart(total))








    

        






            

        









