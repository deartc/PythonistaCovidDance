# import datetime and format date for current date and future date to meet criteria
import datetime
# import re for regular expressions
import re
# import random for dance game
import random


# extract emails from String By Regular Expression to meet criteria

s = """ Group fitness dance class information email lablastlablass@gmail.com
         and the website pythonistacoviddance@google.com"""

# \S matches any non-whitespace,@ for as in the Email
# + for Repeats a character one or more times
Contact = re.findall('\S+@\S+', s)
print(Contact)
# code for  datetime and format date for current date and future date to meet criteria
Current_Date_Formatted = datetime.datetime.today().strftime('%d-%b-%Y')
print('Fitness Start Date: ' + str(Current_Date_Formatted))

# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2021, 5, 29, 18, 25, 30)
b = datetime.datetime(2021, 5, 22, 8, 21, 10)

# returns the Time difference in days
c = a - b
print('Difference between Fitness Start Date and End Date: ', c)


# code that meets project criteria of conversion.  Pounds  to calories (used in previous step of program)

pounds = float(input('Enter weight in Pounds(Lbs) to Convert into Calories:'))
Cals = pounds * 3500
print(pounds, ' Pounds (Lbs) are equal to', Cals, 'Calories (Calories)')


def get(question):  # ask how many calories burned
    calories = input(question)
    if calories.isdigit():  # Check to see if calories are float or integer
        calories = int(calories)
        if calories > -1 and calories < 50000:  # Check to see if calorie count is reasonable
            return calories
        else:
            print("Invalid input")
            return get(question)  # If fail, the function must run again
    else:
        print("Use positive numbers")
        return get(question)


print("This is how many calories you could burn dancing\n")
print("Please enter your calories for the last 7 days")

week = []
for i in range(7):
    day = get(question="Day " + str(i + 1) + ":")
    week.append(day)

total = sum(week)
average = int(total / 7)

print("Your total calorie burnt for the week from dancing:", total)
print("\nYour average  daily calorie burnt from dancing for the week:", average)

if total > 400:
    print("\nYou are doing great. You will build up endurance in time")
elif total < 800:
    print("\nYou have built up endurance. Congratulations")

#bmi in pounds and inches
def bmi_start():
    print("Body Mass Index (BMI) calculator")
    print("List your weight and height")
    print("Determine Body Mass Index")
    print("Safely encourage healthy habits")

# determine bmi in nonmetric.  This code was in Tkinter to learn the concepts before I modified code

def det():
    bmi_start()
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = float(input("Please enter your height in inches. "))
    get_weight = float(input("Please enter your weight in pounds. "))
    body_mass_index = (get_weight * 703) / (get_height ** 2)
    if body_mass_index < 18.5:
        print("A person with a BMI of " + str(body_mass_index ) + " is underweight  or  a tiny dancer ")
    elif body_mass_index < 24.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is normal weight ")
    else:
        print("A person with a BMI of " + str(body_mass_index ) + " could be ligher on their feet ")

    
det ()

#determine bmi in metric and to learn  try except error concept

def met_bmi(height, weight):
    #calculate (BMI)
    return weight / height**2


def des_bmi(bmi):
    #evaluate bmi
    if 18.5 <= bmi <= 24.9:
        return 'normal weight'

    if bmi >= 25:
        return 'could be lighter on your feet'

    return 'tiny dancer'

#used try except value error at least once in project to understand concept
def trial():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except ValueError as error:
        print(error)
    else:
        bmi = round(met_bmi(height, weight), 1)
        statement = des_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {statement}!')

trial()

# string is initialized to determine how many words in sentences and paragraphs
test_string = "Fitness after Covid requires patience"

# string is printed
print("The motivation sentence is : " + test_string)

# words counted
res1 = len(test_string.split())

# result is printed
print("The number of words in string are : " + str(res1))

# string is initialized
test_string = "You must slowly build up to your fitness level"

# string is printed
print("The second motivational sentence is : " + test_string)

# words counted
res2 = len(test_string.split())

# result is printed
print("The number of words in string are : " + str(res2))

# string is initialized
test_string = "Rest between each dance if you need to sit down"

# string is printed
print("The original string is : " + test_string)

# words counted
res3 = len(test_string.split())
# result is printed
print("The number of words in string are : " + str(res3))

# string is initialized
test_string = "Increase your emotional involvement in the dance as you lower your physical involvement"

# string is printed
print("The third motivational sentence is : " + test_string)

res4 = len(test_string.split())
# result is printed
print("The number of words in string are : " + str(res4))


test_string = """Python coding during Covid is positive and allows for
needed exercise breaks. Coding about  getting better reduces stress.  Dance exercise allows for interval training."""

# string is printed
print("The Motivation paragraph is : " + test_string)

res5 = len(test_string.split())
# result is printed10
print("The number of words in string are : " + str(res5))

#this is the dictionary of dance styles

dict1 = {'bolero': 100, 'disco': 100, 'tango': 80,
         'waltz': 90, 'samba': 100, 'rumba': 60}
dict2 = {'quickstep': 200, 'cha cha': 130, 'salsa': 200, 'samba': 100, 'east coast swing': 140, 'jive': 160,
         'bolero': 100, 'disco': 100}
result = {}

print("Slower bpm dances", dict1)
print("Faster bpm dances", dict2)

# intersect dictionaries
# Create a new dictionary which is the intersection of two dictionaries.
# Both key & value must match

# dance bpm intersection
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        result[key] = dict1[key]

print("Dances that  are intermediate bpm100"
      " ", result)
# Two player  dance game (dance instructor and dance student are the players
# Enter number as the selection
# game rules -bolero tops samba
# game rules - disco dances over bolero
# game rules - samba sways over disco
# Dance student gets a turn determined by random
# Dance instructor gets a turn determined by random
# The dance winner (or next dance in class) is determined by games rules


while True:
    print("Enter  number answer \n 1. samba \n 2. bolero \n 3. disco \n")

    # take the input from Dance Student
    answer = int(input("Dance Student turn: "))

    #  Dance Student loop excludes invalid data
    while answer > 3 or answer < 1:
        answer = int(input("enter valid input: "))

    # initialize variables
    if answer == 1:
        answer_name = 'samba'
    elif answer == 2:
        answer_name = 'bolero'
    else:
        answer_name = 'disco'

    # print Dance Student answer
    print("Dance Student answer is: " + answer_name)
    print("\nNow its Dance Instructor turn.......")

    # Dance Instructor chooses randomly any number
    comp_answer = random.randint(1, 3)

    # looping until comp_answer value
    # is equal to the answer value
    while comp_answer == answer:
        comp_answer = random.randint(1, 3)

    # initialize value of comp_answer_name
    # variable corresponding to the answer value
    if comp_answer == 1:
        comp_answer_name = 'samba'
    elif comp_answer == 2:
        comp_answer_name = 'bolero'
    else:
        comp_answer_name = 'disco'

    print("Dance Instructor answer is: " + comp_answer_name)

    print(answer_name + " V/s " + comp_answer_name)

    # condition for winning
    if ((answer == 1 and comp_answer == 2) or
            (answer == 2 and comp_answer == 1)):
        print("bolero wins => ", end="")
        result = "bolero"

    elif ((answer == 1 and comp_answer == 3) or
          (answer == 3 and comp_answer == 1)):
        print("samba wins =>", end="")
        result = "samba"
    else:
        print("disco wins =>", end="")
        result = "disco"

    # Printing either Dance Student or Dance Instructor wins
    if result == answer_name:
        print("<== Dance Student wins ==>")
    else:
        print("<== Dance Instructor wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    # if Dance Student input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
#  loop exit
#  print thanks for playing

print("\nThanks for playing and dancing")
