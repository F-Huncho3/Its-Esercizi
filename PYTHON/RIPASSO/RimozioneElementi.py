def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    for num in lista:

        for key,value in da_rimuovere:

            if num == key:

                lista.pop(num)

            else:

                pass