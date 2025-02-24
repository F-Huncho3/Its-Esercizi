lista_a:list = [2,6,8,3]
lista_b:list = [9,1,4,5]
lista_c:list = []



sum = 0

for i in range(len(lista_a)):
    
    sum = lista_a[i] + lista_b[len(lista_a) - 1 - i]

    lista_c.append(sum)

print (f"La lista A è composta da {lista_a}")
print (f"La lista B è composta da {lista_b}")
print (f"La lista C è composta da {lista_c}") 









