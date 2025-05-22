def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contact:dict = {"profile":name, "email":email, "telefono": telefono}

    return contact
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    if name is not None:
        dictionary["profile"] = name
    if email is not None:
        dictionary["email"] = email
    if telefono is not None:
        dictionary["telefono"] = telefono


    return dictionary