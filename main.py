import datetime

def Calculate_Bdays(x): #This function accounts for all the birthdays in the list birtdays and finds how many days until then
    x = datetime.datetime.now()
    if Output_Bdays == Names(0):
        Days = x - Birthdays(0)
        print(Names(0)+ "birthdy is" + Birthdays(0)+ "It's in"+ Days)

Names = []
Birthdays = []
x = datetime.datetime.now()
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
        Second_prompt = input("would you like to know someones birthday? ")
        if len(Birthdays) == 0:#This is to make sure there is a birthday to return
            print("You need to add a birthday first")
        else:
            print(Names)
            Output_Bdays=input("Whose birthday would you like to know? ")
            Calculate_Bdays(x)

