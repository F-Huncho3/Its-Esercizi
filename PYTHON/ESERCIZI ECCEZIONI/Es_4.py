class DataManagment :

    def __init__(self, datelist:list ):

        self.setDateList(datelist)


    def setDateList (self, datelist:list):

        self.datelist = datelist

    
    
    def viewDates (self):

        if datelist:

            i = 1

            for date in self.datelist:

                print (f"DATE|{i}|-{date}")

                i += 1


            return print(f"These are the dates")
        
        else:

            raise Exception (f"The list is empty")
        
    def addDate (self, gg:int, mm:int, aaaa:int):

        newDate:list = [gg,mm,aaaa]

        self.datelist.append(newDate)

        return self.datelist, newDate
    
    def deleteDate (self):

        i = 1

        print ("These are the dates")

        for date in self.datelist:

            print (f"DATE|{i}| {date}")

            i += 1

        delitingDate = int(input("Chose the date to delete ->"))

        self.datelist.pop(delitingDate-1)


    def modifyDate (self):

        i = 1

        for date in self.datelist:

            print (f"DATE|{i}| {date}")

            i += 1

        modifyindDate = int(input("Chose the date to modify ->"))

        self.datelist[modifyindDate-1]
        
        modylist:list = self.datelist[modifyindDate-1]
        



        print("Modify:\n|1|Day \n|2|Month \n|3|Year")

        modychoice = int(input("What you want to modify?"))

        if modychoice-1 == 0:


            modylist[modychoice-1] = int(input("Modifing Day->"))

            print ("Modify Month?")

            choice = str(input())

            if choice == "Yes":

                modylist[1] = int(input("Modifing Month->"))

            elif choice == "No":

                print ("Modify Year?")

                choice = str(input())

                if choice == "Yes":

                    modylist[2] = int(input("Modifing Year->"))

                elif choice == "No":

                    pass
            else:
                pass






        elif modychoice-1 == 1:


            modylist[modychoice-1] = int(input("Modifing Month->"))

            print ("Modify Day?")

            choice = str(input())

            if choice == "Yes":

                modylist[0] = int(input("Modifing Day->"))

            elif choice == "No":

                print ("Modify Year?")

                choice = str(input())

                if choice == "Yes":

                    modylist[2] = int(input("Modifing Year->"))

                elif choice == "No":

                    pass
            else:
                pass


        elif modychoice -1 == 2:

            modylist[modychoice-1] = int(input("Modifing Year->"))

            print ("Modify Month?")

            choice = str(input())

            if choice == "Yes":

                modylist[1] = int(input("Modifing Month->"))

            elif choice == "No":

                print ("Modify Day?")

                choice = str(input())

                if choice == "Yes":

                    modylist[0] = int(input("Modifing Day->"))
            else:
                pass


        else:

            print("ERROR")



        
        
        

        


    

        

            

                    

                    





            
            

        


    


        
        
 





datelist:DataManagment = DataManagment ([])

datelist.addDate(1,2,2025)

datelist.addDate(2,3,2026)

datelist.viewDates()

datelist.modifyDate()

datelist.viewDates()







        

        
        

        
    



