# Component to check if the intiger they put in for how many times they want to
# be quizzed is valid
# intiger_checker_v1

how_many_times_quizzed = int(input("How many times do you want to place 10 times, 20 times, 30 times,"
                                  " 40 times or 50 times?: "))


if how_many_times_quizzed == 10 or 20 or 30 or 40 or 50:
    print(f"You will be quizzed {how_many_times_quizzed} times")
else:
    print("Enter a valid input")



