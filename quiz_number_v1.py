import random

how_many_times_quized = int(input("How many times do you want to place 10 times, 20 times, 30 times,"
                                  " 40 times or 50 times?: "))

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

while quiz_number <= how_many_times_quized / 2:
    for num in number_list:
        answer = input(f"What is the English translation of {num} ? ")
        if answer.lower() == maori_numbers[num]:
            print("Correct")
            score += 1
            quiz_number += 1
        else:
            print(f"Incorrect, the correct translation was {maori_numbers[num]}")
            quiz_number += 1

print(f"you got {score} out of 10 correct ")

