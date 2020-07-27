#make function to recive birthday information
#get user input for
def birthday_function():
    birth_m = input('Enter birth month ')
    birth_d = int(input('Enter birth day '))
    user_y = input('Enter birth year ')
    user_n = input(' Enter your name ')
    month_days = [0,31,59,90,120,151,181,212,243,274,304,]
    Day = (month_days+ birth_d) - 59 

birthday_function()
