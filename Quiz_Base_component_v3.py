# Base component v2
# fixing my stupid game

import random


# integer checker to check if the integer is valid
def check_integer(input_value):
    try:
        value = int(input_value)
        # if the input is any of these values it continues
        if value in [10, 20, 30, 40, 50]:
            return True
        # Otherwise the program returns false
        else:
            return False
    except ValueError:
        return False


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answers = input(question_text).lower()

        # If they say yes, output 'Program Continues
        if answers == "yes" or answers == "y":
            answers = "Yes"
            return answers

        # If they say no, output 'display instructions'
        elif answers == "no" or answers == "n":
            answers = "No"
            return answers

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")

        print(f"You entered '{answers}'")


# function to display instructions
def instructions():
    print("***** How to play ******")
    print()
    print("You will be asked a Maori number and you have to answer the question in english \n"
          "eg. What is the english translation of tahi?: awnser = one.")
    print()
    print("Have fun!")
    print()


# Asks the user if they have played the game before
played_before = yes_no("Have you played this game before: ")

if played_before == "No":
    instructions()
else:
    print(" ")


# Ask the user how many times they want to be quizzed
how_many_times_quizzed = input("How many times do you want to place 10 times, 20 times, 30 times\n"
                               " 40 times or 50 times?: ")
print(type)
# how_many_times_quizzed = int(check_integer(how_many_times_quizzed))


valid_answer = False

# Loop so when there is not a valid answer it keeps on asking the question until i get a valid answer
while not valid_answer:
    # if the answer is valid it will print how many times they will be quizzed and the program will continue
    if check_integer(how_many_times_quizzed):
        valid_answer = True
        print(f"You will be quizzed {how_many_times_quizzed} times")
    # otherwise they will be asked until there is a valid answer
    else:
        print("Input is either not an integer or not 10, 20, 30, 40 or 50.\n"
              "Please enter a valid number")
        how_many_times_quizzed = input(
            "How many times do you want to place 10 times, 20 times, 30 times\n"
            " 40 times or 50 times?: ")

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
quiz_number = 0

# Loop that keeps on asking a question until quiz_number equals the number of times the person wants to be quizzed
while quiz_number < how_many_times_quizzed:
    # Prints the question
    for num in number_list:
        answer = input(f"What is the English translation of {num} ? ")
        # if the maori number is equal to the enlish number it is correct
        if answer.lower() == maori_numbers[num]:
            print("Correct")
            score += 1
            quiz_number += 1
        # otherwise it is incorrect
        else:
            print(f"Incorrect, the correct translation was {maori_numbers[num]}")
            quiz_number += 1

# something to print what score they got out of how many times they were quizzed
print(f"you got {score} out of {how_many_times_quizzed} correct, thanks for playing. ")
