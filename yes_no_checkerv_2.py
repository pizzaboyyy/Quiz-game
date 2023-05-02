# yes/no checking function
# check if user has played the game before
# if they have continue with game if they have not played show instructions
# also check if input is valid
# yes_no_checker_v2

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


# Main routine goes here
played_before = yes_no("Have you played this game before: ")
