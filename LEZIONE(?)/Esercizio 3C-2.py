voto_laurea = (input("Inserisci il tuo voto di laurea  "))



if voto_laurea.isnumeric():
    voto_laurea = int(voto_laurea)
    match voto_laurea:

            case voto_laurea if voto_laurea >= 66 and voto_laurea < 70:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 1.0")

            case voto_laurea if voto_laurea >= 70 and voto_laurea <= 75:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 1.7")

            case voto_laurea if voto_laurea >= 76 and voto_laurea <= 80:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 2.0")

            case voto_laurea if voto_laurea >= 81 and voto_laurea <= 85:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 2.3")

            case voto_laurea if voto_laurea >= 86 and voto_laurea <= 90:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 2.7")

            case voto_laurea if voto_laurea >= 91 and voto_laurea <= 95:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 3.0")

            case voto_laurea if voto_laurea >= 96 and voto_laurea <= 100:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 3.3")

            case voto_laurea if voto_laurea >= 101 and voto_laurea <= 105:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 3.7")

            case voto_laurea if voto_laurea >= 106 and voto_laurea <= 110:
                print(f"Il voto in GPA corrispondente a {voto_laurea} è 4.0")

            case _:
                print ("Voto non valido nella scala GPA")
    
else:
    print("L'elemento inserito non va bene ")
    

