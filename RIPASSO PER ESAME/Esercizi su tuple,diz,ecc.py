def tuplelist(listatuple:list[tuple]) ->dict:

    dizionario:dict = {}

    for tupla in listatuple:

        if tupla[0] in dizionario:

            dizionario[tupla[0]] += tupla[1]

        else:

            dizionario[tupla[0]] = tupla[1]

    return dizionario
    

print(tuplelist([("A",8), ("B",8), ("C",6), ("A", 4)]))
    




def negorposnumber(listanumeri:list[int|float])-> dict:

    dizionumeri:dict[str,list] = {"Positivi": [], "Negativi":[]}


    for number in listanumeri:

        if number >0 :

            dizionumeri["Positivi"].append(number)

        else:

            dizionumeri["Negativi"].append(number)

    return dizionumeri


print(negorposnumber([1,2,3,4,5,6,3,5,6,-2,-4,-8,-9]))


def products(prodotti:dict) ->dict:

    newdict:dict = {}

    for key,value in prodotti.items():

        if value < 50:

            newdict[key] = ((value)*1.10)

        else:

            pass

    return newdict


prodottiss:dict= {"Pasta": 30, "Carne": 55, "Pesto":10}


print(products(prodottiss))










