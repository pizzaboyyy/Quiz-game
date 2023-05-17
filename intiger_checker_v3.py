# Component to check if the integer they put in for how many times they want to
# be quizzed is valid
# integer_checker_v3

# function to check integers
how_many_times_quizzed = (input("How many times do you want to place 10 times, 20 times, 30 times\n"
                                  " 40 times or 50 times?: "))


def check_integer(input_value):
    try:
        value = int(input_value)
        if value in [10, 20, 30, 40, 50]:
            return True
        else:
            return False
    except ValueError:
        return False


valid_answer = False

while not valid_answer:
    if check_integer(how_many_times_quizzed):
        valid_answer = True
        print(f"You will be quizzed {how_many_times_quizzed} times")
    else:
        print("Input is either not an integer or not 10, 20, 30, 40 or 50.\n"
              "Please enter a valid number")
        how_many_times_quizzed = input(
            "How many times do you want to place 10 times, 20 times, 30 times\n"
            " 40 times or 50 times?: ")


