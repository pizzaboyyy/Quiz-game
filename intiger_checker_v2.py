# Component to check if the intiger they put in for how many times they want to
# be quizzed is valid
# intiger_checker_v2


def check_integer(input_value):
    try:
        value = int(input_value)
        if value in [10, 20, 30, 40, 50]:
            return True
        else:
            return False
    except ValueError:
        return False


how_many_times_quizzed = input("How many times do you want to be quizzed?\n"
                   "10, 20, 30, 40 or 50 times: ")

if check_integer(how_many_times_quizzed):
    print(f"You will be quizzed {how_many_times_quizzed} times")
else:
    print("Input is either not an integer or not 10, 20, 30, 40 or 50.")


