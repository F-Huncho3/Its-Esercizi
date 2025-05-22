things : list[str] = ["wakanda", "Rocks", "Tevere", "Ballon", "Italian", "Germany", "Caffè", "Monopolio"]

l = things[2]

print (l.lower())
print (l.upper())
print (l.title())


x = things[6]
y:str = "I want a"

print (f"{y} {x}")



things.insert(3, "Dino")
things.append("January")
things.pop(2)



del things [:]
print (things)




things : list[str] = ["wakanda", "Rocks", "Tevere", "Ballon", "Italian", "Germany", "Caffè", "Monopolio"]


print (sorted(things))

print (sorted(things,reverse=True))

print (things)

print (sorted(things,reverse=False))
print (sorted(things,reverse=True))

things.sort(reverse=False)
print (things)

things.sort(reverse=True)
print (things)