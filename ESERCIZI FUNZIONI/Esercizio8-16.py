#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn





#First Approach:
#Import della funzione singolarmente dal "Modulo".
import printing_functions
printing_functions.printing_func("Ciao")




#Second Approach:
#Scelta della funzione da importare.
from printing_functions import printing_func



#Third Approach:
#Scelta della funzione da importare come funzione.
from printing_functions import printing_func as fn




#Fourth Approach:
#Scelta del "modulo" da importare come modulo/main
import printing_functions as mn


#Fifth Approach:
#Importare tutto il "Modulo"
from printing_functions import *
