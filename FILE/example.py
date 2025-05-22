PATH: str = "FILE/example.txt"

file = open (PATH, "r", encoding="utf-8")

print(file.read())

file.close()

