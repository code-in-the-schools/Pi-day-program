import datetime
x = datetime.datetime.now()
print(x)

def Calculate_Bdays(x,y):
    

Names = []
Birthdays = []
Start_prompt = input("Would you like to add a birthday? ")
if Start_prompt =="yes": #This will take all nesscary input from the user to store someones birthday
    Collect_names = input("Enter their name ")
    Names.append(Collect_names)
    Collect_Bdays = input("Enter their birthday(yyyy/m/d) ")
    Birthdays.append(Collect_Bdays)
    z=input("Would you like to add another birthday? ")
    while z == "yes":
        Collect_names = input("Enter their name ")
    Names.append(Collect_names)
    Collect_Bdays = input("Enter their birthday(m/d/yyyy) ")
    Birthdays.append(Collect_Bdays)
    if z == "no":
        Output_Bdays = input("would you like to know someones birthday? ")
        if Birthdays.len(0):#This is to make sure there is a birthday to return
            print("You need to add a birthday first")
        else:
            print(Names)
            input("Whose birthday would you like to know? ")
