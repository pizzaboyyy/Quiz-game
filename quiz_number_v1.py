# quiz_number_v1
# this asks how many times the user wants to be quizzed 10 or 20 or 30 or 40 or 50 times
# i got a bit carried away and made the part which asks the person what the numbers are in english
# and then it also tells your score at the end


import random

how_many_times_quizzed = int(input("How many times do you want to place 10 times, 20 times, 30 times,"
                                  " 40 times or 50 times?: "))
print(f"You will be quizzed {how_many_times_quizzed} times")

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

print()
print(f"you got {score} out of {how_many_times_quizzed} correct ")
print()
print("Thank you for playing!")
