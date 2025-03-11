#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.


numeri:list[int] = []
x = 0

for i in range (1000000):
   
    x +=1 
    numeri.append(x)

print (f"The first three items of the list are {numeri[:3]}")

y:int = int(len(numeri)/2)

print (f"The three middle elements of the list are {numeri[y:y+3]}")

print (f"The last three elements of the list are {numeri[-1:-4:-1]}")