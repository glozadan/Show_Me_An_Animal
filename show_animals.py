#Import the animals from the script animals.py
import animals


#List the options in a dictionary
menu = {
    '0': '0. Exit',
    '1': '1. Butterfly',
    '2': '2. Wolf',
    '3': '3. Squirrel',
    '4': '4. Dog',
    '5': '5. Turtle'
}

#Iniitialize a loop that allows the user select an animal and exit the game when needed.
while True:
    print('THIS IS SHOW ME AN ANIMAL')
    for option in menu.values():
        print(option)
    user_imput = int(input('Please, select an option. '))
    if user_imput == 0:
        print("Thanks for playing!")
        break
    elif user_imput == 1:
        print(animals.Butterfly)
    elif user_imput == 2:
        print(animals.Wolf)
    elif user_imput == 3:
        print(animals.Squirrel)
    elif user_imput == 4:
        print(animals.Dog)
    elif user_imput == 5:
        print(animals.Turtle)
    else:
        print("That is an INVALID OPTION, please TRY AGAIN.")
