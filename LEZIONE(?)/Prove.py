#L'utente inserisce in input una stringa con degli spazi, e si deve stampare una stringa con la prima lettera di ogni parola maiuscola.


frase:str = str(input("Inserisci una frase ")).title()

parole = frase.split()

result : list[str] = []

for parola in parole:
    p_in = parola[:-1]
    p_ultima = parola[-1]

    nuova = p_in + p_ultima.upper()
    result.append(nuova)

print (" ".join(result))














#res = ' '.join(
    #map(
        #lambda word: word[0].upper() + word[1:-1] + word[-1].upper()  # Capitalize first and last character
        #if len(word) > 1 else word.upper(),  # If word length is 1, capitalize the whole word
        #frase.split()  # Split `s`into words
 #   )
#)
#print(res)
