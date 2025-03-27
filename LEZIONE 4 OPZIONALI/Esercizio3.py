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
 

    
#FUNZIONE PRODOTTO

def new_product (product_name:str, quantity:int, price:float):

    product_name = {quantity : price}

    return product_name

input_name = str(input("Inserisci il nome del prodotto "))

quantity_number = int(input("Inserisci la quantità "))

price_number = float(input("Inserisci il prezzo "))


def shopping_cart ():

    lista_elimina = []

    total = 0

    print()

    product_list:list[dict] = []

    choice = input("Cosa vuoi inserire")

    while choice != 0:


        match choice:

            case 1:
                product_list.append(new_product(input_name = str(input("Inserisci il nome del prodotto "), 
                quantity_number = int(input("Inserisci la quantità ")), 
                price_number = float(input("Inserisci il prezzo ")) )))

                total += (quantity_number * price_number)

        
            case 2:

                counter =  1

                for product in product_list:

                    print (counter, product)

                    counter += 1 

                print("\nQuesti sono i prodotti del tuo carrello")



            case 3 :

                print ("Scegli quale prodotto vuoi eliminare  ")

                counter =  1

                for counter,product in product_list:

                    print (counter, product)

                    counter += 1 

                elimina = 0

                elemina = int(input("Inserisci il numero del prodotto "))

                



                

                product_list.pop(elimina -1 )

                

            

            

                




            

        









