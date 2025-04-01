from ESERCIZIO9_11 import *

fm:User = User("Francesco","Magno","francescoHuncho","blabla@cia.com")

privi:Privileges = Privileges(["Amministratore","blaBla"])


admin:Admin = Admin(fm,privi)

admin.show_info()