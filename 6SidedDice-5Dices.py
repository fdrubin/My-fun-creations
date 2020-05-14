from random import randint
import sys
import time

print('''





Hey Maddox, thank you for the challenge. Now let's begin.''')

NumberOfSides = int(input("How many sides would you like on the dice(s)? "))

while NumberOfSides > 0:
    print(
        f"Alright let's use {NumberOfSides} as our number of sides on the dice(s) ")
    break
else:
    print("Cannot compute... overload commenced...")
    time.sleep(2)
    sys.exit()


NumberOfDices = int(input("How many dices are we using? "))


while NumberOfDices > 0:
    print(
        f"Awesome, it looks like we're using {NumberOfDices} dice(s), I like that number.. not like I have a choice...")
    break
else:
    "I'm MELTINGGGGGG..."
    sys.exit()

while True:
    answer = input("Want to roll the dice(s) now? (yes/no) ").lower()
    if "no" in answer:
        print("Welp thats too bad, next time then.")
        sys.exit()

    if "yes" in answer:
        print("Very well then.")
    break


roll = input("Press R to roll the dice(s), press A to quit: ")
while roll.lower() == "r":
    print(f"Rolling the {NumberOfDices} dice(s)....")
    time.sleep(2)
    a = NumberOfDices
    b = NumberOfSides
    for x in range(a):
        print(randint(1, b))

    roll = input("Press R to roll again, A to quit. ")

print('''

Hope you had fun Maddy:)

''')
