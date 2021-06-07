import datetime

Current_Date_Formatted = datetime.datetime.today().strftime('%d-%b-%Y')
print('Fitness Start Date: ' + str(Current_Date_Formatted))

# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2021, 5, 29, 18, 25, 30)
b = datetime.datetime(2021, 5, 22, 8, 21, 10)

# returns a timedelta object
c = a - b
print('Difference between Fitness Start Date and End Date: ', c)


# This is code converting Kilograms into pounds and calories

#  code greeting dancers and also an exit code
# code that converts kg (metric) to pounds (used in US) to calories (used in previous step of program)


def print_hi(name):
    # Use a breakpoint in the code line.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import tkinter as tk

    def main():
        window = tk.Tk()
        window.title("Kilograms to Pounds to Calories  Converter")
        window.geometry("375x200")

        # create a label with text Enter Kilograms
        label1 = tk.Label(window, text="Enter Kilograms:")

        # create a label with text Pounds:
        label2 = tk.Label(window, text="Pounds to Calories:")

        # create a label with text Calories:
        label3 = tk.Label(window, text="Calories:")

        # place label1 in window at position x,y
        label1.place(x=50, y=30)

        # create an Entry widget (text box)

        textbox1 = tk.Entry(window, width=12)

        # place textbox1 in window at position x,y
        textbox1.place(x=200, y=35)

        # place label2 in window at position x,y
        label2.place(x=50, y=100)

        # create a label3 with empty text:
        label3 = tk.Label(window, text=" ")

        # place label3 in window at position x,y
        label3.place(x=180, y=100)

        # create a label4 with empty text:
        label4 = tk.Label(window, text=" ")

        # place label4 in window at position x,y
        label3.place(x=240, y=130)

        def btn1_click():
            pounds = round(float(textbox1.get()) * 2.20462 * 3500, 5)
            label3.configure(text=str(pounds) + '  Calories')

        # create a button with text Button 1
        btn1 = tk.Button(window, text="Click Me To Convert", command=btn1_click)
        # place this button in window at position x,y
        btn1.place(x=90, y=150)
        window.mainloop()

    main()


if __name__ == '__main__':
    print_hi('Dancers')


def getCalories(question):  # ask how many calories burned
    calories = input(question)
    if calories.isdigit():  # Check to see if calories are float or integer
        calories = int(calories)
        if calories > -1 and calories < 50000:  # Check to see if calorie count is reasonable
            return calories
        else:
            print("Invalid input")
            return getCalories(question)  # If fail, the function must run again
    else:
        print("Use positive numbers")
        return getCalories(question)


print("This is how many calories you could burn dancing\n")
print("Please enter your calories for the last 7 days")

week = []
for i in range(7):
    day = getCalories(question="Day " + str(i + 1) + ":")
    week.append(day)

total = sum(week)
average = int(total / 7)

print("Your total calorie burnt for the week from dancing:", total)
print("\nYour average  daily calorie burnt from dancing for the week:", average)

if total > 400:
    print("\nYou are doing great. You will build up endurance in time")
elif total < 800:
    print("\nYou have built up endurance. Congratulations")

# string is initialized
test_string = "Fitness after Covid requires patience"

# string is printed
print("The original string is : " + test_string)

# words counted
res = len(test_string.split())

# result is printed
print("The number of words in string are : " + str(res))

# string is initialized
test_string = "You must slowly build up to your fitness level"

# string is printed
print("The original string is : " + test_string)

# words counted
res = len(test_string.split())

# result is printed
print("The number of words in string are : " + str(res))

# string is initialized
test_string = "Rest between each dance if you need to sit down"

# string is printed
print("The original string is : " + test_string)

# words counted
res = len(test_string.split())
# result is printed
print("The number of words in string are : " + str(res))

# string is initialized
test_string = "Increase your emotional involvement in the dance as you lower your physical involvement"

# string is printed
print("The original string is : " + test_string)

# words counted
res = len(test_string.split())
# result is printed
print("The number of words in string are : " + str(res))

dict1 = {'bolero': 100, 'disco': 110, 'tango': 80,
         'waltz': 90, 'samba': 100, 'merengue': 60}
dict2 = {'quickstep': 200, 'rhumba': 130, 'salsa': 200, 'samba': 100, 'east coast swing': 140, 'jive': 160,
         'bolero': 100, 'hustle': 110}
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

from random import randint

# create a list of dance options
t = ["samba", "bolero", "disco"]

# random play assigned to the computer
computer = t[randint(0, 2)]

# set player to False so we can create continuous play
player = False

while player == False:
    # set player to True
    player = input("samba, bolero, disco?")
    if player == computer:
        print("Both instructor and dancer picks same dance!")
    elif player == "samba":
        if computer == "bolero":
            print(computer, "steps over", player)
        else:
            print(player, "is selected over", computer)
    elif player == "bolero":
        if computer == "disco":
            print(computer, "steps over", player)
        else:
            print(player, "is selected over", computer)
    elif player == "disco":
        if computer == "samba":
            print(computer, "steps over", player)
        else:
            print(player, "is selected over", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    # To set up continuous loop we set the player to false
    player = False
    computer = t[randint(0, 2)]


# This is a a conversion of kilograms to pounds

# Then we will convert pounds to calories and post only the calories


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import tkinter as tk

    def main():
        window = tk.Tk()
        window.title("Kilograms to Pounds to Calories Converter")
        window.geometry("375x200")

        # create a label with text Enter Kilograms
        label1 = tk.Label(window, text="Enter Kilograms:")

        # create a label with text Pounds:
        label2 = tk.Label(window, text="Pounds to Calories:")

        # place label1 in window at position x,y
        label1.place(x=50, y=30)

        # create an Entry widget (text box)

        textbox1 = tk.Entry(window, width=12)

        # place textbox1 in window at position x,y
        textbox1.place(x=200, y=35)

        # place label2 in window at position x,y
        label2.place(x=50, y=100)

        # create a label3 with empty text:
        label3 = tk.Label(window, text=" ")

        # place label3 in window at position x,y
        label3.place(x=180, y=100)

        def btn1_click():
            pounds = round(float(textbox1.get()) * 2.20462 * 3500, 5)
            label3.configure(text=str(pounds) + '  Calories')

        # create a button with text Button 1
        btn1 = tk.Button(window, text="Click Me To Convert", command=btn1_click)
        # place this button in window at position x,y
        btn1.place(x=90, y=150)
        window.mainloop()

    main()


if __name__ == '__main__':
    print_hi('Dancers, we will convert each kg to pounds and divide each pound by 3500 calories to get weight loss ')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Dancers')

