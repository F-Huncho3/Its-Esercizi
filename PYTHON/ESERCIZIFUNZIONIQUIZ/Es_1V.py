def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    i=0
    sum = 0

    new_list:list = []
    
    if len(x) != len(y):

        print("Error the lists must have the same lenght")

    else:

        while i <= len(x) - 1:

            new_list.append(x[i]+ y[i])

            i += 1

            

        

        return new_list 



         


