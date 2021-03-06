#Dirk Johnson
#This program is a general combination of all the skills I have learned from the programming exercises and coding we have done
print("Hello there, \nWelcome to a program that aims to show off \neverything I have learned in this class so far.")
print(" \nPress Enter when you are ready to continue at all stops during the program.")
input() #This is used to pace the program down so that all of the code isn't shown at once
print("To start off I need some basic information about you")
mothers_maiden_name = (input("What is your mother's maiden name?:"))
first_pets_name = (input("What was your first pet's name?:"))
print("Ok now that I can log into your bank account, we can ACTUALLY get started. \nI'm kidding of course I don't know how to do that...yet.")
input()
number_of_times_eaten_out = (input("How many times a week would you say you eat out?:"))
while True:   #this while function tests the users input and makes sure it is an appropriate input
    try:      #I got help figuring out this loop from https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
        number_of_times_eaten_out = float(number_of_times_eaten_out)
    except ValueError:
        number_of_times_eaten_out = input("Invalid input. Please try again: ")
    else:
        break
while int(number_of_times_eaten_out) < 0: #this checks and makes sure the user cant input a number less than or equal to -1 because you cant go out a negative amount of times.
    number_of_times_eaten_out = input("Invalid input. please try again.")
    while True:
        try:
            number_of_times_eaten_out = float(number_of_times_eaten_out)
        except ValueError:
            number_of_times_eaten_out = input("Invalid input. Please try again: ")
        else:
            break
average_cost_eating_out = (input("Ok and on average how much would you say you spend each time you go out?:$"))
while True:
    try:
        average_cost_eating_out = float(average_cost_eating_out)
    except ValueError:
        average_cost_eating_out = input("Invalid input. Please try again: ")
    else:
        break
while average_cost_eating_out < 0:
    average_cost_eating_out = input("Invalid input. please try again: ")
    while True:
        try:
            average_cost_eating_out = float(average_cost_eating_out)
        except ValueError:
            average_cost_eating_out = input("Invalid input. Please try again: ")
        else:
            break
while number_of_times_eaten_out > 0:
    while average_cost_eating_out <= 0:
        average_cost_eating_out = (input("Invalid input. Please try again: "))
        while True:
            try:
                average_cost_eating_out = float(average_cost_eating_out)
            except ValueError:
                average_cost_eating_out = input("Invalid input. Please try again: ")
            else:
                break
    break   #this break allows the first while loop to terminate as soon as the user enters a value that satisfies the second while loops condition
average_cost_for_year = int((number_of_times_eaten_out *52)* average_cost_eating_out) #this takes the user input for number of times per week they eat out and scales it up to how many times they eat per year and then, multiplies it by the average cost per time eaten out.
print("So on average you spend about $"+format(average_cost_for_year,".2f"),"eating out per year.") #the + between $ and the average_cost_for_year makes it so the $ and number value are right next to each other instead of there being a space
input()
print("After seeing that number be higher than you likely thought it was, \nhow about we take out some of that frustration?")
angry_word = input("What do you say when your angry?: ")
times_said = (input("On a scale from 1 to 10 how angry are you right now: "))
while True:
    try:
        times_said = float(times_said)
    except ValueError:
        times_said = input("Invalid input. Please try again: ")
    else:
        break
while float(times_said) > 10 or float(times_said) < 1: #this makes sure the user stays between 1 and 10 for their input
    times_said = (input("Invalid input. Please try again: "))
    while True:
        try:
            times_said = float(times_said)
        except ValueError:
            times_said = input("Invalid input. Please try again: ")
        else:
            break
for x in range(round(float(times_said))): #this prints the users word the number of times they input rounded to the nearest whole number for that many number of columns and rows
    for x in range(round(float(times_said))):
        print(angry_word + " ", end=" ")
    print()
print("Feel better? \nGood, now we can continue right along.")
input()
name = input("I should have asked this earlier, but what is your name?: ")
def time_worked_percentage(age,time_at_job):  #this function calculates the percentage the user has worked at their current job based on their input values
    age_in_months = age * 12
    percentage_worked = float(format(((time_at_job / age_in_months)*100),".2""f"))
    return percentage_worked
def main():  #this function takes the user inputs, checks to make sure they are appropriate, and passes the parameters onto the function that calculates the time worked at their job percentage
    age = (input("Also, how old are you?:"))
    while True:
        try:
            age = float(age)
        except ValueError:
            age = input("Invalid input. Please try again: ")
        else:
            break
    while age < 1:
        age = (input("Invalid input. Please try again: "))
        while True:
            try:
                age = float(age)
            except ValueError:
                age = input("Invalid input. Please try again: ")
            else:
                break
    time_at_job = (input("How many months have you worked at your current job?:"))
    while True:
        try:
            time_at_job = float(time_at_job)
        except ValueError:
            time_at_job = input("Invalid input. Please try again: ")
        else:
            break
    while time_at_job < 0:
        time_at_job = (input("Invalid input. Please try again: "))
        while True:
            try:
                time_at_job = float(time_at_job)
            except ValueError:
                time_at_job = input("Invalid input. Please try again: ")
            else:
                break
    while float(format(((time_at_job / (age * 12))*100),".2""f")) > 100:
        time_at_job = (input("Invalid input. Please try again: "))
        while True:
            try:
                time_at_job = float(time_at_job)
            except ValueError:
                time_at_job = input("Invalid input. Please try again: ")
            else:
                break
    print("So ", name,end=', ')  # I got help with figuring out how to use the end = argument thanks to Professor Vanselow and at https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
    print("you have worked about", time_worked_percentage(age,time_at_job), "% of your life so far at this job.")
main()
input()
print("Now before I give you a quick math quiz, I need to make sure my code is calibrated correctly.")
user_number = (input("Please input a number and I will tell you what kind of number it is: "))
while True:
    try:
        user_number = float(user_number)
    except ValueError:
        user_number = input("Invalid input. Please try again: ")
    else:
        break
if user_number > 0:
    print("The number you input was a positive number. It was", user_number)
elif user_number == 0:
    print("The number you input was zero.")
else:  #this assumes that since the users input number wasn't positive or zero, that it must then be negative number
    print("The number input was a negative number. It was", user_number)
input()
print("One more calibration needed.")
def calibration_equation(x,y,z):
    answer = (x+y+z)
    return answer
def main():
    x = (input("Enter a number: "))
    while True:
        try:
            x = float(x)
        except ValueError:
            x = input("Invalid input. Please try again: ")
        else:
            break
    y = (input("Enter another number: "))
    while True:
        try:
            y = float(y)
        except ValueError:
            y = input("Invalid input. Please try again: ")
        else:
            break
    z = (input("Enter one more number: "))
    while True:
        try:
            z = float(z)
        except ValueError:
            z = input("Invalid input. Please try again: ")
        else:
            break
    print("I will now add these three number together")
    print(float(x), "+", float(y), "+", float(z), "=", format(calibration_equation(x,y,z), ".2f"))
main()
input()
print("Now for a quick little math quiz")
print("If I were to tell you that the variables")
print("(x=3)","(y=4)","(z=5)", sep = " ")#I also received help with the sep = argument from Professor Vaneslow and https://www.geeksforgeeks.org/python-sep-parameter-print/?ref=rp
print("Could you solve the equation (x^3+(y/x))+(z^2-3x)")
print("with the answer rounded to the nearest whole number.")
def math_equation():
    x = 3
    y = 4
    z = 5
    solution = (pow(x,3) + (y / x)) + (pow(z,2) - x * 3)
    solution //= 1  #this uses a shortcut operator the shortens the expression solution = solution // 1
    return round(solution)  #this rounds the value received from the equation to the nearest whole number
def main():
    user_solution = (input("Enter solution: "))
    while True:
        try:
            user_solution = float(user_solution)
        except ValueError:
            user_solution = input("Invalid input. Please try again: ")
        else:
            break
    while user_solution != math_equation():
        if user_solution == 43.8:
            user_solution = input("Don't forget to round to the nearest whole number: ")
            while True:
                try:
                    user_solution = float(user_solution)
                except ValueError:
                    user_solution = input("Invalid input. Please try again: ")
                else:
                    break
        else:
            user_solution = (input("Your answer was incorrect. Please try again: "))
            while True:
                try:
                    user_solution = float(user_solution)
                except ValueError:
                    user_solution = input("Invalid input. Please try again: ")
                else:
                    break
    if float(user_solution) == math_equation():
        print("Congratulations on getting the answer correct!\nYour answer:", int(user_solution), "equals",math_equation())
main()
input()
print("Now that you've passed my math test, its only fair that you get a prize right?")
animal_selection = input("Choose either Owl, Frog, Snowman, or Bunny: ")
acceptable_inputs = ["Owl","owl","Frog","frog","Snowman","snowman","Bunny","bunny"] # I got help with the mechanics of a list and testing it against a while loop from https://stackoverflow.com/questions/55450907/while-loop-in-python-3-using-lists-and-if-statement-for-begginer
while True:  #this test to see if the users input is inside of the list of acceptable answers. if not then the user is asked for another input until they input an answer that is in the list
    while animal_selection not in acceptable_inputs:
        animal_selection = input("Invalid input. Please try again: ")
    break   #this break allows the first while loop to terminate as soon as the user enters a value that satisfies the second while loops condition
if animal_selection == "Owl" or animal_selection == "owl":
    print("Owl")
    def owl():
        print("{o,o}")
        print(" /)_) ")
        print(" \"\"")
    owl()
if animal_selection == "Frog" or animal_selection == "frog":
    print("Frog")
    def frog():
        print("  @..@")
        print(" (----)")
        print("( >__< )")
        print("^^ ~~ ^^")
    frog()
if animal_selection == "Snowman" or animal_selection == "snowman":
    print("Snowman")
    def snowman():
        print("   _[_]_")
        print("   (*.*)")
        print(">-(  :  )-<")
        print(" (   :   )")
    snowman()
if animal_selection == "Bunny" or animal_selection == "bunny":
    print("Bunny")
    def bunny():
        print("(\(\ ")
        print("( -.-)")
        print("o_(\")(\")")
    bunny()
input()
print("Ok, well until I learn more coding techniques and brainstorm up some new ideas,")
print("I am afraid this is all I have for you right now")
print("Have a wonderful day",name, ", and I hope Mrs."+mothers_maiden_name,"and",first_pets_name,"are doing well.")
