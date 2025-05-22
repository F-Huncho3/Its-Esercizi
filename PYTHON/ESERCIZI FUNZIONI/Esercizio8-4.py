#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(text:str = "I love Python", size : str = "L"):
    print (f"\nThe size of the shirt will be {size} and the printed text will be {text}")
    

make_shirt()

make_shirt(size= "M")

make_shirt(text= "I love Barbeque", size = "XL")
