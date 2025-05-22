

def validate_password(password:str): 

    uppcount = 0

    speccount = 0

    if len(password) < 20:

        raise Exception(f"The password should be at least 20 characters")
    
    for i in password:

        if i.isupper() == True:
          
          uppcount += 1

          print(uppcount)

    if uppcount < 3: 

        raise Exception (f"The password must have at least 3 upper case characters")
        
    else:

        pass
        
    for i in password:

        if i.isalpha() == True:

            speccount += 1

    if speccount < 4: 

        raise Exception (f"The password must have at least 4 alphanumeric characters")
        
    else:

        pass

    print("Your password is valid")


validate_password("FraNcEsco.!-!Magno)i")
        
