# Base component v2
# fixing my stupid game

import random


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")

        print(f"You entered '{answer}'")


# function to display instructions
def instructions():
    print("***** How to play ******")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


played_before = yes_no("Have you played this game before: ")

if played_before == "No":
    instructions()
else:
    print("program continues")


how_many_times = int(input("How many times do you want to place 10 times, 20 times, 30 times\n"
                           " 40 times or 50 times?: "))
how_many_times_quizzed = 0


def check_integer(input_value):
    try:
        value = int(input_value)
        if value in [10, 20, 30, 40, 50]:
            return True
        else:
            return print("Input is either not an integer or not 10, 20, 30, 40 or 50.\n"
                         "Please enter a valid number")
    except ValueError:
        return False


if how_many_times == [10 or 20 or 30 or 40 or 50]:
    how_many_times = how_many_times_quizzed
else:
    print(input(how_many_times))


# dictonary of Maori numbers and what they are in english
maori_numbers = {"tahi": "one",
                 "rua": "two",
                 "toru": "three",
                 "whā": "four",
                 "rima": "five",
                 "ono": "six",
                 "whitu": "seven",
                 "waru": "eight",
                 "iwa": "nine",
                 "tekau": "ten"
                 }

score = 0
number_list = list(maori_numbers.keys())
random.shuffle(number_list)
quiz_number = -1

while quiz_number < how_many_times_quizzed:
    for num in number_list:
        answer = input(f"What is the English translation of {num} ? ")
        if answer.lower() == maori_numbers[num]:
            print("Correct")
            score += 1
            quiz_number += 1
        else:
            print(f"Incorrect, the correct translation was {maori_numbers[num]}")
            quiz_number += 1

print(f"you got {score} out of {how_many_times_quizzed} correct, thanks for playing. ")
