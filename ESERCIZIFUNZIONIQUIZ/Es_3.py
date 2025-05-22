def prime_factors(n: int) -> list[int]:

    lista_fattori:list = []

    due = 2

    tre = 3

    cinque = 5

    i = n 
    while i >=0:

        if n%i == 0 and i * i == n:

            lista_fattori.append(i)

            n = n/i

        elif n%due== 0 and due * due == n:

            lista_fattori.append(due)

            n = n/due

        elif n%tre== 0 and tre * tre == n:

            lista_fattori.append(tre)

            n = n/tre

        elif n%cinque== 0 and cinque * cinque== n:


            lista_fattori.append(cinque)

            n = n/ cinque

        else:

            if n%2 == 0 and n%3 == 0:

                lista_fattori.append(2)

                n = n/ due

            if n%5 == 0 and n%3 == 0:

                lista_fattori.append(3)

                n = n/ cinque

            if n%2 == 0 and n%5 == 0:

                lista_fattori.append(2)

                n = n/due

    return lista_fattori


print(prime_factors(4))

    


 



    



    





    


