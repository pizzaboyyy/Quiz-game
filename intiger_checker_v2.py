# Component to check if the integer they put in for how many times they want to
# be quizzed is valid
# integer_checker_v2

# function to check integers
def check_integer_input():
    while True:
        user_input = input("Enter an integer (10, 20, 30, 40, or 50): ")
        try:
            integer_value = int(user_input)
            if integer_value in [10, 20, 30, 40, 50]:
                return integer_value
            else:
                print("Please enter a valid integer (10, 20, 30, 40, or 50).")
        except ValueError:
            print("Please enter an integer.")

# Example usage
num = check_integer_input()
print("You entered:", num)



