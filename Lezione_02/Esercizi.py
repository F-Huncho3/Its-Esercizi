#1-1
x:float = 1.5
y:float = 1.0/x 
print(x,y,y*x)
print((x*y)-x)

#1-2
x:float = 4.0
y:float = (x%2.0)
print (x)
print (y)

x:float = -4.0
y:float = (x%2.0)
print (x)
print (y)
'''Siccome x è "divisible" per due in entrambi i casi 
il risultato dell'operazione è lo stesso
'''
#1-3
a: int = 2

b: int = 4

c: int = 6

print(a)

print(b)

print(c)

Media: int = (a+b+c)/3

print(Media)

#1-4
x: int = 2025

mylist= [2,0,2,5]

print(mylist[0])

print(mylist[1])

print(mylist[2])

print(mylist[3])

#1-5
gradi_fahrenheit: int = 72
gradi_Celsius = 5*(gradi_fahrenheit - 32)/9
print(gradi_fahrenheit)

#1-6
TS_Bakery_Menù:dict = {"Pizza":9.00, "Pasta":10.50, "Zuppa":7.00, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine_Fritte": 5.50, "Patate_al_forno": 5.50,
"Verdura_del_giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia_con_Nutella": 6.00, "Coca_Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}

totale = 0
ordine:dict={"Pizza":9.00, "Patatine_Fritte": 5.50, "Cheesecake": 6.00, "Coca_Cola": 3.50}

totale += ordine["Pizza"]
totale += ordine["Patatine_Fritte"]
totale += ordine["Cheesecake"]
totale += ordine["Coca_Cola"]

print(totale)



